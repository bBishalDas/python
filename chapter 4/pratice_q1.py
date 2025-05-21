# write a code in python to store 7 fruit names.
fruit_list= input("enter 7 fruit names separated by commas: ").strip().split(',')



for index, fruit_list in enumerate(fruit_list, start=1):
 print(f"{index}.{fruit_list}")