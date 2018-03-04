def is_lower_101(character):
    if ord(character) >= 97:
        return True
    else:
        return False

def char_rot_13(character):
    if is_lower_101(character) is True:
        return chr(((ord(character) - 84) % 26) + 97)
    else:
        return chr(((ord(character) - 52) % 26) + 65)

def str_rot_13(string):
    output = ""
    for letter in string:
        if letter == " ":
            output += " "
        else:
            output += char_rot_13(letter)
    return output

def str_translate_101(string, old, new):
    return ''.join([new if letter == old else letter for letter in string])
