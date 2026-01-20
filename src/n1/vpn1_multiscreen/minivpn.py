import json
from typing import Dict, Any
from pathlib import Path
from screens import LogsScreen, SettingsScreen, ChatScreen
from textual.app import App
from settings import Settings

SETTINGS_FILE = Path("settings.json")

class MiniVPNApp(App[None]):
    """Application Textual pour un mini VPN."""
    CSS_PATH = "style.css"  # optionnel
    SCREENS = {
        "logs": LogsScreen,
        "settings": SettingsScreen,
        "chat": ChatScreen,
    }
    BINDINGS = [
        ("ctrl+q", "quit", "Quitter"),
        ("l", "goto_logs", "Aller aux logs"),
        ("s", "goto_settings", "Aller aux paramètres"),
        ("c", "goto_chat", "Aller au chat"),
    ]
    settings: Settings = Settings()

    def __init__(self, **kwargs: Any):
        super().__init__(**kwargs)
        self.settings = Settings()

    def load_settings(self) -> None:
        """Charge les paramètres depuis le fichier JSON."""
        if SETTINGS_FILE.exists():
            with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.settings.local_ip = data.get("local_ip", "")
                self.settings.remote_ip = data.get("remote_ip", "")
                self.settings.port = int(data.get("port", 0))
        else:
            self.settings.local_ip = ""
            self.settings.remote_ip = ""
            self.settings.port = 0

    def on_mount(self) -> None:
        """
        Actions à effectuer lors du montage de l'application.
        Charge les paramètres et affiche l'écran approprié.
        """
        self.load_settings()

        if (self.settings.local_ip == "" or self.settings.remote_ip == "") \
            or self.settings.port == 0:
            self.push_screen("settings")
        else:
            self.push_screen("chat")

    def action_goto_logs(self) -> None:
        """Navigue vers l'écran des logs."""
        self.push_screen("logs")

    def action_goto_settings(self) -> None:
        """Navigue vers l'écran des paramètres."""
        self.push_screen("settings")

    def action_goto_chat(self) -> None:
        """Navigue vers l'écran de chat."""
        self.switch_screen("chat")

if __name__ == "__main__":
    MiniVPNApp().run()
