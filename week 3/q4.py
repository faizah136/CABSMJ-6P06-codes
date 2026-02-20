a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

while b!=0:
    carry = a&b
    a = a^b
    b = carry << 1
    
print("sum = ", a)
