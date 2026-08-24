print("🤖 Welcome to DecodeLabs AI Chatbot!")
print("Type 'bye', 'exit', or 'quit' to end the conversation.")

while True:
    user_input = input("You: ").lower().strip()

    if user_input in ["hello", "hi", "hey"]:
        print("Bot: Hello! How can I help you?")

    elif user_input == "how are you":
        print("Bot: I'm doing great! Thanks for asking.")

    elif user_input == "what is ai":
        print("Bot: AI stands for Artificial Intelligence. It helps computers perform tasks that normally require human intelligence.")

    elif user_input == "what is machine learning":
        print("Bot: Machine Learning is a part of AI that allows computers to learn from data.")

    elif user_input == "your name":
        print("Bot: I'm the DecodeLabs AI Chatbot!")

    elif user_input == "thank you":
        print("Bot: You're welcome! 😊")

    elif user_input in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! Have a great day! 👋")
        break

    else:
        print("Bot: Sorry, I don't understand that. Please try another question.")