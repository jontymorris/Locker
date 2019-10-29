import os
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def read_file(path):
    '''
    Reads the given file and returns it's contents.
    '''

    handle = open(path, 'rb')
    contents = handle.read()
    handle.close()

    return contents


def write_file(path, contents):
    '''
    Writes the contents to the given file.
    '''

    handle = open(path, 'wb')
    handle.write(contents)
    handle.close()


def is_folder(path):
    '''
    Checks if the given path is a folder.
    '''

    return os.path.isdir(path)


def generate_fernet(password):
    '''
    Generates the encryption token from given password
    '''

    password = bytes(password, "utf-8")

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=b'',
        iterations=100000,
        backend=default_backend()
    )

    key = base64.urlsafe_b64encode(kdf.derive(password))

    return Fernet(key)


def encrypt_file(path, fernet):
    '''
    Encrypts the given the file with the password.
    '''

    contents = read_file(path)
    contents = fernet.encrypt(contents)

    write_file(path, contents)


def decrypt_file(path, fernet):
    '''
    Decrypts the given the file with the password.
    '''

    contents = read_file(path)
    contents = fernet.decrypt(contents)

    write_file(path, contents)


def encrypt_folder(path, fernet):
    '''
    Recursively encrypts the given folder with the password.
    '''

    for name in os.listdir(path):
        current_path = os.path.join(path, name)

        if is_folder(current_path):
            encrypt_folder(current_path, fernet)

        else:
            encrypt_file(current_path, fernet)


def decrypt_folder(path, fernet):
    '''
    Recursively decrypts the given folder with the password.
    '''

    for name in os.listdir(path):
        current_path = os.path.join(path, name)

        if is_folder(current_path):
            decrypt_folder(current_path, fernet)

        else:
            decrypt_file(current_path, fernet)


def encrypt(path, password):
    '''
    Encrypts the path. Supports both file's and folders.
    '''

    fernet = generate_fernet(password)

    # folder
    if is_folder(path):
        encrypt_folder(path, fernet)
    # file
    else:
        encrypt_file(path, fernet)


def decrypt(path, password):
    '''
    Decrypts the path. Supports both file's and folders.
    '''

    fernet = generate_fernet(password)

    # folder
    if is_folder(path):
        decrypt_folder(path, fernet)
    # file
    else:
        decrypt_file(path, fernet)
