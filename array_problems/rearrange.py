arr=[1,2,3,9,8,7,5,0]
re=[]
temp=None
for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i]<arr[j]:
            temp=arr[j]
            arr[j]=arr[i]
            arr[i]=temp
        else:
            continue

for i in range(len(arr)):
    if i%2==0:
        temp=max(arr)
        re.append(temp)
        arr.remove(temp)
    else:
        temp=min(arr)
        re.append(temp)
        arr.remove(temp)
print(re)
