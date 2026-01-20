'''
Module client UDP simple en Python - Côté client
'''

import socket
import time

# Création du socket UDP
sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Génération du message à envoyer
MESSAGE = input("Entrez le message à envoyer au serveur UDP: ")

# Envoi du message au serveur avec gestion du timeout et renvois
sock.settimeout(2)  # Timeout de 2 secondes
MAX_RETRY = 5
TIME_RETRY = 15  # secondes entre les tentatives
retry: int = 0
recu: bool = False

while retry < MAX_RETRY and not recu:
    try:
        sock.sendto(MESSAGE.encode(), ("192.168.1.137", 12345))
        reponse, adresse_retour = sock.recvfrom(1024)
        resp: str = reponse.decode()
        ad = adresse_retour[0]
        port = adresse_retour[1]
        print(f"Réponse du serveur: {resp} sur {ad}, port {port}")
        recu = True
    except socket.timeout:
        retry += 1
        print(f"Timeout, tentative {retry}/{MAX_RETRY}...")
        time.sleep(TIME_RETRY)
if not recu:
    print(f"Aucune réponse serveur après {MAX_RETRY} tentatives espacées de {TIME_RETRY} secondes.")
