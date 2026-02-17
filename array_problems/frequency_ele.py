arr=[1,2,3,1,1,2,2,3,3,1,2,3,1,3,1,3]
ele=[]
for i in arr:
    if i in ele:
        continue
    count=0
    for j in arr:
        if j==i:
            count=count+1
        
    print(i,count)
    ele.append(i)