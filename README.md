# LLMsBooster

GPT-4 and Gemini are the best Large Language Models out there today with similar performance in benschmarks.

However lots of research goes into how to improve them further.

What's missing is a list of all these papers and corresponding implementations with simple toggles to activate them and see if they truely improve the results in your projects.

The idea is to uss this LLM Booster as if it where the GPT-4 or Gemini API. It should work the same it takes in a prompt and returns an output message. Since OpenAI and Google always add new features like "Memory", "Instructions", ... which help to improve the results they should also still be acessible.

Fine-Tuning would be nice for some use cases as well, but is not possible with these close source state of the art LLMs.

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

Expected Improvements - between ??% and ??%

You can simply use Gemini and GPT-4 in paralle. The script sends the prompt to booth models and displays the outputs next to each other.



## Agents

Expected Improvements - between ??% and ??%


# Getting started

halloOpenAI.py is the simplest possible project that returns the respons of the API to a hard coded prompt.


