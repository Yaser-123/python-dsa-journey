# Head Recursion
count = 0

def greet1():
    global count
    if count == 4:
        return
    print("Hello World")
    count += 1
    greet1()

greet1()

# Tail Recursion
count2 = 0

def greet2():
    global count2
    if count2 == 4:
        return
    count2 += 1
    greet2()
    print("Hello World")

greet2()


