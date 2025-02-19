import matplotlib
matplotlib.use("Agg")  # Use Agg backend to generate plots as images
import matplotlib.pyplot as plt
import numpy as np
import os
from timing_attack import TimingAttack
from aes import AES_Encryption

def generate_timing_attack_plot():
    key = os.urandom(16)
    aes = AES_Encryption(key)
    attacker = TimingAttack(aes)

    plaintext = b"Attack at dawn"
    times = [attacker.perform_attack(plaintext)[0] for _ in range(100)]

    plt.figure(figsize=(8, 6))
    plt.hist(times, bins=20, alpha=0.7, color="blue")
    plt.xlabel("Encryption Time (seconds)")
    plt.ylabel("Frequency")
    plt.title("Timing Attack on AES Encryption")

    plot_path = "static/timing_attack.png"
    plt.savefig(plot_path)  # Save the plot instead of showing it
    plt.close()  # Free memory

    return plot_path  # Return the file path for HTML template
