import binascii

# Mensaje cifrado en hexadecimal
cipher_hex = "747d767268560904050200540406540707525052005451000300540e00030b0702560f5154"
cipher_bytes = bytes.fromhex(cipher_hex)

# Interpretación 1: clave como caracteres ASCII
key_ascii = b"21757"
decoded_ascii = bytes([b ^ key_ascii[i % len(key_ascii)] for i, b in enumerate(cipher_bytes)])

print(" Descifrado usando clave ASCII '21757':")
print(decoded_ascii.decode('utf-8', errors='replace'))


