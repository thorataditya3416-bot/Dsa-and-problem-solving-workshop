# mytuple = ("ADitya", "Reddy", "Kumar","Tejas","Sagar","Sanjog","Uttam", 23,9,16,15,"Shekhar")
# print(mytuple)
# print(type(mytuple))
# mytuple[2] = "Pratik"
# print(mytuple) ouput is not display becoz  not changes a values in any tuple

# init_tuple = ()
# print(init_tuple.__len__()) #output = 0

# init_tuple_a = 'a', 'b'
# init_tuple_b = ('a', 'b')
# print(init_tuple_a == init_tuple_b) #output = True

# init_tuple_a = 'a', 'b'
# init_tuple_b = ('a', 'b')
# print(id(init_tuple_a)) #output = 140432878203264
# print(id(init_tuple_b)) #output = 140432878203264
# print(init_tuple_a is init_tuple_b) #output = True

# init_tuple_a = '1', '2'
# init_tuple_b = ('3','4')
# print(init_tuple_a + init_tuple_b)

# init_tuple = ('python')*3
# print(type(init_tuple))

# init_tuple = (1,)*3
# init_tuple[0] = 2
# print(init_tuple)  output is not display becoz  'init object does not support item assignment'


# init_tuple = ((1, 2),)*7
# print(len(init_tuple[3:8])) #output = 4

# A =[4,0,2,5,0,1]
# for i in A:
#     if i == 0:
#         A.remove(i)
#         A.append(i)
# print(A) #output = [4, 2, 5, 1, 0, 0]

# #input [1,2,2,3,4,4,5] remove duplicates and sort the list
# A= [1,2,2,3,4,4,5]
# newlist=[]
# for i in A:
#     if i not in newlist:
#         newlist.append(i)
# print(newlist) #output = [1, 2, 3, 4, 5]


# Sample Input: [1,2,3],[2,3,4],[3,4,5]
# output = [3]
# A = [1,2,3]
# B = [2,3,4]
# C = [3,4,5]
# for i in A:
#     if i in B and i in C:
#         print(i) #output = 3


