import sys
import os
import getpass
import encryptor


def show_usage():
    '''
    Prints out how to use the program.
    '''

    print('[Usage] locker {option} {path}')
    print('option \t= encrypt or decrypt')
    print("path \t= File or folder")


if __name__ == '__main__':
    args = sys.argv

    # debug
    args.append('encrypt')
    args.append('~/Documents/')

    # require 2 arguments
    if len(args) < 3:
        show_usage()
        exit(0)

    option = args[1].lower()
    path = args[2]

    password = getpass.getpass('Password: ')
    confirm = getpass.getpass('Retype password: ')

    # check password is right
    if password != confirm:
        print('Passwords don\'t match!')
        exit(0)

    # encrypt
    if option == 'encrypt':
        encryptor.encrypt(path, password)

    # decrypt
    elif option == 'decrypt':
        encryptor.decrypt(path, password)

    # invalid
    else:
        show_usage()
