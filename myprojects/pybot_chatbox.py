# chatgpt_clone.py

def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hey there! 😊 How can I help you today?"

    elif "how are you" in user_input:
        return "I'm just code, but I'm doing great! Thanks for asking."

    elif "name" in user_input:
        return "I'm your friendly Python-powered chatbot!"

    elif "bye" in user_input or "exit" in user_input:
        return "Goodbye! Have a great day ahead. 👋"

    elif "help" in user_input:
        return "Sure! You can ask me simple questions like your assistant."

    else:
        return "this wasn't taught me."

# Main Chat Loop
print("🟢 PyBot is online! (type 'exit' to quit)")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("PyBot: 👋 Exiting chat. Bye!")
        break
    response = chatbot_response(user_input)
    print("PyBot:", response)
