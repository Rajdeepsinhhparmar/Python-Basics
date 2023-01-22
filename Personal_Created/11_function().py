# def message():
#     a = str(input("Enter your string: "))
#     return a

# a = message()

# print("We start here.")
# print("Entered string was", a)
# print("We end here.")




# def hello(name):    # defining a function
#     print("Hello,", name)    # body of the function

# name = input("Enter your name: ")
# hello(name)



### Parameterized function
# def message(number):
#     print("Enter a number:", number)


# def message(number):
#     print("Enter a number:", number)
#
# number = 6352591729
# message(number)


### Parametrized functions
# def message(what, number):
#     print("Enter", what, "number", number)
#
# message("telephone", 11)
# message("price", 5)
# message("number", "number")



### Mine
# def message():
#     what = input("Enter your parameters: ")
#     number = input("Enter numeric value of according to parameter: ")
#     print(what, "value is ",number)
#     return what,number
#
# message()




# def introduction(first_name, last_name):
#     print("Hello, my name is", first_name, last_name)
#
# introduction("Skywalker", "Luke")
# introduction("Quick", "Jesse")
# introduction("Kent", "Clark")




# def introduction(first_name, last_name):
#     print("Hello, my name is", first_name, last_name)
#
# introduction(first_name = "James", last_name = "Bond")
# introduction(last_name = "Skywalker", first_name = "Luke")




# def adding(a, b, c):
#     print(a, "+", b, "+", c, "=", a + b + c)
#
# # Call the adding function here.
# adding(10,2,3)
# adding(c = 1, a = 2, b = 3)
# adding(3, a = 1, b = 2) #error statement



###Parametrized functions
# def introduction(first_name, last_name="parmar"):
#     print("Hello, my name is", first_name, last_name)
#
# introduction("Rajdeep")
# introduction("Rajdeep","sinh")
# introduction(first_name="Rajdeep")
# introduction(first_name="Rajdeep",last_name="william")
# introduction(last_name="william")  #error condition




### Calculator

# def calculator():
#     a = int(input("Enter first value: "))
#     b = int(input("Enter second value: "))
#
#     i = input("Enter operator like add, sub, div, mul: ")
#     operation = ["add","sub","div","mul"]
#
#     if i == "add" :
#         print(a," + ",b," = ",a + b)
#         return a,b
#
#     elif i == "sub" :
#             print(a," - ",b," = ",a - b)
#             return a,b
#
#     elif i == "div" :
#             print(a, " / ", b, " = ", a / b)
#             return a,b
#
#     elif i == "mul":
#             print(a," * ",b," = ",a * b)
#             return a,b
#
#     else:
#             print("Wrong value entered")
#
#
# calculator()



### Return

# def list_sum(lst):
#     s = 0
#
#     for elem in lst:
#         s += elem
#
#     return s
#
#
# print(list_sum([5, 4, 3]))


# def strange_decending_list_fun(n):
#     strange_list = []
#
#     for i in range(0, n):
#         strange_list.insert(0, i)
#
#     return strange_list
#
#
# print(strange_decending_list_fun(5))
#
#
# def strange_ascending_list_fun(n):
#     strange_list = []
#
#     for i in range(n):
#         strange_list.append(i)
#
#     return strange_list
#
#
# print(strange_ascending_list_fun(5))




## leap year

# def is_year_leap(year):
#
#     if (year % 4) == 0:
#         if (year % 100) == 0:
#             if (year % 400) == 0:
#                 print(year," is a leap year")
#                 return "true"
#             else:
#                 print(year," is not a leap year")
#                 return "false"
#         else:
#             print(year," is a leap year")
#             return "true"
#     else:
#         print(year," is not a leap year")
#         return "false"
#
# print(is_year_leap(2000))




### leap_year with day's in a month
#
# def is_year_leap(year, month):
#     if (year % 4) == 0:
#         if (year % 100) == 0:
#             if (year % 400) == 0:
#                 leap = 1
#                 return leap
#             else:
#                 leap = 0
#                 return leap
#         else:
#             leap = 1
#             return leap
#
#     else:
#         leap = 0
#         return leap
#
#
# year = int(input("Enter year: "))
# month = int(input("Enter month: "))
# leap = is_year_leap(year, month)
#
# if leap == 1:
#     print(year," is leap year and Number of day's in", month, "month is: ", 28 + leap)
#
# else:
#     list = [1, 3, 5, 7, 8, 10, 12]
#
#     if month in list:
#         print(year, " is not leap year and Number of day's in", month, "month is:30")
#
#     elif month == 2:
#         print(year, " is not leap year and Number of day's in", month, "month is:28")
#
#     else:
#         print(year, " is not leap year and Number of day's in", month, "month is:31")
#





### global variable

# def my_function():
#     global var
#     var = "Rajdeep"
#     print("Do I know that variable?", var)
#
# var = 1
# my_function()
# print(var)




## addition list

# def my_function(n):
#     print("I got", n)
#     n += 1
#     print("I have", n)


# var = 1
# my_function(var)
# print(var)



## Replace list

