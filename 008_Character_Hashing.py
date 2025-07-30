s = 'azyxyyzaaaa'
q=['d','a','y','x']

hash_list = [0]*26
# print(len(hash_list))
for c in s:
    val = ord(c)
    index = val-97
    hash_list[index]+=1

for z in q:
    val2 = ord(z)
    index2 = val2-97
    print(hash_list[index2])