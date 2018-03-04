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
