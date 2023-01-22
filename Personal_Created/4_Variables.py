## Notes ## (Variables creation rules)
# 1)the name of the variable must be composed of upper-case or lower-case letters, digits, and the character _ (underscore)
# 2)the name of the variable must begin with a letter;
# 3)the underscore character is a letter;
# 4)upper- and lower-case letters are treated as different (a little differently than in the real world - Alice and ALICE are the same first names, but in Python they are two different variable names, and consequently, two different variables);
# 5)the name of the variable must not be any of Python's reserved words (the keywords - we'll explain more about this soon).


### Keywords ###
# ['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']


## Variable ##

# var = 1
# print(var)


# var = 1
# account_balance = 1000.0
# client_name = 'John Doe'
# print(var, account_balance, client_name)
# print(var)


# var = 1
# print(Var)


# var = "3.8.5"
# print("Python version:" ,var)
# var = "3.9.5"
# print("Python version: " + var)


## assign new values ##

# var = 1
# print(var)
# var = var + 1
# print(var)

# var = 100
# print(var)
# var = 200 + 300
# print(var)


### c = √ a2 + b2 ###
# a = 3.0
# b = 4.0
# c = (a ** 2 + b ** 2) ** 0.5
# print("c =", c)


### Shortcut Operators ###

# x = 2
# sheep = 3
# x *= 2
# sheep += 1
# print(x,sheep)


# i = 5
# j = 6
# x = 3
# var = 2
# rem = 12
# i += 2 * j
# var /= 2
# rem %= 10
# j -= (i + var + rem)
# x **= 2
# print(i,var,rem,j,x)


### Excercies ###
# kilometers = 12.25
# miles = 7.38
#
# miles_to_kilometers = round(miles * 1.61)
# kilometers_to_miles = round(kilometers / 1.61)
#
# print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
# print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")
#




#
# kilometers = 12.25
# miles = 7.38
#
# miles_to_kilometers = miles * 1.61
# kilometers_to_miles = kilometers / 1.61
#
# print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
# print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")



## Excerices ##  #3*x^3 - 2*x^2 + 3x - 1

# x =  0
# x = float(x)
# y = (((3*x)**3)-((2*x)**2)+((3*x))-1)
# print("y =", y)

# test date =>> x =(0,1,-1)



## comments exercies ##

# #this program computes the number of seconds in a given number of hours
# # this program has been written two days ago
#
# a = 2 # number of hours
# seconds = 3600 # number of seconds in 1 hour
#
# print("Hours: ", a) #printing the number of hours
# # print("Seconds in Hours: ", a * seconds) # printing the number of seconds in a given number of hours
#
# print("Seconds in Hours: ",a * seconds)
# #here we should also print "Goodbye", but a programmer didn't have time to write any code
# #this is the end of the program that computes the number of seconds in 3 hour
