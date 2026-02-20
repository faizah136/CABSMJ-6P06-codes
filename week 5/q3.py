def text_filter(s):
    temp = ""
    result = ""
    for i in range(len(s)):
        if s[i].isalpha() or i%2== 0:
            temp += s[i]
    for i in range(len(temp)):
        if i % 2 != 0:
            result += temp[i]
    return result

text = input("Enter a string: ")

filtered_text = text_filter(text)

print("Filtered string:", filtered_text)
