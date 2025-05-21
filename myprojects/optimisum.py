optimistic_dict= {
    "bad": "good",
    "never": "always",
    "can't": "can",
    "boring": "exciting",
    "bored": "excited",
    "uncool":"cool",
    "not cool":"cool",
    "not good": "not bad",
    "disable": "special",
    "weak": "strong",
    "dumb": "smart",
    "too hard": "too easy",
    "don't": ""
}
print("😊lets make your thougths more positive")
sentence= input("😆enter your thougths here: ").strip()

correction_made= False

for bad_word in optimistic_dict:
    
    if bad_word in sentence.lower():
        sentence = sentence.replace(bad_word, optimistic_dict[bad_word]).strip()
        correction_made=True
        
if correction_made:
  print(f"Here💎, this is more like it: {sentence}")
else:
  print("🥇 that's the spirit king 👑")