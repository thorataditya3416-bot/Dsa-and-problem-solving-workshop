# for i in range(5,0,-1): #i=5
#     print(i)


# for i in range(10,0,-2): #i=10
#     print(i)

# # reverse of a string
# name= "Mumbai"
# new_name= ""
# for i in name: #i=6:r
#     new_name = i + new_name
# print(name)
# print(new_name)

name ="Mumbai"
newname = ""
n = len(name) #n=6
for i in range(n-1, -1, -1): #i=5
    newname = newname + name[i]
print(name)
print(newname)