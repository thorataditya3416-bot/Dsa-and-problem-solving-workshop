# for i in range (1,6):
#     if i==3:
#         continue
#     print(i)

# for i in range (5,0,-1):
#     if i==3:
#         continue
#     print(i)


for i,j in zip(range(1,6),range(5,0,-1)):
    if i==3:
        continue
    print(i,j)