# dictionary

# dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
# phone_numbers = {'boss': 5551234567, 'Suzy': 22657854310}
# empty_dictionary = {}
#
# print(dictionary)
# print(phone_numbers)
# print(empty_dictionary)



# dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
# phone_numbers = {'boss' : 5551234567, 'Suzy' : 22657854310}
# empty_dictionary = {}
#
# # Print the values here.
# dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
# words = ['cat', 'lion', 'horse']
#
# for word in words:
#     if word in dictionary:
#         print(word, "->", dictionary[word])
#     else:
#         print(word, "is not in dictionary")
#



# dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
#
# for key in dictionary.keys():
#     print(key, "->", dictionary[key])
#
# for key in sorted(dictionary.keys()):
#     print(key, "->", dictionary[key])




# dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
#
# dictionary['cat'] = 'minou'
# print(dictionary)
#
# dictionary['swan'] = 'cygne'
# print(dictionary)
#
# dictionary.update({"duck": "canard"})
# print(dictionary)
#
# del dictionary['dog']
# print(dictionary)
#
# dictionary.popitem()
# print(dictionary)


# school_class = {}
#
# while True:
#     name = input("Enter the student's name: ")
#     if name == '':
#         break
#
#     score = int(input("Enter the student's score (0-10): "))
#     if score not in range(0, 11):
#         break
#
#     if name in school_class:
#         school_class[name] += (score,)
#     else:
#         school_class[name] = (score,)
#
# for name in sorted(school_class.keys()):
#     adding = 0
#     counter = 0
#     for score in school_class[name]:
#         adding += score
#         counter += 1
#     print(name, ":", adding / counter)


# line 1: create an empty dictionary for the input data; the student's name is used as a key, while all the associated scores are stored in a tuple (the tuple may be a dictionary value - that's not a problem at all)
# line 3: enter an "infinite" loop (don't worry, it'll break at the right moment)
# line 4: read the student's name here;
# line 5-6: if the name is an empty string (), leave the loop;
# line 8: ask for one of the student's scores (an integer from the range 0-10)
# line 9-10: if the score entered is not within the range from 0 to 10, leave the loop;
# line 12-13: if the student's name is already in the dictionary, lengthen the associated tuple with the new score (note the += operator)
# line 14-15: if this is a new student (unknown to the dictionary), create a new entry - its value is a one-element tuple containing the entered score;
# line 17: iterate through the sorted students' names;
# line 18-19: initialize the data needed to evaluate the average (sum and counter)
# line 20-22: we iterate through the tuple, taking all the subsequent scores and updating the sum, together with the counter;
# line 23: evaluate and print the student's name and average score.




