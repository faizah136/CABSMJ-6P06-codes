def invoice_sum(*args):
    total = 0
    for num in args:
        total += num
    return total

print("Billing System")
print("Enter all item amounts separated by spaces.")
print("Press ENTER without typing anything if invoice is empty.\n")

user_input = input("Enter invoice amounts: ")

if user_input.strip() == "":
    result = invoice_sum()
else:
    numbers = list(map(int, user_input.split()))
    result = invoice_sum(*numbers)

print("Total Invoice Amount =", result)
