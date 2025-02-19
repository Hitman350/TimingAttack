import numpy as np
from aes import AES_Encryption
import os

class TimingAttack:
    def __init__(self, aes_instance):
        self.aes = aes_instance

    def perform_attack(self, plaintext, iterations=1000):
        """Measures encryption times to detect key leakage"""
        times = []
        for _ in range(iterations):
            _, time_taken = self.aes.encrypt_vulnerable(plaintext)
            times.append(time_taken)
        return np.mean(times), np.std(times)

if __name__ == "__main__":
    key = os.urandom(16)
    aes = AES_Encryption(key)
    attacker = TimingAttack(aes)

    plaintext = b"Attack at dawn"
    mean_time, std_dev = attacker.perform_attack(plaintext)
    
    print(f"Mean Encryption Time: {mean_time:.6f} sec")
    print(f"Standard Deviation: {std_dev:.6f} sec")
