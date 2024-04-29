# Requests and responses follow OpenAI's API format but are sent to a local server and have nothing to do with OpenAI's servers.
from openai import OpenAI

# requests and responses are handled by a local server specified by the base_url. The URL http://localhost:1234/v1 indicates that the server is
# running locally on your machine and listens on port 1234. v1 is the version of the API that the server is using.
# the api_key
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

# Define the model variable with the model ID.
#TODO: Replace the modelID with the one you see in LMStudio under local server.
modelID = "QuantFactory/Meta-Llama-3-8B-Instruct-GGUF"

# The chatHistory will be constantly updated. It is a list of messages that have been exchanged between the user and the assistant.
# The very first message in the chatHistory is the system prompt.
chatHistory =[{"role": "system",
           "content":
               '''You are a helpful, smart and efficient AI assistant. You always fulfill the user's requests to the best of your ability.'''
           },]

# Display the initial message for the user in the terminal. With a new line break after System
print("Welcome Message: \nYou can now talk to the assistant with model name " + modelID + " and ask anything.")
# Get the user's first message and add it to the chatHistory.
print("User:")
user_input = input("")
chatHistory.append({"role": "user", "content": user_input})


# While Loop: Keeps the chat session active, allowing for continuous interaction.
while True:
    # Request a chat completion from the local server using the chat chatHistory.
    completion = client.chat.completions.create(
        model=modelID,
        # The message is always the complete chat chatHistory. The complete chatHistory is the memory of the LLM.
        messages=chatHistory,
        # Temperature controls the randomness values closer to 0 makes the responses predictable and conservative.
        # Values closer to 1 allow for more varied and creative outputs.
        temperature=0.7,
        # Stream True, allows the responses to be sent as they are generated in chunks, rather than waiting for the entire response to be completed.
        # Stream False, waits for the entire response to be generated before printing it.
        stream=True,
    )

    # Captures and prints response.
    # A dictionary is created with two keys: role and content. The role is set to "assistant", indicating that this message will be from the assistant.
    # The content is initially an empty string, which will be filled with the assistant’s response.
    new_message = {"role": "assistant", "content": ""}

    print("Assistant: ")
    # When streaming is enabled, response is sent back in chunks (pieces)
    for chunk in completion:
        # The choices-array contains the different completions that the model could generate.
        # Delta is an object within each choice that contains incremental updates to the response. It’s part of the streaming functionality
        # Delta will contain a portion of the text that, when combined with previous deltas, forms the complete response.
        # The content field within delta holds the actual text that has been added in this particular update.
        # Each “choice” represents a possible completion that the model could generate based on the input provided. Even though in most cases only one completion (the first one) is used, the API is designed to support multiple completions.
        # This is why you see an array of choices, even if the array only contains one element.
        newestResponsePart = chunk.choices[0].delta
        # If-clause checks there is any new content in the current chunk to ensure that only non-empty content gets processed.
        if newestResponsePart.content:
            # If there is content, it’s printed to the terminal.
            # end="": By default, the print function ends with a newline character (\n) which is now prevented.
            # flush=True forces Python to “flush” the buffer, writing everything in the buffer to the terminal immediately.
            print(newestResponsePart.content, end="", flush=True)
            # The content is also appended to the content key of the new_message dictionary.
            # This builds up the full response from the model over time.
            new_message["content"] += newestResponsePart.content

    # After processing all chunks, the new_message dictionary, which now contains the complete response from the assistant, is appended to the chatHistory list.
    chatHistory.append(new_message)

    print("\nUser:")
    # Catches user’s next message and appends it to the chat chatHistory.
    # When the input() function is called, Python will pause and wait for the user to enter some text and press Enter
    # before continuing; therefore, the while loop is not constantly requiring resources.
    # The model then takes the complete chat chatHistory and generates a response looking at the very end which contains the new User input, which probaly is a question or command.
    chatHistory.append({"role": "user", "content": input("")})