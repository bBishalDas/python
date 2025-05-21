trans_etoh={
    "me na":"I",
    "me":"I",
    "mene kiya":"I did",
    "kesa he":"how are you",
    "kese":"how",
    "kesa":"how",
    "sab":"everything",
    "thik he tu?":"are you good?",
    "thik he":"good",
    "thik":"good"
}

eng=input("write your hindlish text here: ").strip()
translate=False
for words in trans_etoh:
    if words in eng.lower():
        eng= eng.replace(words, trans_etoh[words]).strip()
        translate=True
if translate:
   print(f"here is yor translation: {eng}")
else:
   print("your sentance is already in English")

