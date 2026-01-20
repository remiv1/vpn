"""
Module UDP pour l'application VPN1 à écrans multiples.
Gestion de l'envoi et de la réception des messages UDP.
"""

import asyncio
import socket
from typing import Callable

class UDPClient:
    """Client UDP pour envoyer et recevoir des messages."""
    def __init__(self, local_ip: str, port: int, on_message: Callable[..., None]):
        self.local_ip = local_ip
        self.port = port
        self.on_message = on_message  # callback
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((local_ip, port))
        self.sock.setblocking(False)
        self.running = True

    async def listen(self):
        """Écoute les messages entrants."""
        loop = asyncio.get_running_loop()
        while True:
            data, addr = await loop.sock_recvfrom(self.sock, 4096)
            self.on_message(data, addr)

    async def send(self, data: bytes, remote_ip: str, port: int):
        """Envoie un message UDP."""
        await asyncio.get_running_loop().sock_sendto(
            self.sock, data, (remote_ip, port)
        )

    def close(self):
        """Ferme le socket UDP."""
        self.running = False
        self.sock.close()
