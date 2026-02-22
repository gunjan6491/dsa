arr=[1, 2, 3, 4]

re=[]

for i in range(len(arr)):
    product=1
    for j in range(len(arr)):
        if i==j:
            continue
        else:
            product*=arr[j]
    re.append(product)
print(re)