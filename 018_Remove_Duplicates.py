#Best Solution
a1 = [1,1,1,2,3,4,4,7,9,9,10]
l1 = len(a1)
b1 = {}
for i in range(l1):
    b1[a1[i]] = 0
j = 0
for k in b1:
    a1[j] = k
    j+=1
print(j)

#Optimal Solution
a = [1,1,1,2,3,4,4,7,9,9,10]
l = len(a)
def let(a):
    global l
    if l==1:
        return 1
    i = 0
    j = i+1
    while j<l:
        if a[i] != a[j]:
            i+=1
            a[i], a[j] = a[j], a[i]
        j+=1
    return i+1
ans = let(a)
print(ans)
