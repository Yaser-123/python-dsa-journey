#asscending
a = [1, 7, 8, 4, 5, 6, 9, 2]
def selection(arr):
    n = len(arr)
    for i in range(0,n):
        min = i
        for j in range(i+1, n):
            if arr[j]<arr[min]:
                min = j
        arr[i],arr[min] = arr[min], arr[i]
    return arr
ans = selection(a)
print(ans)

#decending
b = [1, 7, 8, 4, 5, 6, 9, 2]
def selection2(arr):
    n = len(arr)
    for i in range(0,n):
        min = i
        for j in range(i+1, n):
            if arr[j]>arr[min]:
                min = j
        arr[i],arr[min] = arr[min], arr[i]
    return arr
ans2 = selection2(a)
print(ans2)