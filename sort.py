#sort dictionary by key or value
# input : ("c":1,"B":2,"A":3)
# output : (Asscending by value ("A":1,"B":2,"C":3)
# output : (Descending by value ("C":1,"B":2,"A":3))
#sort dictionary by key or value
# ip= {"A":1,"B":2,"C":3}
# #op ={c,b,a}
# desc = dict(sorted(ip.items(),reverse=True))
# asc = dict(sorted(ip.items()))
# print(asc)
# print(desc)

#========================================================================================

#remove all element from dict
# ip = {"A":1,"B":2,"C":3}
# a = ip.clear()
# print(ip)

#========================================================================================
 
# Queue

# import sys
# class Queue:
#     def __init__(self, queuesize):
#         self.queuelist =[]
#         self.Queuesize = queuesize

#     def isFull(self): 
#         if len(self.queuelist) == self.Queuesize:
#             return True
#         else:
#             return False
#                                                 #stack implementation with size limit
#     def enqueue(self, value):
#         if self.isFull():
#             print("queue is full")
#         else:
#             self.queuelist.append(value)
        
        
#     def displayqueue(self):
#         print("----------------------")
#         print(self.queuelist)
#         print('--------------------')

#     def isempty(self):
#         if self.queuelist == []:
#             return True
#         else:
#             return False
        
#     def dequeue(self):
#         if self.isempty():
#             return "queue is empty: "
#         else:
#             return self.queuelist.pop()
        
#     def deletequeue(self):
#         self.queuelist = None
#         return "queue is deleted" 
    
#     def peek(self):
#         if self.isempty():
#             return "queue is empty"
#         else:
#             return self.queuelist[0]
        
# size = int(input("Enter the size of queue :"))            
# queueobj = Queue(size)                                            

# while True:

#     print("1.enqueue element in queue :")
#     print("2.display element in queue :")
#     print("3.check queue isempty :")
#     print("4.dequeue operation :")
#     print("5.delete operation :")
#     print("6.peek operation :")
#     print("7.Exit")

#     choice = int(input("Enter your choice :"))
#     if choice == 1:
#         val = int(input("Enter the value for queue :"))
#         queueobj.enqueue(val)
#     elif choice == 2:
#         queueobj.displayqueue()
#     elif choice == 3:
#         print(queueobj.isempty())
#     elif choice == 4:
#         print(queueobj.dequeue())
#     elif choice == 5:
#         print(queueobj.deletequeue())
#     elif choice == 6:
#         print(queueobj.peek())
#     else:
#         sys.exit()

#==========================================================================================

# O(1) = constant time
# array = [1,2,3,4,5]
# array[0] // it takes constant time to access any element

# O(N) = linear time
# array = [1,2,3,4,5]
# for element in array:
# print(element)
# //linear time since it is visiting every element of array
#// logarithmic time since it is visitng only some elements

#==========================================================================================

# O[N] = quadratic time
# array = [1,2,3,4,5]
# for i in range(len(array)):
#     for j in range(len(array)):
#         print(i,j)

#==========================================================================================
# O(N²) = quadratic time
# array = [1,2,3,4,5]
# for x in array :
# for y in array:
# print(x,y)

#==========================================================================================
# O(2ⁿ) exponential time
#     def Fibonacci(n):
#     if n <= 1:
#     return n
#     return Fibonacci(n-1) + Fibonacci(n-2)

#==========================================================================================


#                                         Time complexity     space complexity
# create stack                                O(1)                O(1)
# push                                     O(1)/ 0(N^2)               O(1)
# pop                                         O(1)                O(1)
# peek                                        O(1)                O(1)
# isFull                                      O(1)                O(1)
# isEmpty                                     O(1)                O(1)

#==========================================================================================

#                                         Time complexity     space complexity
# create stack                                O(1)                O(1)
# push                                     O(1)/ 0(N^2)           O(1)
# pop                                         O(1)                O(1)
# peek                                        O(1)                O(1)
# isEmpty                                     O(1)                O(1)
# deleteStack                                 O(1)                O(1)    

#==========================================================================================

# In python

# stack using list:
# -easy to implement
# -speed problem when it grows

# stack using linked list:
# -fast performance
# -implementation is not easy

#==========================================================================================

# create queue	O(1)	O(1)
# enqueue	O(n)	O(1)
# dequeue	O(n)	O(1)
# peek	O(1)	O(1)
# delete entire queue	O(1)	O(1)
# isempty	O(1)	O(1)
#=========================================================================================

# Queue using list
# -easy to implement
# -speed problem when it grows

# Queue using linked list
# -fast performance
# -implementation is not easy

#=========================================================================================

# def findlargestnumber():
#     firstvalue = array[0]# first value = 5
#     for i in range(1,len(array)): # i =2 O[i]
#         if array[i] > firstvalue: # 5>4 ==> 
#             firstvalue = array[i]
#     return firstvalue

# array = [1,4,5,6,7,1,9,3,4,5,6]
# print(findlargestnumber())

#=========================================================================================

# write an algorithm to help the agency find number of special characters and whtespaces into given message
# input : The input consists of a string message. representing the message that nedd to be decoded by the agency
# input s: adityathorat3416@gmail.com
# ouput : 4
# def countSpecialCharacters(string):
#     special_characters = "!@#$%^&*()_+-=~`|\\:;\"'<>,.?/"
#     count = 0
#     for char in string:
#         if char in special_characters:
#             count += 1
#     return count

# string = "Hello, World! How are you?"
# print(countSpecialCharacters(string))
# ip = "jdbs54@#jvd$dh!"
# count = 0
# for i in ip:
#     if not i.isalnum():
#         count+=1
# print(count)

