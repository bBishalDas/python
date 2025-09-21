# class vector:
#     def __str__(self):
#         return f"7i+8j+10k"
    
# v=vector()
# print(v)

# OR

class vector:
    def __init__(self, x, y, z):
        self.x=x
        self.y=y
        self.z=z

    def __add__(self, v2):
        result= vector(self.x+v2.x, self.y+v2.y, self.z+v2.z)
        return result
    
    def __mul__(self, v2):
        result= self.x*v2.x + self.y*v2.y + self.z*v2.z
        return result
    
    def __str__(self):
        return  f"{self.x}i + {self.y}j + {self.z}k"
    
v1=vector(1,3,5)
v2=vector(2,4,6)
v3=vector(7,8,9)    

print(v1+v2)
print(v1*v2)

print(v1+v3)
print(v1*v3)
    