# "with" makes the file colse by default, and you don't have to close the file expicitly.

with open("file3.txt") as f:
    print(f.read())