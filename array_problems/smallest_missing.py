arr=[7, 8, 9, 11, 12]
n=len(arr)
temp=None
for i in range(0,n+1):
    if i==0 or i<0:
        continue
    else:
        if i not in arr:
         temp=i
         break
print(temp)