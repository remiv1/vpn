'''
Module de serveur UDP simple en Python - Côté serveur
'''

import socket

# Création du socket UDP
sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
sock.bind(("0.0.0.0", 12345))
print("Serveur UDP en écoute sur le port 12345...")

while True:
    # Réception des données
    data, addr = sock.recvfrom(1024)  # Taille maximale du buffer de réception
    print(f"Reçu {data.decode()} de {addr}")

    # Envoi d'une réponse
    RESPONSE = b"Message recu".upper()
    sock.sendto(RESPONSE, addr)
    print(f"Envoyé {RESPONSE} à {addr}")
