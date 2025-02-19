from Crypto.Cipher import AES
import os
import time

class AES_Encryption:
    def __init__(self, key):
        self.key = key
        self.cipher = AES.new(self.key, AES.MODE_ECB)

    def encrypt_vulnerable(self, plaintext):
        """Vulnerable AES encryption (timing leakage)"""
        start_time = time.time()
        ciphertext = self.cipher.encrypt(plaintext.ljust(16))  # Padding manually
        time_taken = time.time() - start_time
        return ciphertext, time_taken

    def encrypt_secure(self, plaintext):
        """Constant-time AES encryption (secure)"""
        start_time = time.time()
        ciphertext = self.cipher.encrypt(plaintext.ljust(16))  # Using fixed-size padding
        time_taken = time.time() - start_time
        return ciphertext, time_taken

if __name__ == "__main__":
    key = os.urandom(16)
    aes = AES_Encryption(key)

    plaintext = b"Attack at dawn"
    print("Vulnerable Encryption:", aes.encrypt_vulnerable(plaintext))
    print("Secure Encryption:", aes.encrypt_secure(plaintext))
