# program that finds if a student has passed or not when passing persentage is 40% and in each at least 33%

# maths=int(input("enter your marks here: "))
# science=int(input("enter your marks here: "))
# python=int(input("enter your marks here: "))

# if maths<40:
#     print(f"you have failed in maths by {40-int(maths)}")
# if science<40:
#     print(f"you have failed in science by {40-int(science)}")
# if python<40:
#     print(f"you have failed in python by {40-int(python)}")

# persentage= ((100)*(maths+science+python))/300

# if persentage>=40:
#  print(f"congratulations you have passed your test. your total persentage is: {int(persentage)}%")
# this one which i made have has one flaw that is that 




# can also be used-
maths = int(input("Enter your maths marks: "))
science = int(input("Enter your science marks: "))
python = int(input("Enter your python marks: "))

failed = False  # A flag to check if any subject is failed

if maths < 40:
    print(f"You have failed in Maths by {40 - maths} marks.")
    failed = True
if science < 40:
    print(f"You have failed in Science by {40 - science} marks.")
    failed = True
if python < 40:
    print(f"You have failed in Python by {40 - python} marks.")
    failed = True

if not failed:
    percentage = ((maths + science + python) / 300) * 100
    print(f"Congratulations! You passed the test. Your percentage is: {int(percentage)}%")
