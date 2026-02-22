arr=[7, 1, 5, 3, 6, 4]
max=0

for i in range(len(arr)):
    diff=0
    for j in range(i+1,len(arr)):

        if arr[j]>arr[i]:
            diff=arr[j]-arr[i]
            
            if diff>max:
                max=diff

print(max)