#Optimum Method
n = [5, 3, 2, 2, 1, 5, 5, 7, 5, 10]
m = [10, 111, 1, 9, 5, 67, 2]

count = n
frequency = {}
list1 = {}
length = len(n)
for num in range(0,length):
    frequency[count[num]] = frequency.get(count[num], 0)+1
for num2 in m:
    if num2 in frequency:
        list1[num2] = frequency[num2]
    else:
        list1[num2] = 0
print("By dictionary Method: ", list1)

# ------------------------------------------
# Hashing Method
#Constrains:-
# 1) 1<n[i]<=10
# 2) n2 can have 10^8 elements
# 3) m2 can have 10^8 elements

n2 = [5, 3, 2, 2, 1, 5, 5, 7, 5, 10]
m2 = [10, 111, 1, 9, 5, 67, 2]

n2is = n2

frequency2 = {}

hash_list = [0]*11

length2 = len(n2)

answer2 = []

for num in n2:
    hash_list[num] += 1

for num in m2:
    if 0<num<11:
        answer2.append(hash_list[num])
    else:
        answer2.append(0)

print("By hash Method: ",answer2)