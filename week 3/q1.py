n = int(input("Enter the number of prices : "))
sum = 0
product = 1
for i in range (0,n):
    x = int(input(f"Enter price {i+1}: "))
    sum = sum + x
    product = product * x
    
print("Sum = ", sum)
print("Product = ", product)
print("Average = ", sum/n)
