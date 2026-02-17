arr=[100,2999,31,46,56,63,12032]
max_ele=arr[0]
sec_max=arr[-1]
for i in arr :
    if i>max_ele:
        sec_max=max_ele
        max_ele=i
    
    elif i<max_ele and i>sec_max:
        sec_max=i
    
    else :
        continue
print(sec_max)        