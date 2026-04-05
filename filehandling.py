# f = open("myfile.txt", "w")
# print("File name: ", f.name)
# print("File mode: ", f.mode)
# print("readable: ", f.readable())
# print("writable: ", f.writable())
# print("file.closed: ", f.closed)
# f.close()
# print("file.closed: ", f.closed)

#-------------------------------------------

# performing write opration
# f = open("myfile.txt", "w")
# f.write("Kolhapur is a smart city")
# f.close()
# print("File operation is Done")

#-------------------------------------------

# performing write opration
# f = open("myfile.txt", "w")
# f.write("Kolhapur is a smart city")
# f.close()
# print("File operation is Done")

# -------------------------------------------

# inserting list 
# f = open("myfile.txt", "a")
# mylist = ["Aditya ", "Thorat ", "Tejas ", "Kamble"]
# f.writelines(mylist)
# f.close()
# print("Written work has Done ")

# -------------------------------------------

# reading data from a file
# f = open("myfile.txt", "r")
# print(f.read())
# f.close

# -------------------------------------------

# Properties of the object
# with open("myfile.txt", "w") as f:
#     f.write("aditya\n")
#     f.write("Shree\n")
#     f.write("tejas\n")
#     print("File closed :", f.closed)
# print("File closed :", f.closed)

# -------------------------------------------
# with open("myfile.txt", "r") as f:
#     content = f.read()
#     print(content)

# -------------------------------------------

# f1=open("computer.jpg","rb")
# f2=open("adddd.jpg","wb")
# data = f1.read()
# f2.write(data)
# print("Done")

# -------------------------------------------

# import csv
# f = open("Student.csv", "a",newline="")
# a =csv.writer(f)
# # a.writerow(["studentid", "rollno", "name", "mobileno"]) 
# studentid = int(input("Enter student id: "))
# rollno = int(input("Enter roll no: "))
# name = input("Enter name: ")
# mobileno = int(input("Enter mobile no: "))
# a.writerow([studentid, rollno, name, mobileno])
# print("student record has save")

# -------------------------------------------

# {"rollno", "name", "mobileno","p1", "p2", "p3", "total", "percentage","email","result"}
# "rollno","name","mobileno","p1","p2","p3"(you have accept)
# "total","percentage",(calculate)
#"result"(pass/fail)
# if user is pass in all subjects then pass else fail(passing score is 40)
import csv
f = open ("newfile1.csv","a",newline="")
a = csv.writer(f)
a.writerow(["rollno","name","mobileno","p1","p2","p3","total","percentage","email","result"])

rollno = int(input("Enter your roll no:"))
name= input("enter your name:")
mobileno= int(input("Enter your mobile no:"))
p1 = int(input("enter value of p1:"))
p2 = int(input("enter value of p2:"))
p3 = int(input("enter value of p3:"))

email = input("enter email:")
a.writerow(["rollno","name","mobileno","p1","p2","p3","total","percentage","email","result"])
print("student records has saved")