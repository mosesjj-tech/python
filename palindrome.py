word = input("Enter a word: ").lower()

palindrome = True

for i in range(len(word) // 2):
    if word[i] != word[len(word) - 1 - i]:
        palindrome = False
        break

if palindrome:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")