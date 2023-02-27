try:
    stream = open("image.png", "rb")
    image = bytearray(stream.read())
    stream.close()
except IOError:
    print("failed")
else:
    print("success")