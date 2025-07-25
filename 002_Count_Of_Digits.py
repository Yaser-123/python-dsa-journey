#Best Solution
n1 = 5873
num = n1
count1 = 0
while num>0:
    count1+=1
    num//=10
print("The count of 5873 using general method: ",count1)

#Optimized Solution
n2 = 5873
from math import *
def number_count(num2):
    return int(log10(num2)+1)
count2 = number_count(n2)
print("The count of 5873 using math library",count2)
