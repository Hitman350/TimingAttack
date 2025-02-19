from aes import AES_Encryption
import os

if __name__ == "__main__":
    key = os.urandom(16)
    aes = AES_Encryption(key)

    plaintext = b"Attack at dawn"
    _, vulnerable_time = aes.encrypt_vulnerable(plaintext)
    _, secure_time = aes.encrypt_secure(plaintext)

    print(f"Vulnerable AES Time: {vulnerable_time:.6f} sec")
    print(f"Secure AES Time: {secure_time:.6f} sec (Constant-Time)")
