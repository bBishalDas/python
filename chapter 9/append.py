st= "\nwow!! i am really amazing"
# using "a" in the mode of open will allow this programe to append/write st in the end of the file given to open.
# this will happen everytime the code is run.
f=open("newfile.txt", "a")

f.write(st)
f.close()