# Caesar cipher - decrypting a message.
cipher = input('Enter your cryptogram: ')
text = ''
for char in cipher:
    if not char.isalpha().:
        continue
    if char in 'y':
        code =
    elif char in 'z':
        code = 'b'
    else:
        code = ord(char) + 2
    text += chr(code)

print(text)