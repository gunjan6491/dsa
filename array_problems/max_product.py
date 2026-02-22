arr=[1, 4, 3, 6, 7, 0]
max=0

for i in range(len(arr)):
    product=1
    for j in range(len(arr)):
        if i==j:
            continue
        else:
          product=arr[i]*arr[j]
          if product>max:
            max=product

print(max)