# def my_function(my_list_1):
#     print("Print #1:", my_list_1)
#     print("Print #2:", my_list_2)
#     my_list_1 = [0, 1]
#     print("Print #3:", my_list_1)
#     print("Print #4:", my_list_2)


# my_list_2 = [2, 3]
# my_function(my_list_2)
# print("Print #5:", my_list_2)



## Delete list

# def my_function(my_list_1):
#     print("Print #1:", my_list_1)
#     print("Print #2:", my_list_2)
#     del my_list_1[0]  # Pay attention to this line.
#     print("Print #3:", my_list_1)
#     print("Print #4:", my_list_2)


# my_list_2 = [2, 3]
# my_function(my_list_2)
# print("Print #5:", my_list_2)




### BMI index

# def bmi(weight, height):
#     return weight / height ** 2
#
#
# print(bmi(52.5, 1.65))



### evaluating BMI and converting imperial units to metric units


# def ft_and_inch_to_m(ft, inch=0.0):
#     return ft * 0.3048 + inch * 0.0254
#
#
# def lb_to_kg(lb):
#     return lb * 0.45359237
#
#
# def bmi(weight, height):
#     if height < 1.0 or height > 2.5 or weight < 20 or weight > 200:
#         return None
#
#     return weight / height ** 2
#
#
# print(bmi(weight=lb_to_kg(176), height=ft_and_inch_to_m(5, 7)))




###  Some simple functions: continued

# def is_a_triangle(a, b, c):
#     if a + b <= c:
#         return False
#     if b + c <= a:
#         return False
#     if c + a <= b:
#         return False
#     return True


# print(is_a_triangle(1, 1, 1))
# print(is_a_triangle(1, 1, 2))
# print(is_a_triangle(1, 2, 2))
# print(is_a_triangle(2, 2, 2))

# def is_a_triangle(a, b, c):
#     return a + b > c and b + c > a and c + a > b


# print(is_a_triangle(1, 1, 1))
# print(is_a_triangle(1, 3, 3))





### Triangle

# def is_a_triangle(a, b, c):
#     return a + b > c and b + c > a and c + a > b


# a = float(input('Enter the first side\'s length: '))
# b = float(input('Enter the second side\'s length: '))
# c = float(input('Enter the third side\'s length: '))

# if is_a_triangle(a, b, c):
#     print('Yes, it can be a triangle.')
# else:
#     print('No, it can\'t be a triangle.')





### Pythagorean theorem

# def is_a_triangle(a, b, c):
#     return a + b > c and b + c > a and c + a > b
#
#
# def is_a_right_triangle(a, b, c):
#     if not is_a_triangle(a, b, c):
#         return False
#     if c > a and c > b:
#         return c ** 2 == a ** 2 + b ** 2
#     if a > b and a > c:
#         return a ** 2 == b ** 2 + c ** 2
#
#
# print(is_a_right_triangle(5, 3, 4))
# print(is_a_right_triangle(1, 3, 4))






# def is_a_triangle(a, b, c):
#     return a + b > c and b + c > a and c + a > b


# a = float(input('Enter the first side\'s length: '))
# b = float(input('Enter the second side\'s length: '))
# c = float(input('Enter the third side\'s length: '))

# if is_a_triangle(a, b, c):
#     print('Yes, it can be a triangle.')
# else:
#     print('No, it can\'t be a triangle.')



###  Heron's formula

# def is_a_triangle(a, b, c):
#     return a + b > c and b + c > a and c + a > b

# def heron(a, b, c):
#     p = (a + b + c) / 2
#     return (p * (p - a) * (p - b) * (p - c)) ** 0.5

# def area_of_triangle(a, b, c):
#     if not is_a_triangle(a, b, c):
#         return None
#     return heron(a, b, c)

# print(area_of_triangle(1., 1., 2. ** .5))




### factorials


# def factorial_function(n):
#     if n < 0:
#         return None
#     if n < 2:
#         return 1
#
#     product = 1
#     for i in range(2, n + 1):
#         product *= i
#     return product
#
#
# for n in range(0, 11):  # testing
#     print(n, factorial_function(n))





### Fibonacci

# def fib(n):
#     if n < 1:
#         return None
#     if n < 3:
#         return 1
#
#     elem_1 = elem_2 = 1
#     the_sum = 0
#     for i in range(3, n + 1):
#         the_sum = elem_1 + elem_2
#         elem_1, elem_2 = elem_2, the_sum
#     return the_sum
#
#
# for n in range(1, 10):  # testing
#     print(n, "->", fib(n))





### recursion

# def fib(n):
#     if n < 1:
#         return None
#     if n < 3:
#         return 1
#     return fib(n - 1) + fib(n - 2)
#
#     # return n * factorial_function(n - 1)
#
#     elem_1 = elem_2 = 1
#
#     the_sum = 0
#     for i in range(3, n + 1):
#         the_sum = elem_1 + elem_2
#         elem_1, elem_2 = elem_2, the_sum
#     return the_sum
#
#
# for n in range(1, 10):
#     print(n, "->", fib(n))






