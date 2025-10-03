l=[3,45,67,89,23]

# to assign s.no. to the items in the list 
index=0
for item in l:
    print(f"s.no. {index} for item {item}")
    index+=1

print("\n")
# but this can be more simplified by using enumerate

for index, item in enumerate(l,1):
    print(f"s.no. {index} for item {item}")