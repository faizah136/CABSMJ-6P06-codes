def count_upper_lower(s):
    ucount = 0
    lcount = 0
    nolettercount = 0
    for ch in s:
        if ch.isupper():
            ucount+= 1
        elif ch.islower():
            lcount+= 1
        else:
            nolettercount += 1
    print(f"Uppercase letters: {ucount}")
    print(f"Lowercase letters: {lcount}")
    print(f"Non alphabetical characters: {nolettercount}")

s = input("Enter a string: ")
count_upper_lower(s)
