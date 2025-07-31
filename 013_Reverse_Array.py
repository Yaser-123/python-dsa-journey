num = [5, 7, 3, 2, 6, 1, 5, 9]
def reverse_array(arr, start, end):
    if start == end or start > end:
        return
    arr[start], arr[end] = arr[end], arr[start]
    reverse_array(arr, start+1, end-1)
    return arr
ans= reverse_array(num, 0, 7)
print(ans)