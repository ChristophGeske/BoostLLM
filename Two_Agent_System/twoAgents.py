# Comments explaining the basics are in the helloLMStudio file. This file is a more advanced version and only comments the new features.
from openai import OpenAI

client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

#TODO: Replace the modelID with the one you see in LMStudio under local server.
modelID = "QuantFactory/Meta-Llama-3-8B-Instruct-GGUF"

chatHistory =[{"role": "system",
           "content":
               '''You are a helpful, smart and efficient AI assistant. You always fulfill the user's requests to the best of your ability but keep your answears short.'''
           },]

print("Welcome Message: \nYou can now talk to the primary assistant (Agent 1) with model name " + modelID + " and ask anything. A second agent will analyse the conversation after each interaction and tell you the mood_message of the conversation.")
print("Current Mood of Conversation: not analysed yet")
print("User:")
user_input = input("")
chatHistory.append({"role": "user", "content": user_input})

while True:

    ##################### First Agent #####################

    completion = client.chat.completions.create(
        model=modelID,
        messages=chatHistory,
        temperature=0.7,
        stream=True,
    )
    new_message = {"role": "assistant", "content": ""}

    print("Assistant: ")
    for chunk in completion:
        newestResponsePart = chunk.choices[0].delta
        if newestResponsePart.content:
            print(newestResponsePart.content, end="", flush=True)
            new_message["content"] += newestResponsePart.content

    chatHistory.append(new_message)

    ##################### Second Agent #####################

    # Create a new completion request for the second agent with the prompt "Analyse the conversation and describe its mood_message in one word."
    completion = client.chat.completions.create(
        model=modelID,
        # Here we add the prompt for our analysing agent. It often doesnt completly accept our prompt. Some advanced prompt engeneering might help to align it better.
        messages=chatHistory + [{"role": "assistant", "content": "In a single word, describe the mood of the conversation. Choose e.g. from: happy, sad, angry, neutral, excited, bored, confused, surprised. Only return ONE SINGLE WORD LIKE: happy, sad, angry, neutral, excited, bored, confused, surprised"}],
        temperature=0.7,
        stream=True,
    )

    print("\nCurrent Mood of Conversation: ")
    # We store the respons in a variable to check if it is empty or contains only whitespace. This prevents us from printing
    # the message of the analysing agend immediately but since it is supposed to be a single word that should be fine and still
    # quick enough. It takes some time for the message to be generated, the reason for that is not clear to me yet.
    mood_message = ""
    for chunk in completion:
        newestResponsePart = chunk.choices[0].delta
        if newestResponsePart.content:
            mood_message += newestResponsePart.content
    # Check if mood_message is empty or contains only whitespace
    if not mood_message or mood_message.isspace():
        mood_message = "Mood analysis failed"
    print(mood_message, end="", flush=True)

    # chatHistory is not appended with the mood_message message we used for analysis only. After each exchange the whole chatHistory is analysed again. But the analysation should nor be part of the conversation.

    ##################### User Input #####################

    print("\nUser:")
    chatHistory.append({"role": "user", "content": input("")})