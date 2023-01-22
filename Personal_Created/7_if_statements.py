# if statement
# if_else statement
# nested if statement
# elif statemwnt


# Exercise

### Method 1
# Read two numbers
# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))
#
# # Choose the larger number
# if number1 > number2:
#     larger_number = number1
# else:
#     larger_number = number2
#
# # Print the result
# print("The larger number is:", larger_number)





### Method 2
# Read two numbers
# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))
#
# # Choose the larger number
# if number1 > number2: larger_number = number1
# else: larger_number = number2
#
# # Print the result
# print("The larger number is:", larger_number)





### Methos 3
# # Read three numbers
# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))
# number3 = int(input("Enter the third number: "))
#
# # We temporarily assume that the first number
# # is the largest one.
# # We will verify this soon.
# largest_number = number1
#
# # We check if the second number is larger than current largest_number
# # and update largest_number if needed.
# if number2 > largest_number:
#     largest_number = number2
#
# # We check if the third number is larger than current largest_number
# # and update largest_number if needed.
# if number3 > largest_number:
#     largest_number = number3
#
# # Print the result
# print("The largest number is:", largest_number)



## Pseudocode
# largest_number = -999999999
# number = int(input())
# if number == -1:
#     print(largest_number)
#     exit()
# if number > largest_number:
#     largest_number = number
#     print(largest_number)




##method 5 using max() and min() function
# # Read three numbers.
# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))
# number3 = int(input("Enter the third number: "))
#
# # Check which one of the numbers is the greatest
# # and pass it to the largest_number variable.
#
# largest_number = max(number1, number2, number3)
# lowest_number = min(number1, number2, number3)
# # Print the result.
# print("The largest number is:", largest_number)
# print("The lowesr number is:", lowest_number)






### Excercies
# plant = input("Enter your favorite plant: ")
#
# if plant == "Spathiphyllum":
#     print("Yes - Spathiphyllum is the best plant ever!")
#     exit()
#
# if plant == "spathiphyllum":
#     print("No, I want a big Spathiphyllum!")
#     exit()
#
# else:
#     print("Spathiphyllum! Not ",plant," !")






### Excersices

# if the citizen's income was not higher than 85,528 thalers, the tax was equal to 18% of the income minus 556 thalers and 2 cents (this was the so-called tax relief)
# if the income was higher than this amount, the tax was equal to 14,839 thalers and 2 cents, plus 32% of the surplus over 85,528 thalers.

# income = float(input("Enter the annual income: "))
#
# if income <= 85528:
#     tax =( income * 18/100) - 556
# else:
#     tax = 14839 + (( income - 85528 ) *32 /100 )
# tax = round(tax, 0)
# print("The tax is:", tax, "thalers")





## Excercies

# if the year number isn't divisible by four, it's a common year;
# otherwise, if the year number isn't divisible by 100, it's a leap year;
# otherwise, if the year number isn't divisible by 400, it's a common year;
# otherwise, it's a leap year.


# year = int(input("Enter a year: "))
#
# if year % 4 == 0:
#     print("Common year")
#
# elif year % 100 != 0:
#     print("Leap year")
#
# elif year % 400 != 0:
#     print("Common year")
#
# else:
#     print("Leap year")









# # EX1
# x = 10

# if x == 10: # condition
#     print("x is equal to 10")  # Executed if the condition is True.





# #EX2
# x = 10

# if x > 5:  # condition one
#     print("x is greater than 5")  # Executed if condition one is True.

# if x < 10:  # condition two
#     print("x is less than 10")  # Executed if condition two is True.

# if x == 10:  # condition three
#     print("x is equal to 10")  # Executed if condition three is True.





# #Ex3
# x = 10

# if x < 10:  # Condition
#     print("x is less than 10")  # Executed if the condition is True.

# else:
#     print("x is greater than or equal to 10")  # Executed if the condition is False.





# #Ex4
# x = 10

# if x > 5:  # True
#     print("x > 5")

# if x > 8:  # True
#     print("x > 8")

# if x > 10:  # False
#     print("x > 10")

# else:
#     print("else will be executed")




# #EX5
# x = 10

# if x == 10:  # True
#     print("x == 10")

# if x > 15:  # False
#     print("x > 15")

# elif x > 10:  # False
#     print("x > 10")

# elif x > 5:  # True
#     print("x > 5")

# else:
#     print("else will not be executed")




# #Ex6
# x = 10

# if x > 5:  # True
#     if x == 6:  # False
#         print("nested: x == 6")
#     elif x == 10:  # True
#         print("nested: x == 10")
#     else:
#         print("nested: else")
# else:
#     print("else")




# #Exercise 7
# x = 5
# y = 10
# z = 8
#
# print(x > y)
# print(y > z)
#
#
# #Exercise 8
# x, y, z = 5, 10, 8
#
# print(x > z)
# print((y - 5) == x)
#
#
# #Exercise 9
# x, y, z = 5, 10, 8
# x, y, z = z, y, x
#
# print(x > z)
# print((y - 5) == x)
#
#
# #Eexercise 10
# x = 10
#
# if x == 10:
#     print(x == 10)
# if x > 5:
#     print(x > 5)
# if x < 10:
#     print(x < 10)
# else:
#     print("else")
#
#
# #Exercise 11
# x = "1"
#
# if x == 1:
#     print("one")
# elif x == "1":
#     if int(x) > 1:
#         print("two")
#     elif int(x) < 1:
#         print("three")
#     else:
#         print("four")
# if int(x) == 1:
#     print("five")
# else:
#     print("six")
#
#
#
# #Exercise 12
# x = 1
# y = 1.0
# z = "1"
#
# if x == y:
#     print("one")
# if y == int(z):
#     print("two")
# elif x == y:
#     print("three")
# else:
#     print("four")


