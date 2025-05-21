key_word=["bishal das","bishal"]
sentence= input("post: ").lower()

found=False
for name in key_word:

 if name in sentence:
     found=True
     break
 
if found:
   print("this post is about you.")
else:
   print("this post is not about you.")