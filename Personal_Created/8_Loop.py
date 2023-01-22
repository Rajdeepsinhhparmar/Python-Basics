# Infinite loop
# while True:
#     print(" Hello World")
#
#


# Infinite loop
# # Store the current largest number here.
# largest_number = -999999999
#
# # Input the first value.
# number = int(input("Enter a number or type -1 to stop: "))
#
# # If the number is not equal to -1, continue.
# while number != -1:
#     # Is number larger than largest_number?
#     if number > largest_number:
#         # Yes, update largest_number.
#         largest_number = number
#     # Input the next number.
#     number = int(input("Enter a number or type -1 to stop: "))
#
# # Print the largest number.
# print("The largest number is:", largest_number)







# A program that reads a sequence of numbers
# and counts how many numbers are even and how many are odd.
# The program terminates when zero is entered.

# odd_numbers = 0
# even_numbers = 0
#
# # Read the first number.
# number = int(input("Enter a number or type 0 to stop: "))
# # 0 terminates execution.
# while number != 0 :
#     # Check if the number is odd.
#     if number % 2 == 1:
#         # Increase the odd_numbers counter.
#         odd_numbers += 1
#
#     else:
#         # Increase the even_numbers counter.
#         even_numbers += 1
#
#     # Read the next number.
#     number = int(input("Enter a number or type 0 to stop: "))
#
# # Print results.
# print("Odd numbers count:", odd_numbers)
# print("Even numbers count:", even_numbers)




## Counter
# counter = 5
# while counter:
#     print("Inside the loop.", counter)
#     counter -= 1
# print("Outside the loop.", counter)






## Magic trick
# secret_number = 777
# print(
#     """
#     +================================+
#     | Welcome to my game, muggle!    |
#     | Enter an integer number        |
#     | and guess what number I've     |
#     | picked for you.                |
#     | So, what is the secret number? |
#     +================================+
#     """)
#
# number = int(input("Enter your number: "))
# while number != secret_number:
#     print("Ha ha! You're stuck in my loop!")
#
# print("Well done, muggle! You are free now.")




#LOOP
# i = 1
# while i < 10:
#     print(i,'\n')
#     i += 1


# for i in range(10):
#     print(i)
#     pass


# for i in range(2, 8):
#     print("The value of i is currently", i)


# for i in range(2, 8, 3):
#     print("The value of i is currently", i)


# for i in range(1, 1):
#     print("The value of i is currently", i)


# for i in range(2, 1):
#     print("The value of i is currently", i)


# power = 1
# for expo in range(16):
#     print("2 to the power of", expo, "is", power)
#     power *= 2



# import time
#
# for i in range(1, 6):
#     print(i, " Mississippi")
#     time.sleep(1)
#
# print("Ready or not, here I come!")




# break - example
# print("The break instruction:")
# for i in range(1, 6):
#     if i == 3:
#         break
#     print("Inside the loop.", i)
# print("Outside the loop.")


# continue - example
# print("\nThe continue instruction:")
# for i in range(1, 6):
#     if i == 3:
#         continue
#     print("Inside the loop.", i)
# print("Outside the loop.")





## Remove vowels using loop using continue loop

# word = input("Enter your text: ")
# word = word.upper()
# for i in word:
#     if (i == 'A' or i=='E' or i=='I' or i=='O' or i=='U'):
#         continue
#     print(i)




### The while loop and the else branch ###
# i = 1
# while i < 5:
#     print(i)
#     i += 1
# else:
#     print("else:", i)




### The for loop and the else branch ###
# i = 111
# for i in range(2, 1):
#     print(i)
# else:
#     print("else:", i)
#
# for i in range(5):
#     print(i)
# else:
#     print("else:", i)





### pyramid count ###

# blocks = int(input("Enter the number of blocks: "))
# height = 0
# inlayer = 1
# while inlayer <= blocks:
#     height += 1
#     blocks -= inlayer
#     inlayer += 1
#
# print("The height of the pyramid: ", height)



### Collatz formulated
# c = int(input("Enter your number: "))
# count = 0
# while c != 1 :
#     if c % 2 == 0:
#         c = int(c / 2)
#         count += 1
#         print(c)
#
#     else:
#         c = 3 * c + 1
#         count += 1
#         print(c)
#
# print("Steps = ", count)






