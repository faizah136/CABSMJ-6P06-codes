import string

def word_frequency(sentence):
    freq = {}

    sentence = sentence.lower()

    for ch in string.punctuation:
        sentence = sentence.replace(ch, "")

    words = sentence.split()
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    return freq

text = input("Enter a sentence: ")

result = word_frequency(text)

print(result)
