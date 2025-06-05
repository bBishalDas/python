f= open("file2.txt")

lines=f.readlines()

print(lines, type(lines))
f.close()