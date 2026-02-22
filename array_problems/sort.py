arr=[0, 2, 1, 2, 0, 1, 0]
arr1=[]

count0=0
count1=0
count2=0

for i in arr:
    if i==0:
        count0+=1
    elif i==1:
        count1+=1
    else:
        count2+=1

arr= [0]*count0 + [1]*count1 + [2]*count2
print(arr)
            
       
