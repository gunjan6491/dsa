 
arr=[1,2,3,4,5]
k=int(input("enter the number of rotations :"))
n=len(arr)
left=arr[0:n-k]
if k>n:
    k=k%n

right=arr[n-k:]

for i in left:
    right.append(i)

print(right)



