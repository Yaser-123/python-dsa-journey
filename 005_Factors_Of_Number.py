#Best Solution
n1 = 36
num1 = n1
result1 = []
for i in range(1,int(num1/2+1)):
    if num1%i == 0:
        result1.append(i)
result1.append(n1)
print("The factore of ",n1," by using best method is: ",result1)

#Optimized Solution
from math import sqrt
n2 = 36
num2 = n2
result2 = []
for i in range(1, int(sqrt(n2)+1)):
    if num2 % i == 0:
        result2.append(i)
        if num2 // i != i:
            result2.append(int(num2//i))
result2.sort()
print("The factore of ",n2," by using optimized method is: ",result2)