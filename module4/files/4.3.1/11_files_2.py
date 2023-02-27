from os import strerror

data = bytearray(5)

try:
    bf = open('file1.bin', 'rb')
    bf.readinto(data)
    bf.close()

    for b in data:
        print(b, end=' ')
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))