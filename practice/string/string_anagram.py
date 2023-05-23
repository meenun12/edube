str1 = 'listen'
str2 = 'silent'

str1 = "".join(chr1 for chr1 in str1 if chr1.isalpha()).lower()
str2 = "".join(chr2 for chr2 in str2 if chr2.isalpha()).lower()

if sorted(str1) == sorted(str2):
    print("string is anagram")
else:
    print("string is not anagram")





