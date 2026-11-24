#Count vowels and consonants.

text = input("Enter a sentence: ").lower()

vowels = 0
consonants = 0

for letter in text:
    if letter >= "a" and letter <= "z":
        if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
            vowels = vowels + 1
        else:
            consonants = consonants + 1

print("Vowels:", vowels)
print("Consonants:", consonants)