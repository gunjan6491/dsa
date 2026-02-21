arr=[0, 1, 0, 3, 12]
count=0
zero=[]
for i in arr:
    if i==0:
        count+=1
        continue
    zero.append(i)

for j in range(count):
    zero.append(0)

print(zero)