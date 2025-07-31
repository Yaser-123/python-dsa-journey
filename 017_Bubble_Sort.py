a = [1, 7, 8, 4, 5, 6, 9, 2]

def bubble(arr):
    n = len(arr)
    for i in range(n-2, -1, -1):
        for j in range(0, i+1):
            if arr[j+1] < arr[j]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
bubble(a)
print(a)