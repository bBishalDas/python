# what the globle key word does is that it fix the value of an variable so that it will show the same value inside a fuction or locally.

a= 45

def fuc():
    global a
    a=69
    print(a)


fuc()
print(a)