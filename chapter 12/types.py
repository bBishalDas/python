from typing import List, Dict, Tuple, Union  #using these types you can also specify the type of the value you re using

number: List[int]= [1,2,3,4,]
# sprcifing that the list only have int values

name: Tuple[str, int]= ("bishal", 345)
# the values of tuple have both str and int values

soures: Dict[str, int] = {"books": 1234, "novels": 456}
# dictionary with str key and int value

indentifier: Union[int, str]= "gh45hdu56"
# union specifies that the value can has both str and int value in it.

n: int=5

name : str= "bishal"

def sum(a: int, b:int) -> int:
    return a+b

print(sum(2,4))

# here it may seem that, i have only assigned types of the variables and as python is a dynamic language it seems inefficient but 
# when working wihtin a groupe when more than 2 people are coding on the same project this can help navigate the other codders to 
# the same path, making it easier to collaborate, with each other better and not make  mess of each others code.