# Rule-Based AI Chatbot 🤖

## Project Overview

This project is a simple Rule-Based AI Chatbot developed using Python.

The chatbot responds to predefined user inputs using a dictionary-based knowledge base and rule-based decision-making. It continuously interacts with the user until an exit command is entered.

## Objectives

- Create a simple rule-based chatbot.
- Implement input sanitization.
- Use a dictionary as a knowledge base.
- Handle multiple predefined user inputs.
- Provide a fallback response for unknown inputs.
- Implement a continuous conversation loop.
- Provide clean exit commands.

## Technologies Used

- Python
- VS Code

## Features

- Greeting responses
- General conversation
- AI-related questions
- Chatbot information
- Help responses
- Polite responses
- Fallback response
- Exit commands
- Case-insensitive input handling

## How It Works

1. The user enters a message.
2. The input is converted to lowercase and unnecessary spaces are removed.
3. The chatbot checks whether the input is an exit command.
4. If it is not an exit command, the chatbot searches the response dictionary.
5. If a matching response is found, it is displayed.
6. If no match is found, a fallback response is displayed.
7. The chatbot continues until the user enters an exit command.

## Example

    🤖 Rule-Based AI Chatbot
    Type 'bye', 'exit', or 'quit' to end the conversation.

    You: hello
    Bot: Hello! How can I help you?

    You: what is your name
    Bot: I am a Rule-Based AI Chatbot.

    You: what is AI
    Bot: AI stands for Artificial Intelligence. It enables computers to perform tasks that normally require human intelligence.

    You: something random
    Bot: Sorry, I don't understand that.

    You: bye
    Bot: Goodbye! Have a great day!

## Future Improvements

- Add more conversational responses.
- Add a graphical user interface.
- Add natural language processing.
- Improve intent recognition.
- Support multiple variations of the same question.

## Author

Developed as part of the DecodeLabs Artificial Intelligence Industrial Training - Project 1.