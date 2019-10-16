def encrypt(text, password):
    '''
    Encrypts the string using the vingenere cipher.
    Note, this encryption is extremly weak.
    '''

    output = ''
    index = 0
    for char in text:
        output += chr(ord(char) + ord(password[index]))

        index += 1
        if index >= len(password):
            index = 0

    return output


def decrypt(text, password):
    '''
    Decrypts the string using the vingenere cipher.
    '''

    output = ''
    index = 0
    for char in text:
        output += chr(ord(char) - ord(password[index]))

        index += 1
        if index >= len(password):
            index = 0

    return output
