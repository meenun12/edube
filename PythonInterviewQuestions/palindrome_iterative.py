string = "alla?1"

str1 = "".join(char for char in string if char.isalpha()).lower()

if str1 == str1[::-1]:
    print("string is palindrome")
else:
    print("string is not palindrome")



