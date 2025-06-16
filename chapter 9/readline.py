f= open("file2.txt")

lines=f.readlines()

print(lines, type(lines))
f.close() # type: ignore

# you can also control the lines to be red by using readline

j= open("file3.txt")

line1=j.readline()
print(line1)

line2=j.readline()
print(line2)

line3=j.readline()
print(line3)

line4=j.readline()
print(line4)

line5=j.readline()
print(line5)

line6=j.readline()
print(line6)
j.close()