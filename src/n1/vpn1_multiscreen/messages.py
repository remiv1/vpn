"""Modules de messages pour l'application VPN1 multiscreen."""

from textual.widgets import ListItem, Static

class SentMessage(ListItem):
    """Représente un message envoyé par l'utilisateur."""
    def __init__(self, text: str):
        super().__init__(
            Static(f"[Moi] {text}", classes="sent")
        )

class ReceivedMessage(ListItem):
    """Représente un message reçu d'un autre utilisateur."""
    def __init__(self, text: str):
        super().__init__(
            Static(f"{text} [Lui]", classes="received")
        )
