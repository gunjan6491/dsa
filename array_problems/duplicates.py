arr=[1,1,2,2,4,5,6,7,8,9,9]
arr1=[]
for i in arr:
    if i not in arr1:
        arr1.append(i)

print(arr1)
