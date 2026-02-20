n = input("Enter a number: ")
sum = 0
for ch in n:
     if ch.isdigit():
         sum = sum + int(ch)
print(f"sum = {sum}")
