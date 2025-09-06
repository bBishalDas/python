# class employee:
#     language= "java"
#     salary="120000"
    
#     # this is a dunder method, it calls itself every time employee class is initialized or called.
#     def __init__(self):
#         print("I'm creating an object")

#     def get_info(self):
#         print(f"the languade is {self.language}, and the salary is {self.salary}")

# harry= employee()
# harry.name= "harry"
# print(harry.name)
# employee.get_info(harry)

# # here another object is created but nothing is called but still as its been created the dunder method will appear.
# ram=employee()


# dunder method can be used for direct passing through object, like this-
class employee:
    language= "java"
    salary="120000"
    
    def __init__(self, name, salary, language):
        self.name= name 
        self.salary= salary
        self.language= language

# newly set values will always have the preference over before typed values.
harry= employee("harry", 140000, "python")

print(harry.name, harry.salary, harry.language)