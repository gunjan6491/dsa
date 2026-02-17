arr=[1,2,3,4,9,8]
sorted_arr=True
for i in range(len(arr)-1):
    if arr[i]>arr[i+1]:
        sorted_arr=False
    else:
        continue

if sorted_arr:
    print("array is sorted")
else:
    print("array is not sorted")