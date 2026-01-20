'''
Module pour générer et sauvegarder une clé de chiffrement symétrique.
'''
import os
from Crypto.Random import get_random_bytes

# Génération de la clé
key = get_random_bytes(32)  # 256 bits pour ChaCha20/AES

# Sauvegarde dans un fichier binaire
with open("ma_cle.key", "wb") as f:
    f.write(key)

# (Optionnel) Restreindre les permissions du fichier (Linux)
os.chmod("ma_cle.key", 0o600)  # Lecture/écriture uniquement pour le propriétaire

print("Clé sauvegardée dans 'ma_cle.key' avec des permissions restreintes.")
print(f"Clé (hex)         : {key.hex()}")

# Chargement de la clé depuis le fichier
with open("ma_cle.key", "rb") as f:
    loaded_key = f.read()
print(f"Clé chargée (hex) : {loaded_key.hex()}")
assert key == loaded_key, "La clé chargée ne correspond pas à la clé sauvegardée!"
