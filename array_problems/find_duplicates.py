arr=[1,1,2,2,3,3,4,5,5,6,7,7,8,8,1] 
s=[] 
count=0 
for i in arr: 
    count=0 
    for j in arr: 
        if i==j: 
            count+=1 
    
    if count>1:
        if i not in s:
         s.append(i)

print(s)