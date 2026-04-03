n=int(input("enter the size of elements in list: "))
arr=[]
for i in range(n):
    val = int(input("enter the element: "))
    arr.append(val)
sum =0
for i in range(n):
    if i+1 in range(n):
        sum += abs(arr[i]-arr[i+1])
print(sum)