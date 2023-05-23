string = "Do geese see God?"
string = "".join(char for char in string if char.isalpha()).lower()

if string == string[::-1]:
    print("str is palindrome")
else:
    print("str is not palindrome")
