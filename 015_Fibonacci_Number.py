# def fibo(n,i=0):
#     if i >= n:
#         return 0
#     return i+fibo(n,i+1)
# ans = fibo(5)
# print(ans)

def fibo2(n):
    if n==0 or n==1:
        return n
    return fibo2(n-1) + fibo2(n-2)
ans2 = fibo2(6)
print(ans2)