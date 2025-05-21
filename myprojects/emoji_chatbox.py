# emoji_bot.py

def emoji_translate(text):
    # Dictionary of keywords to emojis
    emoji_dict = {
        "happy": "😊",
        "sad": "😢",
        "love": "❤️",
        "tired": "😴",
        "angry": "😡",
        "excited": "🤩",
        "bored": "🥱",
        "hungry": "🍕",
        "cool": "😎",
        "hello": "👋",
        "bye": "👋😢",
        "help": "help😁",
        "funny": "😂",
        
    }

    output = []
    words = text.lower().split()
    
   
    
    for word in words:  
        if word in emoji_dict:
            output.append(emoji_dict[word])
        else:
            output.append(word)

    return ' '.join(output)

# 👾 Chat loop
print("🟢 EmojiBot is online! (type 'exit' to quit)")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("EmojiBot: 👋 Bye-bye!")
        break
    response = emoji_translate(user_input)
    print(f"EmojiBot: {response}")
