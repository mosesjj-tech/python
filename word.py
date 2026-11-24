print("PROGRAMMING SNACKS - PYTHON")
print("11. Display words separately")

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