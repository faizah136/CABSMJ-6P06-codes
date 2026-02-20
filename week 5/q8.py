def reverse_each_word(s):
    result = ""
    word = ""

    for ch in s:
        if ch != ' ':
            word += ch
        else:
            result += word[::-1]
            result += ch
            word = ""

    result += word[::-1]
    return result

text = input("Enter a sentence: ")

output = reverse_each_word(text)

print("Result:", output)
