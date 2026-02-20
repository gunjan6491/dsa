arr=[2,3,4,5,6,7,8]
s=int(input("enter the number:"))
m=[]

for i in range(len(arr)):
    if arr[i]==s:
        continue
    else:
        m.append(arr[i])

print(m)