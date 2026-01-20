"""
Module de tunnel pour l'application VPN1 à écrans multiples.
Gestion du tunnel VPN.
"""

import json
from typing import Any, Dict

def encapsulate(nonce: bytes, ciphertext: bytes, tunnel_type: str="MINI-VPN"):
    """Encapsule les données dans un paquet JSON pour le tunnel VPN."""
    if isinstance(tunnel_type, bytes):
        tunnel_type = tunnel_type.hex()
    packet: Dict[str, Any] = {
        "type": tunnel_type,
        "nonce": nonce.hex(),
        "length": len(ciphertext),
        "payload": ciphertext.hex()
    }
    return json.dumps(packet).encode()

def decapsulate(packet_bytes: bytes):
    """Décapsule les données d'un paquet JSON du tunnel VPN."""
    packet = json.loads(packet_bytes.decode())
    nonce = bytes.fromhex(packet["nonce"])
    ciphertext = bytes.fromhex(packet["payload"])
    return nonce, ciphertext
