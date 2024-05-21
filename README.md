# LLMsBooster

The idea of this project is to improve the performance of large language models (LLMs) using differnt strategies and allow users to switch strategies on and off.

The amount of papers claiming massive improvements in LLM performance is long.

What's missing is a list of all these papers and corresponding implementations with a simple toggles to activate each of them separately or in combination so we can check if they consistently improve the results of our models in our own projects.

# Getting started 

## Software I am using

### LMStudio
I use LMStudio to download model a model and as an API, because it is free, easy to install, offers many open source models and has an API that works flawlessly in combination with my code project.

You should not start with OpenAI's or Google Gemini's payed APIs when there are all these free options available to play around with. 
From time to time you could switch to the more powerful APIs though to check if your software works with them as expected.

### PyCharm IDE with Copilot Plugin
For programming I use PyCharm (Professional 2023.2.5) with the Copilot and CopilotChat Plugin enabled. The CopilotChat Plugin is a GPT-4 based assistent with direct access to the code files in my project. This is very helpful when programing and you don't need to copy and past the code into ChatGPT. I highly recommend the Github Copilot Chat. I use it for free via my Github student subscription. If you are not a student and don't have access to GPT-4 jet the second best option is Microsoft Copilot in the Edge browser which is also based on GPT-4 and free to use.

# Available Projects

## Getting_Started_Project 👶

### helloLMStudio.py 
This is the simplest possible project. A basic chat with the model in the terminal of your IDE. 

## Two_Agents_Project 

### twoAgents.py 🦾🤖 🦾🤖
This is the simplest possible 2 agent project. Have a chat with agent 1 and in the background agent 2 analyses the mood of the conversation and prints it's analysis in the chat. 

## Voice_Input_And_TTS_Project

### Text_To_Speech.py ✍🗣️
A 4 liner for implementing and testing text to speach.

### Voice_To_Text.py 👂✍
A simplest project to see how speech can be transcribed into text. 

### Realtime_Interactive_Voice_To_Text.py 👂✍
An extended project that constantly listens to what the user says.

### TODO👂✍-> 🧠 ->✍🗣️

## Code_Interpreter_Project 
The goal of this module is to create an agent that has the ability to not only see the code itself, but also by running the code learns if the code runs successfully.

### codeInterpreter.py 👨‍💻
This module simply accepts text which should be python code, runs it and returns the output of the code and if it threw any errors. 

### codingAgent.py 🤖
Contains the user conversation and assignes the right messages to the agent, the user and the codeInterpreter module.


# List of Strategies to Improve the Performance

## Prompt Engineering

Expected Improvements - between ??% and ??%

Costs - Non

Pros:
- easy to change

Cons:
- Non

In the twoAgents.py we see the need for prompt engeneering already. There the second agent which task it is to analyse the conversation should only reply with one word that describes the mood of the conversation. Without good prompt engeneering it doesn't always follows the command and e.g. gives answears that are too long.

Sources:

ChatGPT Prompt Engineering for Developers by deeplearning.ai - https://learn.deeplearning.ai/courses/chatgpt-prompt-eng/lesson/1/introduction

## Use Multiple LLMs

### Use LLMs of different providers

Expected Improvements - between ??% and ??%

You can simply use Gemini, GPT-4 or smaller models in parallel. The script sends the prompt to booth models and displays the outputs next to each other.

## Repetition and Output Analysis

Expected Improvements - between ??% and ??%

Multiple instances work on the same task in parallel. The results are then analysed by:

- Consensus: Majority vote helps find the most likely correct solution.
- filtering: Wrong results are removed. One way is by using another LLM to check the results or statistical methods that are able to find errors. these Statistical methods could be written in python by another LLM making it possible to use the correct statistical methods for the specific output to filter.



## Agents

Expected Improvements - between ??% and ??%


## Fine-Tuning

A promising strategy to improve an LLM for your use case but because of cost and resource requirements not the first step one should do when looking for performance improvements.

We will not cover fine tuning in this project because we only want to look at the strategies which do not change the underlying language model.

However here are some important thoughts you should consider before using fine tuning:
- The training set should not just contain the new data you want the model to improve but should also contain the old data so it doesn’t unlearn the old capabilities(TODO add source)
- Smaller Models benefit much more from fine tuning compared to bigger models.
- Fine Tuning is especially great if you have a special task GPT-4 can solve already and you want to distil the capabilities of GPT-4 into a smaller, faster, cheaper model.
- When using fine Tuning to improve small models with synthetic data created by larger models it makes sense to first improve the answers of the larger model with all the other strategies we discuss in this project.



