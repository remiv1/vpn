"""
Mini VPN Application utilisant Textual
Application minimaliste de VPN pour envoi de messages dans un tunnel chiffré.
Application de démonstration du pipeline de traitement des messages.
Une seule page avec un champ d'entrée, un bouton d'envoi, un affichage du pipeline et des logs.
Pas d'envoi réel de messages, juste une simulation des étapes.
"""
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Input, Button, Static, Log

FOOTER_NAME = "Mini VPN App Footer"


class Pipeline(Static):
    """Widget pour afficher les étapes d'un pipeline."""
    def show_steps(self, steps: list[str]):
        """Met à jour l'affichage avec les étapes du pipeline."""
        content = "\n".join(f"{i+1}. {step}" for i, step in enumerate(steps))
        self.update(content)


class MiniVPNApp(App[None]):
    """Application Textual pour un mini VPN."""
    CSS_PATH = "style.css"

    def compose(self) -> ComposeResult:
        """Compose les widgets de l'application."""
        yield Header(show_clock=True,
                     name="Mini VPN - Démo pipeline",
                     id="header",
                     icon="AIO")
        yield Static("Message à envoyer :", id="label")
        yield Input(placeholder="Tape ton message ici", id="input")
        yield Button("Envoyer", id="send")
        yield Pipeline(id="pipeline")
        yield Log(id="log")
        yield Footer(name=FOOTER_NAME, id="footer")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Gère l'événement de pression du bouton d'envoi."""
        if event.button.id == "send":
            message = self.query_one("#input", Input).value

            steps = [
                f"Message original : {message}",
                "🔐 Chiffrement ............. OK",
                "📦 Encapsulation ........... OK",
                "📡 Envoi UDP ............... OK",
                "📭 Réception ............... OK",
                "🔓 Déchiffrement ........... OK",
            ]

            pipeline = self.query_one("#pipeline", Pipeline)
            pipeline.show_steps(steps)

            log = self.query_one("#log", Log)
            log.write("Message saisi par l'utilisateur\n")
            log.write("Chiffrement effectué\n")
            log.write("Paquet encapsulé et envoyé (simulé)\n")
            log.write("Paquet reçu et décapsulé (simulé)\n")


if __name__ == "__main__":
    MiniVPNApp().run()
