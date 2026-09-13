responses = {
    
    "hello": "Hello! How can I help you?",
    "hi": "Hi there! Nice to meet you.",
    "hey": "Hey! How can I help you?",
    "good morning": "Good morning! I hope you're having a great day.",
    "good afternoon": "Good afternoon! How can I help you?",

    
    "what is your name": "I am a Rule-Based AI Chatbot.",
    "can i know your name": "Sure! I am a Rule-Based AI Chatbot.",
    "who are you": "I am a simple AI chatbot created using Python.",
    "what can you do": "I can respond to predefined questions using simple rules.",
    "how do you work": "I use predefined rules and a dictionary to generate responses.",

    
    "how are you": "I'm doing great! Thanks for asking.",
    "how is your day": "My day is going well! Thanks for asking.",
    "are you okay": "Yes! I'm ready to chat with you.",
    "are you a robot": "Yes, I am a simple rule-based chatbot.",
    "are you human": "No, I am a computer program designed to chat with you.",

    
    "help": "You can ask me about my name, capabilities, or how I work.",
    "what is ai": "AI stands for Artificial Intelligence. It enables computers to perform tasks that normally require human intelligence.",
    "what is python": "Python is a popular programming language known for its simple and readable syntax.",
    "what is a chatbot": "A chatbot is a computer program designed to communicate with users through conversation.",
    "what is rule based ai": "Rule-based AI uses predefined rules and conditions to make decisions and generate responses.",

   
    "thank you": "You're welcome! Happy to help.",
    "thanks": "You're welcome!",
    "please": "Of course! How can I help you?",
    "nice to meet you": "Nice to meet you too!",

    
    "tell me a joke": "Why did the computer go to the doctor? Because it had a virus!",
    "are you smart": "I'm smart enough to follow my programmed rules!",
    "do you like me": "Of course! I enjoy chatting with you.",

}
print("Rule-Based AI Chatbot")
print("Type 'bye', 'exit', or 'quit' to end the conversation.")
print("-" * 50)

while True:
    user_input = input("You: ").lower().strip()

    if user_input in ["bye","goodbye","exit", "quit"]:
        print("Bot: Goodbye! Have a great day!")
        break

    response = responses.get(
        user_input,
        "Sorry, I don't understand that."
    )

    print("Bot:", response)