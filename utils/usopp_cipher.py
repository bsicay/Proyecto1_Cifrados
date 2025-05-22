import random

def generate_keystream(seed, length):
    random.seed(seed)  # PRNG débil
    return bytes([random.randint(0, 255) for _ in range(length)])

def encrypt(plaintext, seed):
    keystream = generate_keystream(seed, len(plaintext))
    return bytes([p ^ k for p, k in zip(plaintext.encode(), keystream)])

def decrypt(ciphertext):
    cipherbytes = bytes.fromhex(ciphertext)
    for seed in range(100000):  # Intentar semillas del 0 al 99999
        keystream = generate_keystream(seed, len(ciphertext))        
        plaintext = bytes([c ^ k for c, k in zip(cipherbytes, keystream)])        
        if plaintext.startswith(b"FLAG_"):  # Condición para detectar la flag
            print(f"Semilla encontrada: {seed}")
            print(f"Texto descifrado: {plaintext.decode()}")
            break
        
def usopp_cipher(flag, secret_seed):
    ciphertext = encrypt(flag, secret_seed)
    return ciphertext



if __name__ == "__main__":
    decrypt('a77742694e1d538c1c6d3c30d4c4df294c6c02379a1b138a411f26ec12fbc58cee1b028c39')

