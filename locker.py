import sys
import os
import getpass
import vigenere


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


def encrypt_file(path, password):
    '''
    Encrypts the given the file with the password.
    '''

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


def is_folder(path):
    '''
    Checks if the given path is a folder.
    '''

    return os.path.isdir(path)


def show_usage():
    '''
    Prints out how to use the program.
    '''

    print('[Usage] locker {option} {path}')
    print('option \t= encrypt or decrypt')
    print("path \t= File or folder")


if __name__ == '__main__':
    args = sys.argv

    # require 2 arguments
    if len(args) < 3:
        show_usage()
        exit(0)

    option = args[1].lower()
    path = args[2]

    password = getpass.getpass()

    # encrypt
    if option == 'encrypt':
        # folder
        if is_folder(path):
            encrypt_folder(path, password)
        # file
        else:
            encrypt_file(path, password)

    # decrypt
    elif option == 'decrypt':
        # folder
        if is_folder(path):
            decrypt_folder(path, password)
        # file
        else:
            decrypt_file(path, password)

    # invalid
    else:
        show_usage()
