#Tail Recursion
def display(n):
    if n==0:
        return
    display(n-1)
    print(n)
display(4)

#Head Recursion
def display2(i,n):
    if i>4:
        return
    print(i)
    display2(i+1,n-1)
display2(1,4)

# N to 1 in tail Recursion
def display3(i,n):
    if i>4:
        return
    display3(i+1,n-1)
    print(i)
display3(1,4)