



word=input("input a word to check if its palindrome:")
palindrome = True
if len(word) % 2 == 0:
    i = 0
    length = len(word)
    half = length / 2
    while i < half:
        if word[i] == word[length-i-1]:
            palindrome=True
        else:
            palindrome=False
        i=i+1
print(palindrome)

