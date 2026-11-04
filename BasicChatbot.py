
# Basic Chatbot using Python

def chatbot():
    print("==============================")
    print("     WELCOME TO CHATBOT")
    print("==============================")
    print("Bot: Hello! Welcome.")
    print("Bot: You can talk to me.")
    print("Bot: Type 'bye' to exit.")

    while True:
        user = input("\nYou: ").lower()

        if user == "hello" or user == "hi":
            print("Bot: Hi! How can I help you?")

        elif user == "how are you":
            print("Bot: I'm fine, thanks!")

        elif user == "what is your name":
            print("Bot: I am a Python Chatbot.")

        elif user == "what can you do":
            print("Bot: I can chat with you!")

        elif user == "thank you":
            print("Bot: You're welcome!")

        elif user == "bye":
            print("Bot: Goodbye! Have a nice day!")
            break

        else:
            print("Bot: Sorry, I don't understand.")

# Start the chatbot
chatbot()
