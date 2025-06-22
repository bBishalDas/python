with open("log.txt", "r") as f:
    content=f.read()

if "python" in content:
    print("the word 'python' is present in this file.")
else:
    print("this word doesn't exist in this file.") 