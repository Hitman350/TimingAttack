import time
from aes import AES_Encryption
import os

if __name__ == "__main__":
    key = os.urandom(16)
    aes = AES_Encryption(key)

    plaintext = b"Attack at dawn"
    
    start = time.time()
    for _ in range(10000):
        aes.encrypt_vulnerable(plaintext)
    end = time.time()
    print(f"Vulnerable AES: {end - start:.2f} sec")

    start = time.time()
    for _ in range(10000):
        aes.encrypt_secure(plaintext)
    end = time.time()
    print(f"Secure AES: {end - start:.2f} sec")
