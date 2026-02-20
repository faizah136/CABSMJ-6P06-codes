def string_to_char_list(s):
    char_list = list(s) 
    return char_list


text = input("Enter a string: ")

result = string_to_char_list(text)

print("Character List:", result)
