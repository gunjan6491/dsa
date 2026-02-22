arr=[2, 2, 1, 2, 3, 2, 2]
n=len(arr)
maj=n/2
temp=None
for i in arr:
    count=0
    for j in arr:
        if i==j:
            count+=1

    if count>maj:
       temp=i
    else:
        continue

print(temp)