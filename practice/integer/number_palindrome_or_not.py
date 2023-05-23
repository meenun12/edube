def is_palindrome(n):

    n = str(n)

    if len(n) <= 1:
        return True

    total = len(n)

    if n[0] == n[total-1]:
        return is_palindrome(n[1:-1])
    else:
        return False


n = int(input("Enter a number"))
if is_palindrome(n):
    print(n, "Num is palindrome")
else:
    print(n, "Num is not palindrome")