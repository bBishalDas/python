def myfuc():
    print("hello me!!")
    print(f"this function is executed by {__name__}")
    print("well how __name__ works is that it's a string variable that shows \n"
    "if the file is executed by the main file or is being used by import\n"
    "if the file is imported the __name__ will show the name of the file it has been imported by without '.py'.\n"
    "or if the file is directly execute by the main file it will print '__main__'.")

if __name__=="__main__":
    print("this is running directly.")

myfuc()