list1 = [1,1,2,0,-5,3,4,4,-2]
list2 = [0]*((max(list1)+1) - min(list1))

for item in list1:
    list2[item]+=1

res = 0
for item in list2:
    if item!=0:
        res+=1

print (res)
print(list2)