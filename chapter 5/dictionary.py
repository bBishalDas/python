important_syntax = {
    "1. import": "1. import",
    "2. dictionary": '2. name_of_dict= {"name_of_item": "value of item", name_of_item2": "value of item2"}',
    "3. fuction string": '3. print(f"teaxt funct.{can be used in many ways}")',
    "4. alt use": "4.1. in visual studio multiple cursers can be used using alt+left click \n4.2. use alt+up/down to move the snippet to the upper line or the lower line directly ",
    "5. instance method for dictionary":'1. to display all the items in the list \n syntax-\n  print(name.items()) \n2. to display all the key values in the dictionary \n syntax- \n  print(name.keys())\n3. to update the dictionary. \n syntax \n  name.update({"harry": 99, "navidi": 45}) \n4. to get a value of a spesific key from the dictionary. \n syntax-\n  print(name.get(name_of_the_key) \n5. to print all the values asigned the the keys. \n syntax- \n  print(name.values())'
     
}

# print(*important_syntax.values(), sep="\n")
print(important_syntax.get("5. instance method for dictionary"))
print(f"this dictionary contains {len(important_syntax)} elements.")