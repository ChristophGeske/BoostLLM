# LLMsBooster

The idea of this project is to improve the performance of large language models (LLMs) using the latest strategies researchers came up with.

The amount of papers claiming massive improvements in LLM performance is long.

What's missing is a list of all these papers and corresponding implementations with a simple toggles to activate each of them separately or in combination so we can check if they consistently improve the results of our models in our own projects.

# List of Strategies to Improve the Performance

## Fine-Tuning

A promising strategy to improve an LLM for your use case but because of cost and resource requirements not the first step one should do when looking for performance improvements.

We will not cover fine tuning in this project because we only want to look at the strategies which do not change the underlying language model.

However here are some important thoughts you should consider before using fine tuning:
- The training set should not just contain the new data you want the model to improve but should also contain the old data so it doesn’t unlearn the old capabilities(TODO add source)
- Smaller Models benefit much more from fine tuning compared to bigger models.
- Fine Tuning is especially great if you have a special task GPT-4 can solve already and you want to distil the capabilities of GPT-4 into a smaller, faster, cheaper model.
- When using fine Tuning to improve small models with synthetic data created by larger models it makes sense to first improve the answers of the larger model with all the other strategies we discuss in this project.

## Prompt Engineering

Expected Improvements - between ??% and ??%

Costs - Non

Pros:
- easy to change by everyone

Cons:
- reduces Input token number. Less important with ever growing context lengths.


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


# Getting started

I use LMStudio as my model API, because it is free, easy to install, offers many open source models and has an API that works flawlessly in combination with my code project.

You should not start with OpenAI or Google Gemini APIs directly when there are these free options available. LMStudio saves you money and is faster, especially in the beginning and testing phase this is very helpful.
From time to time you should switch to the more powerful APIs though to check if they perform as expected.

For programming I use PyCharm Professional with the Copilot and CopilotChat Plugin. The CopilotChat Plugin is a GPT-4 based Assistent with direct access to the code files in my project. This is very helpful when programing and you don't need to copy and past the code into a chat window. I highly recommend the Github Copilot. I use it for free via my Github student subscription. If you are not a student and don't have access to GPT-4 jet the second best option is Microsoft Copilot in the browser which is also based on GPT-4 and free to use.

helloLMStudio.py is the simplest possible project that returns the response of the API to a hard coded prompt.
