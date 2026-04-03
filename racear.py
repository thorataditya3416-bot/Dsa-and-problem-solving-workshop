# name ="racear"
#  #012345
# for i in name: #i=6:r
#     print(i)

#Write a program to remove the duplicate characters
name = "racear"
new_name = ""
for i in name: #i=6:r
    if i not in new_name:
        new_name = new_name + i
print(name)
print(new_name)