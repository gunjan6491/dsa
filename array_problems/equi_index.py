arr=[1, 3, 5, 2, 2]


for  i in range(len(arr)):
    
    left=arr[:i]
    right=arr[i+1:]

    if sum(left)==sum(right):
        print(i)

        