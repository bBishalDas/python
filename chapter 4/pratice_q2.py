marks= input("enter the markes of 6 students separated by commas: ").split(',')

marks=[int(mark) for mark in marks]
marks.sort()
print(marks)
