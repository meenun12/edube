from os import strerror

try:
    bf = open('file1.bin', 'rb')
    data = bytearray(bf.read(5))
    bf.close()

    for b in data:
        print(b, end='')

except IOError as e:
    print("I/O error occurred:", strerror(e.errno))
