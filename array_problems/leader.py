arr=[16, 17, 4, 3, 5, 2]
leader=[arr[-1]]

max=arr[-1]
for i in arr[::-1]:
    print(i)
    if i>max:
        if i not in leader:
          leader.append(i)
        max=i
    else:
       continue

print(leader)




          