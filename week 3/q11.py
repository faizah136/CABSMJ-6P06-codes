n = int(input("Enter a number: "))

if n <=1:
    print(n, "is not a prime number.")
else:
    is_Prime = True

    for i in range (2, n//2):
        if n % i == 0:
            is_Prime = False
            print(f"{n} is not prime, first factor:", i)
            break
    if is_Prime:
        print(n, "is a prime number.")
