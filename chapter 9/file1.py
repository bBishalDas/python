'''
what the file I/O is used is to open a file read or write in it through python.
'''

# import os

# # Change the working directory to the folder of the script
# os.chdir(os.path.dirname(__file__))

# Now open the file
f= open("file.txt", "r")
data = f.read()
print(data, end="")
f.close()