def reverse_string(s):
    left = 0
    right = len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1


text = input("Enter a string: ")

char_list = list(text)

reverse_string(char_list)

print("Reversed array:", char_list)

print("Reversed string:", ''.join(char_list))
