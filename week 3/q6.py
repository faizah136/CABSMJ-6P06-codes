a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
print(f"Before swapping:\na = {a}\tb = {b}")
a = a ^ b
b = a ^ b
a = a ^ b
print(f"After swapping:\na = {a}\tb = {b}")
