arr=[9, 1, 4, 7, 3, 2, 6, 8, 0]

longest=0

for i in arr:
    
    count=1
    current=i

    for j in range(current+1,current+len(arr)):
        if j in arr:
            count+=1
        else:
            break
    if count>longest:
        longest=count

print(longest)


        
