class name:
    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    
    # here wihtin the program the name provided by the user is split and stored as first name and last name.
    @name.setter
    def ename(self, value):
        self.fname= value.split(" ")[0]
        self.lname= value.split(" ")[1]

a=name()

a.ename="Bishal Das"
print(a.fname, a.lname)
print(a.ename)