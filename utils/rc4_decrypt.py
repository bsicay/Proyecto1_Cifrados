def rc4(key, data):
    S = list(range(256))
    j = 0
    out = []

    # Key Scheduling Algorithm (KSA)
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]

    # Pseudo-Random Generation Algorithm (PRGA)
    i = j = 0
    for char in data:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % 256]
        out.append(char ^ K)

    return bytes(out)

if __name__ == "__main__":
    # Mensaje cifrado en hex
    cipher_hex = "7a0e44502ee5c8f505a4fe70550b99005b2b5037af1ff22171847385360962e0ca9d4d718d"
    
    # Convertir a bytes
    cipher_bytes = bytes.fromhex(cipher_hex)

    # Clave como bytes
    key = b"21757"

    # Descifrado
    plain = rc4(key, cipher_bytes)

    print("Mensaje descifrado:")
    print(plain.decode("utf-8", errors="replace"))




