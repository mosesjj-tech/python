# Print each word on a separate line.

text = input("Enter a sentence: ")
word = ""

for letter in text:
    if letter == " ":
        if word != "":
            print(word)
            word = ""
    else:
        word = word + letter

if word != "":
    print(word)