import math
def fact(num):
    factorial = 1
    while num > 1:
        factorial *= num
        num -= 1
    return factorial
n= float(input("enter the number:"))
print(f"factorical of {n} is {fact(n)}")

num = float(input("enter the numner:"))
output = math.sqrt(num)
print(f"square root : {output}")

log = math.log(num)
print("Natural logarithm:", log)

sin = math.sin(num)
print("Sine:", sin)
