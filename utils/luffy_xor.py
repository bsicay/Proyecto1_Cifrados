def xor_cipher(text, key):
    # Convertir tanto el texto como la clave a bytes
    if type(text) == str:
        text_bytes = text.encode()
    else:
        text_bytes = text
    key_bytes = key.encode()  # Convertir la clave a bytes

    # Cifrar con XOR
    cipher_text = bytes([text_bytes[i] ^ key_bytes[i % len(key_bytes)] for i in range(len(text_bytes))])
    
    return cipher_text


if __name__ == "__main__":
    cipher_text = "747d767268560904050200540406540707525052005451000300540e00030b0702560f5154"
    carne = '21757'
    results = xor_cipher(cipher_text, carne)


    print(f"results: {results}")
