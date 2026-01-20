"""
Mini VPN Application utilisant Textual
Application minimaliste de VPN pour envoi de messages dans un tunnel chiffré.
"""
from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.widgets import Header, Footer, Input, Button, Static, Log

FOOTER_NAME = "Mini VPN App Footer"


class MiniVPNApp(App[None]):
    """Application Textual pour un mini VPN."""
    CSS_PATH = "style.css"  # optionnel
    SCREENS = {
        "logs": LogsScreen,
        "settings": SettingsScreen,
        "chat": ChatScreen,
    }

    def on_mount(self) -> None:
        """Actions à effectuer lors du montage de l'application."""
        self.push_screen("settings")  # Affiche l'écran de paramètres au démarrage

    def on_button_pressed(self, event: Button.Pressed):
        """Gère l'événement de pression du bouton."""
        if event.button.id == "send":
            # 1. Récupérer le message
            message = self.query_one("#input", Input).value

            # 2. Simuler ton pipeline mini-VPN
            steps = [ f"Message original : {message}",
                     "🔐 Chiffrement ............. OK",
                     "📦 Encapsulation ........... OK",
                     "📡 Envoi UDP ............... OK",
                     "📭 Réception ............... OK",
                     "🔓 Déchiffrement ........... OK",
                    ]

            # 3. Mettre à jour le pipeline
            pipeline = self.query_one("#pipeline", Pipeline)
            pipeline.show_steps(steps)

            # 4. Écrire quelques logs
            log = self.query_one("#log", Log)
            log.write("Message saisi par l'utilisateur")
            log.write("Chiffrement effectué")
            log.write("Paquet encapsulé et envoyé (simulé)")
            log.write("Paquet reçu et décapsulé (simulé)")

    def on_key(self, event: events.Key) -> None:
        if event.key == "l":
            self.push_screen("logs")
        elif event.key == "s":
            self.push_screen("settings")
        elif event.key == "c":
            self.push_screen("chat")


class Pipeline(Static):
    """Widget pour afficher les étapes d'un pipeline."""
    def update_steps(self, steps: list[str]):
        """Met à jour l'affichage des étapes du pipeline."""
        content = "\n".join(f"{i+1}. {step}" for i, step in enumerate(steps))
        self.update(content)

    def show_steps(self, steps: list[str]):
        """Affiche les étapes du pipeline."""
        self.update_steps(steps)



if __name__ == "__main__":
    MiniVPNApp().run()