#=========================================================================================
# write a algorith to help apparel find the number of plots that it can select for its outlets
# input : The first line of the input consists of an integer numbofmots, representing the number of plots shortlisted by the compan for outlets(N)
# import math
# n = int(input("Enter number of plots: "))
# areas = list(map(int, input("Enter areas: ").split()))

# count = 0

# # Check each area
# for area in areas:
#     root = int(math.sqrt(area))
    
#     if root * root == area:   # perfect square check
#         count += 1

# # Output
# print("Number of square plots:", count)

#=========================================================================================

# size = int(input("Enter the number of elements: "))
# a = [] 


# for i in range(size):
#     element = int(input(f"Enter element {i+1}: "))
#     a.append(element)

# print("The elements are:")
# for i in a:
#     print(i)

#=========================================================================================
# import math

# size = int(input("Enter the number of elements: "))
# a = []

# for i in range(size):
#     element = int(input(f"Enter element {i+1}: "))
#     a.append(element)

# print("The elements are:", a)


# sqrt_list = []

# for i in a:
#     sqrt_list.append(math.sqrt(i))
# print("Length of square root is:", len(sqrt_list))

#=========================================================================================

# import math

# size = int(input("Enter the number of elements: "))
# a = []

# for i in range(size):
#     element = int(input(f"Enter element {i+1}: "))
#     a.append(element)

# count = 0
# for i in a:
#     if math.sqrt(i).is_integer():
#         count += 1

# print("Perfect square roots count:", count)

#=========================================================================================

# Linear search
# def linearsearch(array, target): #[1,2,3,4,5,6,7,8] #===> O(n)
#     for i in range(len(array)):#i=2 #=======> O(1)
#         if array[i] == target:# == 4 #=======> O()
#             return i #=======================> O(1)
#     return -1 #===============================>O(1)

# array = [1,2,3,4,5,6,7,8]
# target = 4 # int
# result = linearsearch(array,target)
# if result == -1:
#     print("Element not found")
# else:
#     print("Element found at index",result)

#=========================================================================================

# def binarySearch(array,target): 
#     start = 0
#     end = len(array)-1
#     while start <= end:
#         mid = (start+end) //2
#         if array[mid] == target:
#             return mid
#         elif array[mid]< target:
#             start = mid+1
#         else:
#             end = mid -1
#     return -1 
#                                      #o(1)
    
# sorted_array =[1,2,3,4,5,6,7,8,9]
# target = 44
# result=binarySearch(sorted_array, target)
# if result == -1:
#     print("not found")
# else:
#     print('Element found at index no=',result)

#=========================================================================================
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
# class LinkedList:
#     def __init__(self):
#         self.head = None
# linkedlist = LinkedList()
# linkedlist.head = Node(5)  # first node
# second          = Node(10)
# third           = Node(15)
# fourth          = Node(20)
# #linking part
# linkedlist.head.next = second
# second.next = third
# third.next=fourth
# #display linkedlist
# while linkedlist.head != None:
#     print("|",linkedlist.head.data,"|",linkedlist.head.next,"->", end=" ")
#     linkedlist.head =linkedlist.head.next


#=========================================================================================  
# import sys

# class node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class  LinkedList:
#     def __init__(self):
#         self.head = None

#     def addnode(self, value):
#         new_node = node(value)
#         if self.head is None:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             self.tail = new_node
    
#     def addNodeinBeginning(self, value):
#         new_node = node(value)
#         if self.head is None:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             new_node.next = self.head
#             self.head = new_node

#     def addNodeinBetween(self, value, left_value, right_value):
#         if self.head is None:
#             print("List is empty. Cannot insert between nodes.")
#             return

#         current = self.head
#         while current is not None:
#             if current.data == left_value and current.next is not None and current.next.data == right_value:
#                 new_node = node(value)
#                 new_node.next = current.next
#                 current.next = new_node
#                 if current is self.tail:
#                     self.tail = new_node
#                 return
#             current = current.next

#         print(f"No adjacent nodes found with values {left_value} and {right_value}. Cannot insert {value} between them.")

#     def addNodeatEnd(self, value):
#         new_node = node(value)
#         if self.head is None:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             self.tail = new_node

#     def display(self):
#         current = self.head
#         while current is not None:
#             print(current.data, end=" -> ")
#             current = current.next
#         print("None")

#     def exit(self):
#         sys.exit()

# if __name__ == "__main__":
#     obj = LinkedList()

#     while True:
#         print("\n1. Add Node in Linked List :")
#         print("2. Add node in Beginning :")
#         print("3. Add node Between  :")
#         print("4. Add node at End :")
#         print("5. Display Linked List :")
#         print("6. Exit")
        
#         choice = int(input("Enter your choice : "))
        
#         if choice == 1:
#             val = int(input("Enter value for node : "))
#             obj.addnode(val)
#         elif choice == 2:
#             val = int(input("Enter value for node : "))
#             obj.addNodeinBeginning(val)
#         elif choice == 3:
#             val = int(input("Enter value for node : "))
#             left_val = int(input("Enter the value of the node before the new node: "))
#             right_val = int(input("Enter the value of the node after the new node: "))
#             obj.addNodeinBetween(val, left_val, right_val)
#             print("Element Added Successfully")
#         elif choice == 4:
#             val = int(input("Enter value for node : "))
#             obj.addNodeatEnd(val)
#         elif choice == 5:
#             obj.display()
#         elif choice == 6:
#             obj.exit()
