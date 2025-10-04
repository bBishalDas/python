user=int(input("enter the number you want the table of: "))

table=str([user*i for i in range(1,11)])
print(table)

with open("table.txt", "a") as f:
    f.write(table + "\n")
