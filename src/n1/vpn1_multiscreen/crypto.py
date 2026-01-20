"""
Module de cryptographie pour l'application VPN1 à écrans multiples.
Gestion du chiffrement et du déchiffrement des messages.
"""

import os
from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305

def encrypt_chacha20(key: bytes, plaintext: bytes) -> tuple[bytes, bytes]:
    """Chiffre les données avec ChaCha20-Poly1305."""
    nonce = os.urandom(12)
    cipher = ChaCha20Poly1305(key)
    ciphertext = cipher.encrypt(nonce, plaintext, None)
    return nonce, ciphertext

def decrypt_chacha20(key: bytes, nonce: bytes, ciphertext: bytes) -> bytes:
    """Déchiffre les données avec ChaCha20-Poly1305."""
    cipher = ChaCha20Poly1305(key)
    return cipher.decrypt(nonce, ciphertext, None)
