#Best Solution
nums1 = [5,6,7,7,1,9,111,1,1,5,1,1]
frequency = {}
for i in range(0,len(nums1)):
    if nums1[i] in frequency:
        frequency[nums1[i]] += 1
    else:
        frequency[nums1[i]] = 1
print(frequency)

#Optimized Solution
nums2 = [5,6,7,7,1,9,111,1,1,5,1,1]
hash_map = dict()
for i in range(0,len(nums1)):
    hash_map[nums2[i]] = hash_map.get(nums2[i],0)+1
print(hash_map)