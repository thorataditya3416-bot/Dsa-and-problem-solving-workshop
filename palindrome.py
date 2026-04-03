# question : write a program to check if a given string is palindrome or not
# logic : use loops to compare the first and last character of the string, then second and second last character and so on
 #samle input : " racear"

name = "racear"
print(name)
print(name[::-1])
if name == name[::-1]:
    print("palindrome")
else:
    print("not palindrome")