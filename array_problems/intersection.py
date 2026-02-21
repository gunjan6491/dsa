arr=[1,2,2,3,4,5]
arr1=[3,7,8,9,2,2,5]
inter=[]

for i in arr:
    for j in arr1:
        if i==j:
            if i not in inter:
               inter.append(i)

print(inter)        