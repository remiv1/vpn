'''
Module de compréhension du chiffrement ChaCha20 en Python
'''
from Crypto.Cipher import ChaCha20, ChaCha20_Poly1305  # type: ignore
from Crypto.Random import get_random_bytes


# --- ChaCha20-Poly1305 (mode authentifié) ---
print("\n--- Exemple ChaCha20-Poly1305 (authentifié) ---")
key = get_random_bytes(32)  # 256 bits
nonce = get_random_bytes(12)  # 96 bits

# Création d'un service chacha20-poly1305
cipher = ChaCha20_Poly1305.new(key=key, nonce=nonce)  # type: ignore

# Lecture d'un fichier à chiffrer et chiffrement des données
with open("fichier.txt", "rb") as f:
    plaintext = f.read()
ciphertext, tag = cipher.encrypt_and_digest(plaintext)  # type: ignore

# Écriture des fichiers chiffré et tag
with open("fichier_chiffre_poly.txt", "wb") as f:
    f.write(ciphertext) # type: ignore
with open("fichier_tag_poly.txt", "wb") as f:
    f.write(tag)    # type: ignore

# Affichage des informations
print("Fichier chiffré avec ChaCha20-Poly1305.")
print(f"Clé (hex) : {key.hex()}")
print(f"Nonce (hex) : {nonce.hex()}")
print(f"Tag (hex) : {tag.hex()}")   # type: ignore
print(f"Chifftext (hex) : {ciphertext[:32].hex()}...")  # type: ignore 32 premiers car hexadécimaux

# Déchiffrage avec corruption volontaire
decipher = ChaCha20_Poly1305.new(key=key, nonce=nonce)  # type: ignore
with open("fichier_chiffre_poly.txt", "rb") as f:
    ciphertext = f.read()
with open("fichier_tag_poly.txt", "rb") as f:
    tag = f.read()

# Corruption volontaire du ciphertext
ciphertext = ciphertext + b"corruption"

# Tentative de déchiffrement avec vérification d'intégrité
try:
    decrypted = decipher.decrypt_and_verify(ciphertext, tag)  # type: ignore
    with open("fichier_dechiffre_poly.txt", "wb") as f:
        f.write(decrypted)  # type: ignore
    print("Fichier déchiffré avec ChaCha20-Poly1305.")
except ValueError as e:
    print(f"Erreur d'intégrité détectée : {e}")

# Chiffrage d'un fichier en simple ChaCha20
print("\n\n--- Exemple ChaCha20 (simple) ---")
key = get_random_bytes(32)  # 256 bits
nonce = get_random_bytes(12)  # 96 bits
cipher = ChaCha20.new(key=key, nonce=nonce) # type: ignore

# Lecture du fichier à chiffrer
with open("fichier.txt", "rb") as f:
    plaintext = f.read()

# Chiffrement
ciphertext = cipher.encrypt(plaintext)  # type: ignore

# Écriture du fichier chiffré
with open("fichier_chiffre_chacha20.txt", "wb") as f:
    f.write(ciphertext) # type: ignore

# Affichage des informations
print("Fichier chiffré avec ChaCha20.")
print(f"Clé (hex) : {key.hex()}")
print(f"Nonce (hex) : {nonce.hex()}")
print(f"Chifftext (hex) : {ciphertext.hex()}...")  # type: ignore 64 premiers car hexadécimaux

# Déchiffrage du fichier avec corruption volontaire
decipher = ChaCha20.new(key=key, nonce=nonce)   # type: ignore
with open("fichier_chiffre_chacha20.txt", "rb") as f:
    ciphertext = f.read()

# Corruption volontaire du ciphertext
ciphertext = ciphertext + b"corruption"  # type: ignore

# Déchiffrement
decrypted = decipher.decrypt(ciphertext)  # type: ignore
with open("fichier_dechiffre_chacha20.txt", "wb") as f:
    f.write(decrypted)  # type: ignore
print("Fichier déchiffré avec ChaCha20.")
