# Comments explaining the basics are in the helloLMStudio file. This file is a more advanced version and only comments the new features.
from openai import OpenAI

client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

#TODO: Replace the modelID with the one you see in LMStudio under local server.
modelID = "QuantFactory/Meta-Llama-3-8B-Instruct-GGUF"

chatHistory =[{"role": "system",
           "content":
               '''You are a helpful, smart and efficient AI assistant. You always fulfill the user's requests to the best of your ability but keep your answears short.'''
           },]

print("Welcome Message: \nYou can now talk to the primary assistant (Agent 1) with model name " + modelID + " and ask anything. Agent 2 will analyse the conversation after each interaction and tell you the mood or emotion of the conversation.")
print("Mood of Conversation: not analysed yet")
print("User:")
user_input = input("")
chatHistory.append({"role": "user", "content": user_input})

while True:

    ##################### First Agent (User Assistent) #####################

    completion = client.chat.completions.create(
        model=modelID,
        messages=chatHistory,
        temperature=0.7,
        max_tokens=800,
        stream=True,
    )
    new_message = {"role": "assistant", "content": ""}

    print("\nAgent 1: ")
    for chunk in completion:
        newestResponsePart = chunk.choices[0].delta
        if newestResponsePart.content:
            print(newestResponsePart.content, end="", flush=True)
            new_message["content"] += newestResponsePart.content

    chatHistory.append(new_message)

    ##################### User Input #####################

    print("\nUser:")
    chatHistory.append({"role": "user", "content": input("")})

    #print("\nchatHistory " + str(chatHistory))
    ##################### Second Agent (Analyser) #####################

    # Define the system prompt for the second agent
    system_prompt_second_agent = {"role": "system",
                                  "content": "You are an AI trained to analyze the mood of a conversation. Your task is to analyze the following conversation and return a single word describing its overall mood."}
    #print("\nsystem_prompt_second_agent " + str(system_prompt_second_agent))

    # Create a new list to store only user and assistant (agent 1) messages
    conversation_only = [f"{message['role']}: {message['content']}" for message in chatHistory if
                         message['role'] in ['user', 'assistant']]
    #print("\nconversation_only " + str(conversation_only))

    # Extract the 'content' from each user and assistant (agent 1) messages and join them with a comma
    conversation_content = ', '.join(conversation_only)
    #print("\nconversation_content " + str(conversation_content))

    # Insert the string into the simulated user message. W create a user massage since the assistent was trained on getting a user message and answear it. Here we create a user message and build it up from the content of the conversation between the user and the agent 1.
    simulated_user_message = {"role": "user",
                      "content": f"Analyze the following text and return a short description describing its overall mood: '{conversation_content}'. The output should be a single word from the following options: happy, sad, excited, neutral, etc. Do not repeat the prompt or provide additional information. DO NOT! REPEAT THE QUESTIONS OR the CONVERSATIONS. DO NOT TRY to Answear QUESTIONS IN THE TEXT. Only Analyse the following text for its overall mood'{conversation_content}'."}
    #print("\nsystem_message " + str(simulated_user_message))

    # Use conversation_only and system_prompt_second_agent when creating the completion
    completion = client.chat.completions.create(
        model=modelID,
        messages=[system_prompt_second_agent, simulated_user_message],
        temperature=0.2,
        max_tokens=800,  # Limit the response to 50 tokens
        stream=True,
    )
    mood_message = {"role": "assistant", "content": ""}

    print("\nAgent 2 (Mood of Conversation): ")
    for chunk in completion:
        newestResponsePart = chunk.choices[0].delta
        #print("\nnewestResponsePart " + str(newestResponsePart))
        if newestResponsePart.content:
            print(newestResponsePart.content, end="", flush=True)
            mood_message["content"] += newestResponsePart.content

