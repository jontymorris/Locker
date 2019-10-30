import sys
import os
import argparse
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
    # parse the arguments
    parser = argparse.ArgumentParser(description='Secure your file system')

    parser.add_argument('option', help='encrypt or decrypt')
    parser.add_argument('path', help='path to target file')

    args = parser.parse_args()

    # get the password
    password = getpass.getpass('Password: ')
    confirm = getpass.getpass('Retype password: ')

    # check passwords match
    if password != confirm:
        print('Passwords don\'t match!')
        exit(0)

    # encrypt
    if args.option.lower() == 'encrypt':
        encryptor.encrypt(args.path, password)

    # decrypt
    elif args.option.lower() == 'decrypt':
        encryptor.decrypt(args.path, password)

    # invalid
    else:
        show_usage()
