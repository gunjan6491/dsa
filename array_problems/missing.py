arr=[1,2,4,6,7,8,9]
n=arr[-1]
miss=[]
for i in range(1,n+1):
    if i not in arr:
        miss.append(i)

print(miss)
    
