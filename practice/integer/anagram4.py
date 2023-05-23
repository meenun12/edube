str1 = "silent"
str2 = "listen"

str1 = "".join(char for char in str1 if char.isalpha())
str2 = "".join(char for char in str2 if char.isalpha())

if sorted(str1) == sorted(str2):
    print("string is anagram")
else:
    print("string is not anagram")

    