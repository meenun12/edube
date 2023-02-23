# Caesar cipher - decrypting a message.
cipher = input('Enter your cryptogram: ')
text = ''
for char in cipher:

    if char.isalnum() or char.isspace():

        if char.isalpha():
            if char not in 'yz':
                code = ord(char) + 2
            elif char in 'y':
                code = ord('a')
            elif char in 'z':
                code = ord('b')
        if char.isspace():
            code = ord(char)

        text += chr(code)

        if char.isdigit():
            text += char

print(text)