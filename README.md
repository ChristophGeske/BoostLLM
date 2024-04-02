# LLMsBooster

GPT-4 and Gemini are the best Large Language Models out there today with similar performance in benschmarks.

However lots of research goes into how to improve them further.

What's missing is a list of all these papers and corresponding implementations with simple toggles to activate them and see if they truely improve the results in your projects.

The idea is to uss this LLM Booster as if it where the GPT-4 or Gemini API. It should work the same it takes in a prompt and returns an output message. Since OpenAI and Google always add new features like "Memory", "Instructions", ... which help to improve the results they should also still be acessible.

Fine-Tuning would be nice for some use cases as well, but is not possible with these close source state of the art LLMs.

Bing Copilot is also using GPT-4 but seems not to offer an official API (TODO: Find an inofficial API). It would be a great solution for users wanting to try out this Boosters abilities for free.

# List of Strategies to Improve the Performance

## Prompt Engeneering

Expected Improvements - between ??% and ??%

Costs - Non 

Pros:
- easy to change by everyone

Cons:
- reduces Input token number. Less important with ever growing context lengths.


Sources:

ChatGPT Prompt Engineering for Developers by deeplearning.ai - https://learn.deeplearning.ai/courses/chatgpt-prompt-eng/lesson/1/introduction

## Use Multiple LLMs

### Use LLMs of differnt providers

Expected Improvements - between ??% and ??%

You can simply use Gemini, GPT-4 or smaller models in parallel. The script sends the prompt to booth models and displays the outputs next to each other.

## Repetition and Ourput Analysis

Expected Improvements - between ??% and ??%

Multiple instances work on the same task in parallel. The reults are then analysed by:

- Consensus: Mayority vote helps find the most likely correct solution.
- filtering: Wrong results are removed. One way is by using another LLM to check the results or statistical methods that are able to find errors. theses Statistical methods could be eritten ion python by another LLM making it possible to use the correct statistical methods for the specific output to filter.



## Agents

Expected Improvements - between ??% and ??%


# Getting started

halloOpenAI.py is the simplest possible project that returns the respons of the API to a hard coded prompt.


