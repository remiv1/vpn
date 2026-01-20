"""Classe pour stocker les paramètres de configuration du VPN."""

from dataclasses import dataclass
import json

@dataclass
class Settings:
    """Classe pour stocker les paramètres de configuration du VPN."""
    local_ip: str
    remote_ip: str
    port: int
    key: bytes

    def __init__(self, local_ip: str = "", remote_ip: str = "", port: int = 0):
        self.local_ip: str = local_ip
        self.remote_ip: str = remote_ip
        self.port: int = port
        self.key: bytes = b"0123456789ABCDEF0123456789ABCDEF"  # Clé fixe pour ChaCha20-Poly1305

    def save(self, local_ip: str, remote_ip: str, port: int) -> None:
        """Met à jour les paramètres."""
        self.local_ip = local_ip
        self.remote_ip = remote_ip
        self.port = port
        with open("settings.json", "w", encoding="utf-8") as f:
            f.write(f'{{"local_ip": "{local_ip}", "remote_ip": "{remote_ip}", "port": {port}}}')

    def load(self) -> 'Settings':
        """Charge les paramètres depuis le fichier JSON."""
        try:
            with open("settings.json", "r", encoding="utf-8") as f:
                data = json.loads(f.read())
                self.local_ip: str = data["local_ip"]
                self.remote_ip: str = data["remote_ip"]
                self.port: int = int(data["port"])
        except FileNotFoundError:
            self.local_ip = ""
            self.remote_ip = ""
            self.port = 0

        return self
