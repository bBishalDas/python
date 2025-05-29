def find_greatest(numbers):
    greatest = numbers[0]
    for num in numbers:
        if num > greatest:
            greatest = num
    return greatest

# Taking input from user
user_input = input("Enter numbers separated by commas: ")

# Converting input string to list of integers
number_list = [int(x) for x in user_input.split(",")]

# Finding and printing the greatest number
result = find_greatest(number_list)
print("The greatest number is:", result)