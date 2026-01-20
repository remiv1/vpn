"""Module des écrans pour l'application VPN1 à écrans multiples."""
from typing import TYPE_CHECKING, Any
#from datetime import datetime
from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Header, Footer, Input, Button, Static, Log, ListView

from settings import Settings
from udp import UDPClient
from crypto import encrypt_chacha20, decrypt_chacha20
from messages import SentMessage, ReceivedMessage
from tunnel import encapsulate, decapsulate

if TYPE_CHECKING:
    from minivpn import MiniVPNApp

FOOTER_NAME = "Mini VPN App Footer"
LOCAL_IP = "#local_ip"
REMOTE_IP = "#remote_ip"
PORT = "#port"

class LogsScreen(Screen[None]):
    """Écran pour afficher les logs de l'application."""
    def compose(self) -> ComposeResult:
        """Compose les widgets de l'écran."""
        yield Header(show_clock=True,
                     name="Logs de l'application VPN",
                     id="header",
                     icon="AIO")
        yield Static(content="Logs :", id="label")
        yield Log(id="log")
        yield Footer(name=FOOTER_NAME, id="footer")

class SettingsScreen(Screen[None]):
    """Écran pour les paramètres de l'application."""
    @property
    def app(self) -> "MiniVPNApp":
        """Retourne l'application principale."""
        return super().app  # type: ignore

    def compose(self) -> ComposeResult:
        """Compose les widgets de l'écran."""
        yield Header(show_clock=True,
                     name="Paramètres de l'application VPN",
                     id="header",
                     icon="AIO")
        yield Static(content="Paramètres :", id="label")
        yield Input(placeholder="IP locale", id="local_ip")
        yield Input(placeholder="IP distante", id="remote_ip")
        yield Input(placeholder="Port du serveur", id="port")
        yield Button(label="Enregistrer", id="save")
        yield Footer(name=FOOTER_NAME, id="footer")

    def on_mount(self) -> None:
        """Actions à effectuer lors du montage de l'écran."""
        settings: Settings = self.app.settings.load()
        if settings:
            self.query_one("#local_ip", Input).value = settings.local_ip
            self.query_one("#remote_ip", Input).value = settings.remote_ip
            self.query_one("#port", Input).value = str(settings.port)

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Gère l'événement de pression du bouton d'enregistrement."""
        if event.button.id == "save":
            lip: str = self.query_one(LOCAL_IP, Input).value
            rip: str = self.query_one(REMOTE_IP, Input).value
            pv: str = self.query_one(PORT, Input).value
            self.app.settings.save(local_ip=lip,
                                   remote_ip=rip,
                                   port=int(pv))
            self.app.push_screen("chat")


class ChatScreen(Screen[None]):
    """Écran pour le chat de l'application."""
    def __init__(self) -> None:
        super().__init__()
        self.udp: UDPClient
        self.listen_worker: Any
        self.run_worker: Any

    @property
    def app(self) -> "MiniVPNApp":
        """Retourne l'application principale."""
        return super().app  # type: ignore

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True, name="Chat VPN", id="header", icon="AIO")
        yield ListView(id="messages")
        yield Input(placeholder="Tape ton message ici", id="input")
        yield Button(label="Envoyer", id="send")
        yield Footer(name=FOOTER_NAME, id="footer")

    async def on_mount(self) -> None:
        """Lancement du listener UDP."""
        settings = self.app.settings

        self.udp = UDPClient(
            local_ip=settings.local_ip,
            port=settings.port,
            on_message=self.on_udp_message
        )

        # Lancer le listener en tâche de fond
        self.listen_worker = self.run_worker(self.udp.listen(), exclusive=True)

    async def on_unmount(self) -> None:
        """Arrêt propre du listener."""
        self.udp.close()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Gère l'événement de pression du bouton d'envoi."""
        if event.button.id == "send":
            text = self.query_one("#input", Input).value
            self.query_one("#input", Input).value = ""

            # Affichage local
            messages_view = self.query_one("#messages", ListView)
            messages_view.append(SentMessage(text))

            # Envoi réseau
            self.call_later(self.send_message, text)

    async def send_message(self, text: str):
        """Pipeline d'envoi : chiffrement → encapsulation → UDP."""
        key = self.app.settings.key  # clé ChaCha20 (32 bytes)

        nonce, ciphertext = encrypt_chacha20(key, text.encode())
        packet = encapsulate(nonce, ciphertext)

        await self.udp.send(
            packet,
            self.app.settings.remote_ip,
            self.app.settings.port
        )

    def on_udp_message(self, data: bytes, addr: tuple[str, int]) -> None:
        """Pipeline de réception : décapsulation → déchiffrement → affichage."""
        key: bytes = self.app.settings.key

        nonce, ciphertext = decapsulate(data)
        plaintext: bytes = decrypt_chacha20(key, nonce, ciphertext)
        message: str = plaintext.decode()

        messages = self.query_one("#messages", ListView)
        messages.append(ReceivedMessage(message))
