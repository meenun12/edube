import os

os.mkdir("my_second_directory")
print(os.listdir())
os.rmdir("my_second_directory")
print(os.listdir())
