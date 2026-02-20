arr=[2,7,11,15,4,5]
sum=9
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]+arr[j]==sum:
            print((arr[i],arr[j]))