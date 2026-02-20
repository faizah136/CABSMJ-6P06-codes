def remove_indent(text):
    lines = text.split('\n') 
    cleaned= []

    for line in lines:
        cleaned.append(line.lstrip()) 

    return '\n'.join(cleaned)


print("Enter multi-line text (press enter twice to finish):")

lines = []
while True:
    line = input()
    if line == "": 
        break
    lines.append(line)  

multi_text = "\n".join(lines)

result = remove_indent(multi_text)

print("\nCleaned Text:\n")
print(result)
