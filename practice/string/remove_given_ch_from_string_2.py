'''
Python program to remove given character from string
'''

def remove_char(input_string, char_to_remove):

    output_string = ""
    for i in input_string:
        if i != char_to_remove:
            output_string += i

    return output_string


input_string = "hello_world"
char_to_remove = "l"
output_string = remove_char(input_string, char_to_remove)
print(output_string)



