"""
This program stores bytes array into binary file
"""

from os import strerror

data = bytearray(10)

for i in range(len(data)):
    data[i] = ord('a') + i
    print(ord('a') + i)

try:
    bf = open('file1.bin', 'wb')
    bf.write(data)
    bf.close()
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))

