# Her we would like to have a system maybe based on multiple agents that analyse the conversation and store cases where the conversation failed. It would also be possible to let the models talk to themself and find out their own weaknesses and store them. One could imagine that one LLM googles facts onloine that are easy to ask and check but hard to generate. This way the judge model can test another model and figutre out its weaknesses and store them.


from openai import OpenAI
from difflib import SequenceMatcher

client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

# TODO: Replace the modelID with the one you see in LMStudio under local server.
modelID = "QuantFactory/Meta-Llama-3-8B-Instruct-GGUF"

chatHistory = [{"role": "system",
                "content": '''You are a helpful, smart and efficient AI assistant. You always fulfill the user's requests to the best of your ability but keep your answers short.'''
                }, ]

# List to store weaknesses
weaknesses = []

print("Welcome Message: \nYou can now talk to the primary assistant (Agent 1) with model name " + modelID + " and ask anything. A second agent will analyze the conversation after each interaction and tell you the mood_message of the conversation.")
print("Current Mood of Conversation: not analyzed yet")
print("User:")
user_input = input("")
chatHistory.append({"role": "user", "content": user_input})


def is_similar(question, weaknesses, threshold=0.7):
    """Check if the question is similar to any known weaknesses."""
    for weak_question in weaknesses:
        similarity = SequenceMatcher(None, question, weak_question).ratio()
        if similarity > threshold:
            return True
    return False


while True:
    ##################### First Agent (User Assistant) #####################

    # Check if the current question is similar to known weaknesses
    if is_similar(user_input, weaknesses):
        print("Assistant: I'm sorry, I can't answer that question.")
        chatHistory.append({"role": "assistant", "content": "I'm sorry, I can't answer that question."})
    else:
        # Generate response using the primary agent
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

    ##################### Second Agent (Analyzer) #####################

    # Analyzing the conversation for weaknesses
    analysis_prompt = [
        {"role": "system", "content": "You are an AI that identifies weaknesses in conversations."},
        *chatHistory,
        {"role": "assistant", "content": "Identify any weaknesses in the assistant's response."}
    ]
    completion = client.chat.completions.create(
        model=modelID,
        messages=analysis_prompt,
        temperature=0.7,
        stream=True,
    )

    weakness_detected = ""
    for chunk in completion:
        newestResponsePart = chunk.choices[0].delta
        if newestResponsePart.content:
            weakness_detected += newestResponsePart.content.strip()

    if weakness_detected and weakness_detected.lower() != "none":
        print("\nWeakness Detected: ", weakness_detected)
        # Add the problematic question to the weaknesses list
        weaknesses.append(chatHistory[-2]["content"])
    else:
        print("\nNo weaknesses detected.")

    ##################### Mood Analysis #####################
    mood_analysis_prompt = [
        {"role": "system", "content": "You are an AI that analyzes conversation moods."},
        *chatHistory,
        {"role": "assistant", "content": "In a single word, describe the mood of the conversation. Choose e.g. from: happy, sad, angry, neutral, excited, bored, confused, surprised. Only return ONE SINGLE WORD LIKE: happy, sad, angry, neutral, excited, bored, confused, surprised"}
    ]
    completion = client.chat.completions.create(
        model=modelID,
        messages=mood_analysis_prompt,
        temperature=0.7,
        stream=True,
    )

    print("\nCurrent Mood of Conversation: ")
    mood_message = ""
    for chunk in completion:
        newestResponsePart = chunk.choices[0].delta
        if newestResponsePart.content:
            mood_message += newestResponsePart.content
    if not mood_message or mood_message.isspace():
        mood_message = "Mood analysis failed"
    print(mood_message, end="", flush=True)

    print("\nUser:")
    user_input = input("")
    chatHistory.append({"role": "user", "content": user_input})