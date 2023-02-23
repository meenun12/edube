# Caesar cipher - decrypting a message.
cipher = input('Enter your cryptogram: ')
text = ''
for char in cipher:

    if char.isalnum() or char.isspace():

        if char.isalpha():
            if char not in 'a':
                code = ord(char) - 1
            elif char in 'a':
                code = ord('z')
        if char.isspace():
            code = ord(char)

        text += chr(code)

        if char.isdigit():
            text += char

print(text)