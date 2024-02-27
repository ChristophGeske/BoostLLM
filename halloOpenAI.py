# Import the openai module
import openai

# Create a client object with your API key
client = openai.OpenAI(api_key="sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxx") # Replace this with your OpenAI secret key

# Define your prompt and the engine
prompt = """You are a poetic assistant, skilled in explaining complex programming concepts with creative flair.
User: Compose a poem that explains the concept of recursion in programming.
System:"""
engine = "gpt-3.5-turbo" # Replace this with your preferred engine

# Send your prompt and model to the OpenAI Completions API using the client.completions.create method
response = client.completions.create(model=engine, prompt=prompt, logprobs=0)

# Print the response message
print(response.choices[0].text)