# class employee:
#     salary=45000 
#     def increment(self, n):
#         print(f"this yers increment {self.salary+n}")


# rise = employee()

# rise.increment(5000)

class employee:
    salary=45000
    increment= 20

    @property
    def salaryafterincrement(self):
        return (self.salary + self.salary*(self.increment/100))
    
    @salaryafterincrement.setter
    def salaryafterincrement(self, salary):
        self.increment= ((salary/self.salary)-1)*100



income=employee()
print(income.salaryafterincrement)
income.salaryafterincrement= income.salaryafterincrement
print(income.increment)