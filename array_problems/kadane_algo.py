arr=[-2, 1, -3, 4, -1, 2, 1, -5, 4]
max=arr[0]
sub=[]
for i in range(len(arr)):
    sum=0
    for j in range(i,len(arr)):
        sum+=arr[j]
        if sum>max:
            max=sum
            sub=arr[i:j+1]
print(sub)