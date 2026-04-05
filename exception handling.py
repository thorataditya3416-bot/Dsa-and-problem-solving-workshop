# n1 = int(input("Enter first value :"))
# n2 = int(input("Enter second value :"))
# try:
#     print(n1/n2)
# except:
#     print("Can't devide by zero !")
# print("To be continue")

#___________________________________________________________________

# try:
#     n1 = int(input("Enter first value :"))
#     n2 = int(input("Enter second value :"))
#     print(n1/n2)
# except ZeroDivisionError:
#     print("Can't devide by zero !")
# except ValueError:
#     print("Enter only integer value")
# print("To be continue")

#__________________________________________________________________


# try: 
#     a = int(input("Enter 1st value :"))
#     b = int(input("Enter 2nd value :"))
#     print(a/b)
# except(ValueError, ZeroDivisionError) as message:
#     print(message)

#__________________________________________________________________

# try: 
#     a = int(input("Enter 1st  integer value :"))
#     b = int(input("Enter 2nd  integer value :"))
#     print(a/b)
# except(ValueError, ZeroDivisionError) as message:
#     print("Enter correct number: ",message)
# except:
#     print("This is default part of except block")

#_________________________________________________________________

# try: 
#     a = int(input("Enter 1st  integer value :"))
#     b = int(input("Enter 2nd  integer value :"))
#     print(a/b)
# except(ValueError, ZeroDivisionError) as message:
#     print("Enter correct number: ",message)
# else:
#     print("Everything is ok")

#_______________________________________________________________

# try: 
#     a = int(input("Enter 1st  integer value :"))
#     b = int(input("Enter 2nd  integer value :"))
#     print(a/b)
# except(ValueError, ZeroDivisionError) as message:
#     print("Enter correct number: ",message)
# finally:
#     print(" I will Always Executed")

#_______________________________________________________________

# try: 
#     a = int(input("Enter 1st  integer value :"))
#     b = int(input("Enter 2nd  integer value :"))
#     try:
#         print(a/b)
#     except ZeroDivisionError as msg:
#         print(msg)
# except ValueError as msg:
#     print(msg)

#______________________________________________________________

# try: 
#     a = int(input("Enter 1st  integer value :"))
#     b = int(input("Enter 2nd  integer value :"))
#     print(a/b)
# except(ZeroDivisionError, ValueError) as message:
#     print(message)
# else:
#     print(" There are no eerror in try block")
# finally:
#     print("I am finally block i always executed ")

#______________________________________________________________
# logic : The input consist of an intiger data representing the data to bi transmitted 
# output : print an integer representing the security key for the given data if no data is repeated it should display
# input : 578378923
# output : 3
# mylist = [5,7,8,3,7,8,9,2,3]
# newlist = []
# for i in range(len(mylist)):
#     count = 0
#     key = mylist[i]

#     j=i+1
#     while j<len(mylist):
#         if key == mylist[j]:
#             newlist.append(key)
#         j = j+1
# print(len(newlist))

#______________________________________________________________

# find the second largest number in a list
# list = [7,3,9,2,8]
# list.sort()
# print(list)
# print(list[-2])

#______________________________________________________________

# i = 1
# while i<=10:
#     print(i)
#     i = i+1

#______________________________________________________________ 

# username = "" #str
# password = "" #str
# while username != "aditya" or password != "aditya":
#     username = input("Enter username: ")
#     password = input("Enter password: ")


#____________________________________________________________

# count a vowels in string
# name = 'programming'
# vowels = ['a','e','i','o','u']
# cons = 0
# vowel = 0
# for i in name: 
#     if i in vowels:
#         vowel += 1
#     else:
#         cons += 1
# print("consonants: ",cons)
# print("vowels: ",vowel)

#____________________________________________________________

# logic : USe list comprehensions or a loop to filter out of the element
# input : [1,2,2,3,4,2] and Element 2
# output : [1,3,4]
# list = [1,2,2,3,4,2]
# element = 2
# newlist = [i for i in list if i != element]
# print(newlist)

#____________________________________________________________

# loigic : use a loop to iterate through the list and accoumulate the product 
# input : [2,3,4,5]
# output : 120
# list = [2,3,4,5]
# product = 1
# for i in list:
#     product = product*i
# print(product)
