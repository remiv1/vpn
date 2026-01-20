'''
Module d'exploration du chiffrement symétrique en Python
'''
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# Clé et IV
key = get_random_bytes(32)  # 256 bits
iv = get_random_bytes(16)   # 128 bits pour AES

# Chiffrement
cipher = AES.new(key=key, mode=AES.MODE_GCM, nonce=iv)    # type: ignore
MESSAGE = b"Message secret a chiffrer"
ciphertext, tag = cipher.encrypt_and_digest(MESSAGE)    # type: ignore
print(f"Chiffré : {ciphertext.hex()}")  # type: ignore
print(f"Tag : {tag.hex()}") # type: ignore

# Déchiffrement
decipher = AES.new(key, AES.MODE_GCM, iv)   # type: ignore
decipher.update(b"")  # type: ignore Si des données supplémentaires sont authentifiées
decrypted = decipher.decrypt_and_verify(ciphertext, tag)    # type: ignore
print(f"Déchiffré : {decrypted.decode()}")  # type: ignore
