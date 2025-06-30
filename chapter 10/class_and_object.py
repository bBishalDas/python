class car:
    brand='toyota'  # class atrribute
    color='red'
    year='2020'


# also the instance atrribute has more preferance than the class atrribute
# so if you do 'mycar.color="blue"' blue will be printed instead of red
mycar= car()
# mycar.color='blue'
mycar.name='ruum ruum' # name also called the instance attribute
print(mycar.brand, mycar.color, mycar.year, mycar.name)

# also the name is n object attribute and the brand, color and year all are class atrribute as 
# they are directly comes from the class.
