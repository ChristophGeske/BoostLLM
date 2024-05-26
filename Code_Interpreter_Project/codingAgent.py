# The goal of this module is to create an agent that has the ability to not only see the code itself,
# but also learns by running the code if the code runs successfully.

# Import the necessary libraries and functions
from openai import OpenAI
from codeInterpreter import runCode

# Initialize the OpenAI client with your local server details
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

# TODO Replace the modelID with the one from your LMStudio. You will find it under local server in LM Studio.
modelID = "QuantFactory/Meta-Llama-3-8B-Instruct-GGUF"

# Initialize the chat history with a system message
chatHistory = [{"role": "system", "content": "You are a helpful, smart, and efficient AI assistant. Respond to the Users messages in a short response. Only say more if you have to add useful information helping the user suceed."}]

# Welcome message for the user
print("Hi. How can I assist you? If you have code use trigger word 'code' and we can check your code together.")

# Main conversation loop
while True:
    # Get the user input
    user_input = input("User: ")

    # Check if the user input contains the word 'code', 'coding', or 'programming'
    if 'code' in user_input.lower() or 'coding' in user_input.lower() or 'programming' in user_input.lower():
        # Ask the user if they want to check code
        print("Do you have some code you want me to run?")
        user_response = input("User (Type y or yes to check code): ")
        if user_response.lower() in ['yes', 'y']:
            # Prompt the user to enter their code
            print("Please paste your code below and I'll take a look:")
            code_to_run = input("Code: ")

            # Run the code using the runCode function
            print("\nRunning code...")
            output, _ = runCode(code_to_run)
            if output:
                print("Result:", output)
                # Append the user's code and the result to the user_input
                user_input = f"\nUser's code: {code_to_run}\nResult of running your code: {output}"
            else:
                print("No output from the code execution.")
                user_input = f"\nUser's code: {code_to_run}\nNo output from the code execution."

            # Append the user's code and its output to the chatHistory
            chatHistory.append({"role": "user", "content": user_input})
        else:
            print("Alright, let's continue our conversation. What else would you like to talk about?")
    elif 'exit' in user_input.lower() or 'quit' in user_input.lower():
        # Exit the conversation loop if the user wants to quit
        print("No code provided. Back to the Conversation with the Assistant.")
        break
    else:
        # Normal conversation flow
        chatHistory.append({"role": "user", "content": user_input})

    # Generate the assistant's response
    completion = client.chat.completions.create(
        model=modelID,
        messages=chatHistory,
        temperature=0.7,
        stream=True,
    )

    # Process the completion and add the assistant's response to the chat history
    new_message = {"role": "assistant", "content": ""}
    for chunk in completion:
        newestResponsePart = chunk.choices[0].delta
        if newestResponsePart.content:
            new_message["content"] += newestResponsePart.content

    chatHistory.append(new_message)
    print("Assistant:", new_message["content"])