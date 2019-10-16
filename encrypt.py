import vigenere
import system
import os


def should_process_file(path):
    '''
    Returns whether the given file should be processed
    based on if the file's extension is in a given whitelist.
    '''

    whitelist = [
        '',
        '.txt',
        '.py',
        '.pyw',
        '.js',
    ]

    extension = os.path.splitext(path)[1]

    return extension.lower() in whitelist


def read_file(path):
    '''
    Reads the given file and returns it's contents.
    '''

    handle = open(path, 'r', encoding='utf-8')
    contents = handle.read()
    handle.close()

    return contents


def write_file(path, contents):
    '''
    Writes the contents to the given file.
    '''

    handle = open(path, 'w', encoding='utf-8')
    handle.write(contents)
    handle.close()


def is_folder(path):
    '''
    Checks if the given path is a folder.
    '''

    return os.path.isdir(path)


def encrypt_file(path, password):
    '''
    Encrypts the given the file with the password.
    '''

    if not should_process_file(path):
        return

    try:
        contents = read_file(path)
        contents = vigenere.encrypt(contents, password)
        write_file(path, contents)
    except:
        print('[Error] Failed to encrypt {}'.format(path))


def decrypt_file(path, password):
    '''
    Decrypts the given the file with the password.
    '''

    if not should_process_file(path):
        return

    try:
        contents = read_file(path)
        contents = vigenere.decrypt(contents, password)
        write_file(path, contents)
    except:
        print('[Error] Failed to decrypt {}'.format(path))


def encrypt_folder(path, password):
    '''
    Recursively encrypts the given folder with the password.
    '''

    for name in os.listdir(path):
        current_path = os.path.join(path, name)

        if is_folder(current_path):
            encrypt_folder(current_path, password)

        else:
            encrypt_file(current_path, password)


def decrypt_folder(path, password):
    '''
    Recursively decrypts the given folder with the password.
    '''

    for name in os.listdir(path):
        current_path = os.path.join(path, name)

        if is_folder(current_path):
            decrypt_file(current_path, password)

        else:
            decrypt_file(current_path, password)
