## x = 5   # try with and without assign value
#
# try:
#   print(x)
# except:
#   print("An exception occurred")



# try:
#     value = int(input('Enter a natural number: '))
#     print('The reciprocal of', value, 'is', 1/value)  ## reciprocal number is reverse number of natural numbre
# except:
#     print('I do not know what to do.')


# try:
#     value = int(input('Enter a natural number: '))
#     print('The reciprocal of', value, 'is', 1 / value)
#
# except ValueError:          ##
#     print('I do not know what to do.')
#
# except ZeroDivisionError:
#     print('Division by zero is not allowed in our Universe.')



# try:
#     value = int(input('Enter a natural number: '))
#     print('The reciprocal of', value, 'is', 1/value)
# except ValueError:
#     print('I do not know what to do.')
# except ZeroDivisionError:
#     print('Division by zero is not allowed in our Universe.')
# except:
#     print('Something strange has happened here... Sorry!')





try:
    value = int(input("Enter a value: "))
    print(value/value)
except ValueError:
    print("Bad input...")
except ZeroDivisionError:
    print("Very bad input...")
except:
    print("Booo!")
