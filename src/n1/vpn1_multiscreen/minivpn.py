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

    def save_settings(self, local_ip: str, remote_ip: str, port: int) -> None:
        """Sauvegarde les paramètres dans le fichier JSON."""
        data: Dict[str, Any] = {
            "local_ip": local_ip,
            "remote_ip": remote_ip,
            "port": port,
        }
        with open(SETTINGS_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        self.settings.local_ip = data.get("local_ip", "")
        self.settings.remote_ip = data.get("remote_ip", "")
        self.settings.port = int(data.get("port", 0))

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

if __name__ == "__main__":
    MiniVPNApp().run()
