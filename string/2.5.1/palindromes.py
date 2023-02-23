# Caesar cipher - decrypting a message.
palin = input('Enter your sentence: ')
palin = palin.lower().replace(" ", "")

text = ''
length = len(palin) - 1

for char in palin:

    if char.isalnum():
        text += palin[length]
    length = length-1

if palin == text:
   print("It's a palindrome")
else:
   print("It's not a palindrome")

