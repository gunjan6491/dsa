arr=[1,2,2,1,2,1,1,1,1]
num=[]
count=0
for i in range(len(arr)):
    if arr[i] not in num:
        num.append(arr[i])

max_count=0
best_type=None


for j in num:
    count=0
    k=0
    while k <len(arr):
      if arr[k]==j:
         count+=1
         k+=2
      else:
          k+=1
    
    if count>max_count:
        max_count=count
        best_type=j

print(max_count)
