n = int(input("Enter a number: "))

if n < 0:
    print(f"{n} is not a Fibonacci number")
else:
    a, b = 0, 1

    while b < n:
        a, b = b, a + b

    if n == 0 or b == n:
        print(f"{n} is a Fibonacci number")
    else:
        print(f"{n} is not a Fibonacci number")
