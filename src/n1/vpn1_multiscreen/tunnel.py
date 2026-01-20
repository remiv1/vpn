"""
Module de tunnel pour l'application VPN1 à écrans multiples.
Gestion du tunnel VPN.
"""

import json
from typing import Any, Dict

def encapsulate(payload: bytes, tunnel_type: str="MINI-VPN"):
    """Encapsule les données dans un paquet JSON pour le tunnel VPN."""
    packet: Dict[str, Any] = {
        "type": tunnel_type,
        "length": len(payload),
        "payload": payload.hex()
    }
    return json.dumps(packet).encode()

def decapsulate(packet_bytes: bytes):
    """Décapsule les données d'un paquet JSON du tunnel VPN."""
    packet = json.loads(packet_bytes.decode())
    return bytes.fromhex(packet["payload"])
