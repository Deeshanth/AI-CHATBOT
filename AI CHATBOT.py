from datetime import datetime

print("Welcome to the Simple Chatbot!")
print("Type 'bye' to exit.\n")

while True:
    msg = input("You: ").lower()

    if msg == "hi" or msg == "hello":
        print("Bot: Hello! Nice to meet you.")

    elif "how are you" in msg:
        print("Bot: I'm fine. Thanks for asking. How are you?")

    elif "your name" in msg:
        print("Bot: My name is ChatBot.")

    elif "time" in msg:
        print("Bot: Current time is", datetime.now().strftime("%H:%M"))

    elif "date" in msg:
        print("Bot: Today's date is", datetime.now().strftime("%d-%m-%Y"))

    elif "thanks" in msg or "thank you" in msg:
        print("Bot: You're welcome!")

    elif msg == "bye":
        print("Bot: Goodbye. Have a nice day!")
        break

    else:
        print("Bot: Sorry, I don't understand. Please try another question.")