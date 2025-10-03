l_of_num=[1,2,4,9,5,8]

# this method helps to shorten list related opperations
# so instead of this-

square_of_l=[]

for i in l_of_num:
    square_of_l.append(i*i)
print(square_of_l)

# you can do this, its more time efficient and more practical-

square_of_l=[i*i for i in l_of_num]

print(square_of_l)

