
import struct
import base64
import sys

from hashlib import md5, sha1
from Crypto.Cipher import AES
from Crypto.Random.random import getrandbits

# AES CBC requires blocks to be aligned on 16-byte boundaries.
BS = 16


def pad(s): return (s + (BS - len(s) % BS) *
                    chr(BS - len(s) % BS)).encode('utf-8')


def unpad(s): return s[0:-ord(s[-1])]


def EVP_ByteToKey(pwd, salt, key_len, iv_len):
    buf = md5(pwd + salt).digest()
    d = buf
    while len(buf) < (iv_len + key_len):
        d = md5(d + pwd + salt).digest()
        buf += d
    return buf[:key_len], buf[key_len:key_len + iv_len]


def aes_encrypt(pwd, plaintext):
    key_len, iv_len = 32, 16

    # generate salt
    salt = struct.pack('=Q', getrandbits(64))
    pwd = bytes(pwd, 'utf-8')
    # generate key, iv from password
    key, iv = EVP_ByteToKey(pwd, salt, key_len, iv_len)

    # pad plaintext
    plaintext = pad(plaintext)

    # create a cipher object
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # ref: openssl/apps/enc.c
    ciphertext = b'Salted__' + salt + cipher.encrypt(plaintext)

    # encode base64
    ciphertext = base64.b64encode(ciphertext)
    return ciphertext
