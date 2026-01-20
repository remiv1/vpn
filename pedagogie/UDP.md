# Prise en main d’UDP avec Python

## Objectifs de l’exercice

- Comprendre le protocole UDP et ses différences avec TCP
- Savoir créer un client et un serveur UDP en Python
- Identifier les erreurs courantes et les bonnes pratiques
- Être capable de réaliser un échange de bout en bout

---

## 1. Introduction à UDP

UDP (User Datagram Protocol) est un protocole de transport simple, rapide, mais non fiable :

- Pas de connexion préalable (pas de handshake)
- Pas de garantie de livraison, d’ordre ou d’unicité des paquets
- Utilisé pour la voix, la vidéo, les jeux en ligne, etc.

> ***À retenir :*** UDP est plus rapide que TCP mais ne garantit pas la fiabilité.

---

## 2. Exercice pratique : Client/Serveur UDP

### a) Serveur UDP minimal

Créez un fichier `serveur_udp.py` :

```python
import socket

# Création du socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("127.0.0.1", 12345))
print("Serveur UDP en attente...")

while True:
    data, addr = sock.recvfrom(1024)
    print(f"Reçu de {addr} : {data.decode()}")
    sock.sendto(b'ACK', addr)
```

### b) Client UDP minimal

Créez un fichier `client_udp.py` :

```python
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(b'Bonjour UDP', ("127.0.0.1", 12345))
reponse, _ = sock.recvfrom(1024)
print(f"Réponse du serveur : {reponse.decode()}")
```

---

## 3. Expérimentations

- [X] Lancez le serveur, puis le client.
- [X] Modifiez le client pour envoyer plusieurs messages.
- [X] Arrêtez le serveur et observez le comportement du client.
  - `Le client bloque en attente de réponse.`
  - Si on relance le serveur, Il faut relancer le client pour recevoir la réponse.

---

## 4. Erreurs courantes à éviter

- **Oublier de fermer le socket** : utilisez `sock.close()` quand c’est fini.
- **Supposer que les paquets arrivent dans l’ordre** : UDP ne garantit pas l’ordre.
- **Ignorer les pertes de paquets** : UDP ne retransmet pas automatiquement.
- **Utiliser UDP pour des données critiques** : préférez TCP si la fiabilité est essentielle.

---

## 5. Pour aller plus loin

- Ajoutez une gestion du timeout côté client (`sock.settimeout(2)`).
- Essayez d’envoyer de gros messages (> 65 507 octets) et observez le résultat.
  - ```OSError: [Errno 90] Message too long```
- Implémentez un mini-protocole d’accusé de réception.

---

## 6. Ressources complémentaires

- [Documentation officielle Python - socket](https://docs.python.org/fr/3/library/socket.html)

---

> ***But :*** Comprendre les fondamentaux d’UDP, savoir l’utiliser en Python, et éviter les pièges classiques.
