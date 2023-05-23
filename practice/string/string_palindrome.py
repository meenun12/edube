str1 = 'Do geese see God?'
str1 = "".join(chr1 for chr1 in str1 if chr1.isalpha()).lower()

if str1 == str1[::-1]:
    print("string is palindrom")
else:
    print("string is not palindrom")





