### NOTES ### input method

# 1)The program prompts the user to input some data from the console (most likely using a keyboard, although it is also possible to input data using voice or image);
# 2)the input() function is invoked without arguments (this is the simplest way of using the function); the function will switch the console to input mode; you'll see a blinking cursor, and you'll be able to input some keystrokes, finishing off by hitting the Enter key; all the inputted data will be sent to your program through the function's result;
# 3)note: you need to assign the result to a variable; this is crucial - missing out this step will cause the entered data to be lost;
# 4)then we use the print() function to output the data we get, with some additional remarks.




#input method
# print("Tell me anything...")
# anything = input()
# print("Hmm...", anything, "... Really?")





#error
# anything = input("Enter a number: ")
# something = anything ** 2.0
# print(anything, "to the power of 2 is", something)

#solution
# anything = float(input("Enter a number: "))
# something = anything ** 2.0
# print(anything, "to the power of 2 is", something)





### c = √ a2 + b2 ###
# leg_a = float(input("Input first leg length: "))
# leg_b = float(input("Input second leg length: "))
# hypo = (leg_a**2 + leg_b**2) ** .5
# print("Hypotenuse length is", hypo)



## String operators
# fnam = input("May I have your first name, please? = ")
# lnam = input("May I have your last name, please? = ")
# print("Thank you.")
# print("\nYour name is " + fnam + " " + lnam + ".")



# string replication
# print("+" + 10 * "-" + "+")
# print(("|" + " " * 10 + "|\n") * 5, end="")
# print("+" + 10 * "-" + "+")



#right-angle triangle  str()
# leg_a = float(input("Input first leg length: "))
# leg_b = float(input("Input second leg length: "))
# print("Hypotenuse length is " + str((leg_a**2 + leg_b**2) ** .5))




#Exierces
# x = float(input("Enter value for x: "))
#
# y = 1/(x+(1/(x+(1/(x+(1/x))))))
#
# print("y =", y)



#Exierces
# hour = int(input("Starting time (hours): "))
# mins = int(input("Starting time (minutes): "))
# dura = int(input("Event duration (minutes): "))
# time_hour = (hour + dura//60 + (mins+ dura%60)//60)%24
# time_min = (mins+ dura%60)%60
# print("It will end at " + str(time_hour) + ":" + str(time_min))



#exierces   #most important
# x = int(input("Enter a number: "))
# print(x * "5")
#
#
# x = input("Enter a number: ")
# print(type(x))

# print(123+0.0)