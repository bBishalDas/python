l=[1,4,6,7,8,9,9,11]





for index,item in enumerate(l,1):
    
    if (index%2)!=0:
        print(item)  
    # or
    if index==3 or index==5 or index==7:
        print(item)