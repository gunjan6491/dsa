arr=[1,2,3,4,5,6,7,8,9]
k=int(input("enter the value of k :"))
n=len(arr)

if k>n:
    k=k%n

left=arr[0:k]
right=arr[k:]
rotate=right+left
print(rotate)