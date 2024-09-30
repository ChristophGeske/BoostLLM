# BoostLLM

BoostLLM is a versatile project aimed at enhancing the performance of Large Language Models (LLMs) through various strategies. It provides users with the flexibility to enable or disable these strategies individually or in combination, allowing for consistent performance improvements tailored to specific projects.

While numerous research papers claim significant advancements in LLM performance, there is a lack of centralized resources that list these papers alongside their implementations. BoostLLM bridges this gap by compiling these strategies into an accessible framework, enabling users to test and validate these improvements within their own projects.

## Table of Contents
- [Overview](#overview)
- [Getting Started](#getting-started)
  - [Software Requirements](#software-requirements)
    - [LMStudio](#lmstudio)
    - [PyCharm IDE with Copilot Plugin](#pycharm-ide-with-copilot-plugin)
  - [Available Projects](#available-projects)
    - [Getting_Started_Project 👶](#getting_started_project-👶)
    - [Two_Agents_Project 🦾🤖](#two_agents_project-🦾🤖)
    - [Voice_Input_And_TTS_Project 🗣️](#voice_input_and_tts_project-🗣️)
    - [Code_Interpreter_Project 👨‍💻](#code_interpreter_project-👨‍💻)
- [Strategies to Improve Performance](#strategies-to-improve-performance)
- [Contributing](#contributing)
- [License](#license)

## Overview

BoostLLM aims to systematically enhance the capabilities of Large Language Models by integrating a variety of improvement strategies. Users can toggle these strategies on or off to evaluate their effectiveness within their specific applications. By consolidating research-backed methods and providing practical implementations, BoostLLM serves as a valuable tool for developers and researchers seeking to optimize LLM performance without altering the underlying model architecture.

## Getting Started

### Software Requirements

#### LMStudio

BoostLLM utilizes LMStudio to download and manage models. LMStudio is chosen for its free availability, ease of installation, extensive selection of open-source models, and seamless API integration.

**Why LMStudio?**
- **Cost-Effective**: Free to use, avoiding the expenses associated with APIs like OpenAI's or Google Gemini's.
- **User-Friendly**: Easy installation and setup process.
- **Versatile**: Supports a wide range of open-source models.
- **Reliable API**: Integrates flawlessly with BoostLLM's codebase.

> **Note**: While LMStudio is ideal for experimentation, you may occasionally switch to premium APIs (e.g., OpenAI, Google Gemini) to leverage their advanced capabilities and ensure compatibility with BoostLLM.

#### PyCharm IDE with Copilot Plugin

For development, BoostLLM recommends using PyCharm Professional (version 2023.2.5) enhanced with the Copilot and CopilotChat plugins.

**Features:**
- **GitHub Copilot**: AI-powered code completion and suggestions.
- **CopilotChat Plugin**: A GPT-4 based assistant with direct access to project files, enabling seamless assistance without manual code copying.

**Benefits:**
- **Increased Productivity**: Accelerates coding with intelligent suggestions.
- **Enhanced Debugging**: Real-time assistance in identifying and fixing issues.
- **Accessible AI Tools**: Free access via GitHub Student Subscription. Non-students can use Microsoft Copilot in the Edge browser, also based on GPT-4.

### Available Projects

BoostLLM is organized into several projects, each demonstrating different aspects of LLM performance enhancement.

#### Getting_Started_Project 👶

A beginner-friendly project to familiarize yourself with LMStudio and the basic interaction with LLMs.

- **helloLMStudio.py**: A simple script that facilitates a basic chat with the model directly within your IDE's terminal.

#### Two_Agents_Project 🦾🤖

Demonstrates a multi-agent system where one agent interacts with the user while another analyzes the conversation.

- **twoAgents.py 🦾🤖 🦾🤖**: Engage in a conversation with Agent 1. Concurrently, Agent 2 analyzes the conversation's mood and provides real-time feedback within the chat.

#### Voice_Input_And_TTS_Project 🗣️

Explore voice-based interactions with LLMs through text-to-speech (TTS) and speech-to-text functionalities.

- **Text_To_Speech.py ✍🗣️**: A concise script (4 lines) for implementing and testing text-to-speech conversion.
- **Voice_To_Text.py 👂✍**: A simple project that transcribes spoken words into text.
- **Realtime_Interactive_Voice_To_Text.py 👂✍**: An advanced project that continuously listens to user input and transcribes it in real-time.

> **TODO**: Speech Processing Pipeline
> Planned Features:
> - Integrate brain-like processing for enhanced speech analysis.
> - Implement a pipeline: 👂✍ ➔ 🧠 ➔ ✍🗣️

#### Code_Interpreter_Project 👨‍💻

Focuses on creating an agent capable of understanding and executing code, along with evaluating its success.

- **codeInterpreter.py 👨‍💻**: Accepts Python code as text, executes it, and returns the output along with any error messages.
- **codingAgent.py 🤖**: Manages user interactions and delegates tasks between the user, the agent, and the codeInterpreter module to ensure seamless code execution and feedback.

## Strategies to Improve Performance

BoostLLM integrates multiple strategies to enhance LLM performance. Each strategy includes expected improvements, costs, pros, cons, and relevant sources.

### 1. Prompt Engineering
- **Expected Improvements**: 10% - 30% (variable based on implementation)
- **Costs**: None
- **Pros**: 
  - Easy to implement and modify.
  - Immediate impact on model responses.
- **Cons**: 
  - Requires creativity and testing to optimize prompts.

**Description**:  
Prompt engineering involves crafting effective prompts to elicit better responses from the LLM. For instance, in twoAgents.py, prompt engineering ensures that the second agent accurately analyzes the conversation mood with concise, one-word outputs, preventing verbose and irrelevant responses.

**Sources**:  
- ChatGPT Prompt Engineering for Developers by deeplearning.ai

### 2. Use Multiple LLMs
- **Expected Improvements**: 15% - 40%
- **Costs**: Computational resources and potential API usage fees.

**Description**:  
Leverage multiple LLMs from different providers to process the same input and compare outputs. This approach can enhance reliability and accuracy by cross-verifying responses.

#### 2.1 Use LLMs from Different Providers

**Implementation**:  
Simultaneously send prompts to models like Gemini, GPT-4, and smaller open-source variants. Display and compare the outputs side-by-side to identify the most accurate or relevant responses.

### 3. Repetition and Output Analysis
- **Expected Improvements**: 20% - 50%
- **Costs**: Increased computational requirements.

**Description**:  
Run multiple instances of the same task in parallel and aggregate the results to improve accuracy.

**Techniques**:  
- **Consensus**: Use majority voting to determine the most likely correct answer.
- **Filtering**: Remove incorrect results using secondary verification, either through another LLM or statistical methods implemented in Python.

### 4. Agents
- **Expected Improvements**: 10% - 35%
- **Costs**: Additional development for multi-agent coordination.

**Description**:  
Implementing specialized agents that handle different aspects of tasks can streamline processes and enhance performance. For example, one agent manages user interactions while another analyzes and provides feedback.

### 5. Fine-Tuning
- **Expected Improvements**: 30% - 70%
- **Costs**: High computational resources and data requirements.

**Description**:  
Fine-tuning involves training the LLM on a specific dataset to improve its performance on targeted tasks. While highly effective, it is resource-intensive and not the first recommended step for performance enhancement.

**Considerations**:
- **Comprehensive Training Set**: Ensure the training data includes both new and existing data to prevent the model from losing its foundational capabilities.
- **Model Size**: Smaller models benefit more significantly from fine-tuning compared to larger ones.
- **Specialized Tasks**: Ideal for distilling complex capabilities from larger models like GPT-4 into smaller, more efficient ones.

> **Note**: Fine-tuning is not covered in BoostLLM's current scope, focusing instead on strategies that do not alter the underlying model.

## Contributing

Contributions are welcome! Whether you're reporting a bug, suggesting a feature, or submitting a pull request, your participation helps improve BoostLLM.

1. Fork the Repository
2. Create a Feature Branch (`git checkout -b feature/YourFeature`)
3. Commit Your Changes (`git commit -m 'Add some feature'`)
4. Push to the Branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

Please ensure your contributions adhere to the project's coding standards and include relevant tests.

## License

This project is licensed under the MIT License.
