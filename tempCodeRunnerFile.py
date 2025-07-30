def display(n):
    if n==0:
        return
    display(n-1)
    print(n)
display(4)