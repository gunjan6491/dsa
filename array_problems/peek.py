arr=[1, 2,3, 4]

peek=None
for i in range(len(arr)):
    if arr[0]>arr[1]:
        peek=arr[0]
    elif arr[-1]>arr[-2]:
        peek=arr[-1]
    else:
        if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
            peek=arr[i]
print(peek)