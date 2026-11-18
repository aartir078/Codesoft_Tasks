import random

responses = {
    "hello": [
        "Hello! How can I help you?",
        "Hi there! Nice to meet you."
    ],
    "how are you": [
        "I am doing great! Thanks for asking.",
        "I am fine. How can I help you today?"
    ],
    "name": [
        "I am RuleBot, your simple AI chatbot."
    ],
    "help": [
        "I can greet you, answer simple questions, and chat with you."
    ],
    "bye": [
        "Goodbye! Have a great day.",
        "See you again!"
    ]
}

def chatbot():
    print("RuleBot: Hello! Welcome to my chatbot.")
    print("RuleBot: Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ").lower().strip()

        if user_input == "":
            print("RuleBot: Please type something.")
            continue

        if user_input == "bye":
            print("RuleBot:", random.choice(responses["bye"]))
            break

        elif "hello" in user_input or "hi" in user_input:
            print("RuleBot:", random.choice(responses["hello"]))

        elif "how are you" in user_input:
            print("RuleBot:", random.choice(responses["how are you"]))

        elif "name" in user_input:
            print("RuleBot:", random.choice(responses["name"]))

        elif "help" in user_input:
            print("RuleBot:", random.choice(responses["help"]))

        else:
            print("RuleBot: Sorry, I don't understand that yet.")

if __name__ == "__main__":
    chatbot()
