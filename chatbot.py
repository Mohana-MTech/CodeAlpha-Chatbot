import random
from datetime import datetime

# Responses
responses = {
    "greetings": {
        "hello": "Hello! Nice to meet you.",
        "hi": "👋 hi there! How are you?",
        "how are you": "I’m fine, thanks for asking! How about you?"
    },
    "jokes": [
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "Why did the Python developer go broke? He kept importing antigravity!",
        "I told my computer I needed a break… it said 'No problem, I’ll go to sleep.'"
    ],
    "quotes": [
        "'Code is like humor. When you have to explain it, it’s bad.'",
        "'Talk is cheap. Show me the code.'",
        "'First, solve the problem. Then, write the code.'"
    ]
}

def chatbot():
    print("Welcome to your CodeAlpha Chatbot, Mohana!")

    print("\nOptions:")
    print("1. Greetings (chat with me)")
    print("2. Tell me a joke")
    print("3. Share a motivational quote")
    print("4. Show current date & time")
    print("5. Exit")

    while True:
        choice = input("\nEnter your choice (1-5): ")

        if choice == "1":
            user_input = input("You: ").lower()
            if user_input in responses["greetings"]:
                print("Chatbot:", responses["greetings"][user_input])
            else:
                print("Chatbot: Sorry, I don’t understand that greeting.")
        elif choice == "2":
            print("Chatbot:", random.choice(responses["jokes"]))
        elif choice == "3":
            print("Chatbot:", random.choice(responses["quotes"]))
        elif choice == "4":
            now = datetime.now()
            print("Chatbot: Current date & time is", now.strftime("%Y-%m-%d %H:%M:%S"))
        elif choice == "5":
            print("Chatbot: Goodbye! Have a wonderful day")
            break
        else:
            print("Chatbot: Invalid choice, please try again.")

# Run the chatbot
chatbot()
