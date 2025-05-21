name_list=["bishal", "raghav", "harry", "yuki"]
name=input("search: ")
if name in name_list:
    print(f"{name} is present in the list.")
else:
    print(f'the name "{name}" is not there in the list.')