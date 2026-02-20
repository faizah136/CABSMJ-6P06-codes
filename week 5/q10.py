text = input("Enter a text: ")

vowels = "aeiouAEIOU"
vowel_list = []
consonant_list = []

for ch in text:
    if ch.isalpha():    
        if ch in vowels:
            vowel_list.append(ch)
        else:
            consonant_list.append(ch)

# Display results
print("\nVowels:", vowel_list)
print("Number of vowels:", len(vowel_list))

print("\nConsonants:", consonant_list)
print("Number of consonants:", len(consonant_list))
