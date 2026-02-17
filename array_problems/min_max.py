arr=[23,56,18,90,54,65,32]
min_ele=arr[0]
max_ele=arr[0]
for i in arr:
    if i>max:
        max=i
    elif i<min:
        min=i
    else :
        continue
print(max_ele)
print(min_ele)