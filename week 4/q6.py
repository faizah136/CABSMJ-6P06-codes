def is_perfect_number(n):
    if n <= 1:
        return False

    divisor_sum = 0
    for i in range(1, n):
        if n % i == 0:
            divisor_sum += i

    return divisor_sum == n

num=int(input("Enter a number: "))

if is_perfect_number(num):
    print(num, "is a Perfect Number")
else:
    print(num, "is not a Perfect Number")
