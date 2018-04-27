import struct
import base64
import sys

from hashlib import md5, sha1
from Crypto.Cipher import AES
from Crypto.Random.random import getrandbits

# AES CBC requires blocks to be aligned on 16-byte boundaries.
BS = 16


def unpad(s): return s[0:-s[-1]]


def EVP_ByteToKey(pwd, salt, key_len, iv_len):
    buf = md5(pwd + salt).digest()
    d = buf
    while len(buf) < (iv_len + key_len):
        d = md5(d + pwd + salt).digest()
        buf += d
    return buf[:key_len], buf[key_len:key_len + iv_len]


def aes_decrypt(pwd, cipher_string):
    cipher_bites = bytes(cipher_string.split("'")[1], 'utf-8')
    ciphertext = base64.b64decode(cipher_bites)
    pwd = bytes(pwd, 'utf-8')
    # check magic
    if ciphertext[:8] != b'Salted__':
        raise Exception("bad magic number")

    # get salt
    salt = ciphertext[8:16]

    # get key, iv
    key, iv = EVP_ByteToKey(pwd, salt, 32, 16)

    # decrypt
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(ciphertext[16:])).strip().decode('utf-8')
