# Write a program ro move*
# input = aditya*is*a*good*programmer
# ouput = ****adityaisagoodprogrammer
# s = input("enter the string: ")
# s1 = s.split("*")
# s2 = "".join(s1)
# print(s2)
# print("*"*s.count("*")+s2)


# name = 'aditya*is*a*good*programmer'
# newname =''
# val = ''
# for i in name:
#     if i == '*':
#         newname += i
#     else:
#         val+= i
# print(str(newname)+str(val))

# a=50
# b=30
# c=20
# d=10
# print((a+b)*(c/d))
# print((a-b)*(c/d))
# print(a+(b*c)/d)

# x=['A','B','C']
# y=['A','B','C']
# z=[1,2,3,4]
# print(x==y)
# print(x==z)
# print(x != z)
# print(id(x))
# print(id(y))
# print(id(z))

# #logic : check if the character counts in both the strings are same 
# # input = "listen" and "silent"
# # output = "anagram"
# a = "listen"
# b = "silent"
# if sorted(a) == sorted(b): 
#     print("Anagram")

# # Logic Use loops to count spaces and words
# # input = "This is a sentence"
# # output = 4
# a = "This is a sentence"
# count = 1
# for i in a:
#     if i == " ":
#         count += 1
# print(count)

# Logic use two passes, one from left to right and one from right to left to calculate products
# input = [1,2,3,4]
# output = [24,12,8,6]
# A = [1,2,3,4]
# B = [1,1,1,1]
# for i in range(len(A)):
#     for j in range(len(A)):
#         if i != j:
#             B[i] *= A[j]
# print(B)