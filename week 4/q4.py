def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

n = int(input("Enter a number:"))
if n < 0:
    print("Invalid input.")
else:
    result = factorial(n)
    print("Factorial:", result)

    
