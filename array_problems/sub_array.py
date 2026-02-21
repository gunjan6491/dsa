arr=[1, 2, 3, 7, 5]
target=12
sub=[]

for i in range(len(arr)):
     sum=0
     for j in range(i,len(arr)):
          sum=sum+arr[j]
          if sum==target:
               sub.append((arr[i:j+1]))
          else:
               continue
     
print(sub)