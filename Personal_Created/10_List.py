# numbers = [10, 5, 7, 2, 1]
# print("List content:", numbers)  # Printing original list content.

# numbers = [10, 5, 7, 2, 1]
# print("Original list content:", numbers)  # Printing original list content.
# numbers[0] = 111
# print("New list content: ", numbers)  # Current list content.


# numbers = [10, 5, 7, 2, 1]
# print("Original list content:", numbers)  # Printing original list content.
# numbers[0] = 111
# print("\nPrevious list content:", numbers)  # Printing previous list content.
# numbers[1] = numbers[4]  # Copying value of the fifth element to the second.
# print("New list content:", numbers)  # Printing current list content.

# print("\nList length:", len(numbers))  # Printing the list's length.

# del numbers[1]  # Removing the second element from the list.
# print("New list's length:", len(numbers))  # Printing new list length.
# print("\nNew list content:", numbers)



## Negative indices are legal
# numbers = [111, 7, 2, 1]
# print(numbers[-1])
# print(numbers[-2])



# # Adding elements to a list: append() and insert()
#
# numbers = [111, 7, 2, 1]
# print(len(numbers))
# print(numbers)
#
# numbers.append(4)
# print(len(numbers))
# print(numbers)
#
# numbers.insert(0, 222)
# print(len(numbers))
# print(numbers)


# #Adding elements to a list: continued
#
my_list = []  # Creating an empty list.

for i in range(5):
    my_list.append(i * 2)

print(my_list)


## reverse
# my_list = []  # Creating an empty list.
#
# for i in range(5):
#     my_list.insert(0, i + 1)
#
# print(my_list)



# my_list = [10, 1, 8, 3, 5]
# total = 0
#
# for i in range(len(my_list)):
#     total += my_list[i]
#
# print(total)
#
#
# my_list = [10, 1, 8, 3, 5]
# total = 0
#
# for i in my_list:
#     total += i
#
# print(total)





### Swip number in list ###
# my_list = [10,1,2,4,5,9]
# total = 0

# c = my_list [1]
# my_list[1] = my_list[0]
# my_list[0] = c

# print(my_list)



# my_list = [10, 1, 8, 3, 5]


# my_list[0], my_list[4] = my_list[4], my_list[0]
# my_list[1], my_list[3] = my_list[3], my_list[1]
# print(my_list)



# my_list = [10, 1, 8, 3, 5]
# length = len(my_list)

# for i in range(length // 2):
#     my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]

# print(my_list)




### Exercise ###

# step 1: create an empty list named beatles;
# step 2: use the append() method to add the following members of the band to the list: John Lennon, Paul McCartney, and George Harrison;
# step 3: use the for loop and the append() method to prompt the user to add the following members of the band to the list: Stu Sutcliffe, and Pete Best;
# step 4: use the del instruction to remove Stu Sutcliffe and Pete Best from the list;
# step 5: use the insert() method to add Ringo Starr to the beginning of the list.


## Step : 1

# beatles = []
# print("Step 1:", beatles)
#
# ## Step : 2
# name = ["John Lennon","Paul MacCartney","George Harrison"]
# i = 0
# for i in range(len(name)):
#     beatles.append(name[i])
# print("Step 2:", beatles)





## Exerices

# lst = [1, 2, 3, 4, 5]
# lst.insert(1, 6)
# del lst[0]
# lst.append(1)

# print(lst)



# lst = [1, 2, 3, 4, 5]
# lst_2 = []
# add = 0

# for number in lst:
#     add += number
#     lst_2.append(add)

# print(lst_2)



# lst = []
# del lst
# print(lst)



# lst = [1, [2, 3], 4]
# print(lst[1])
# print(len(lst))





### Bubble short

# my_list = [8, 10, 6, 2, 4]  # list to sort
# j = 1
# for i in range(len(my_list) ):  # we need (5 - 1) comparisons
#     for j in range(len(my_list)):
#
#         if my_list[i] > my_list[j]:  # compare adjacent elements
#             my_list[i], my_list[j] = my_list[j], my_list[i]  # If we end up here, we have to swap the elements.
#         j += 1
#
#
#     else: j+=1
#
#     i +=1
#
# print(my_list)

# my_list = [8, 10, 6, 2, 4]  # list to sort
# swapped = True  # It's a little fake, we need it to enter the while loop.
#
# while swapped:
#     swapped = False  # no swaps so far
#     for i in range(len(my_list) - 1):
#         if my_list[i] > my_list[i + 1]:
#             swapped = True  # a swap occurred!
#             my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
#
# print(my_list)





# my_list = []
# swapped = True
# num = int(input("How many elements do you want to sort: "))
#
# for i in range(num):
#     val = float(input("Enter a list element: "))
#     my_list.append(val)
#
# while swapped:
#     swapped = False
#     for i in range(len(my_list) - 1):
#         if my_list[i] > my_list[i + 1]:
#             swapped = True
#             my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
#
# print("\nSorted:")
# print(my_list)


# lst = [5, 3, 1, 2, 4]
# print(lst)
#
# lst.sort()
# print(lst)  # outputs: [1, 2, 3, 4, 5]



# lst = [5, 3, 1, 2, 4]
# print(lst)
#
# lst.reverse()
# print(lst)  # outputs: [4, 2, 1, 3, 5]



# lst = ["D", "F", "A", "Z"]
# lst.sort()
#
# print(lst)



# a = 3
# b = 1
# c = 2
#
# lst = [a, c, b]
# lst.sort()
#
# print(lst)



# a = "A"
# b = "B"
# c = "C"
# d = " "
#
# lst = [a, b, c, d]
# lst.reverse()
#
# print(lst)

