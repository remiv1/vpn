# 🛠️ WORKFLOW — Explication du Mini‑VPN Niveau 1

## Qu’est-ce qu’un VPN minimaliste ?

Un VPN (Virtual Private Network) permet de créer un tunnel sécurisé entre deux machines, même à travers Internet. Ici, on construit la version la plus simple possible : un client et un serveur qui échangent des messages chiffrés via UDP.

## Comment ça marche ?

1. **Le client chiffre un message** avec une clé secrète partagée.
2. **Le client envoie ce message** via UDP au serveur.
3. **Le serveur reçoit le message**, le déchiffre avec la même clé.
4. **Le serveur peut répondre** en chiffrant sa réponse de la même façon.

## Pourquoi UDP ?

UDP est un protocole réseau très simple, sans connexion ni garantie de livraison. Il est parfait pour comprendre les bases sans complexité inutile.

## Le chiffrement, c’est quoi ?

On utilise un algorithme comme AES ou ChaCha20 ou d'autres encore pour rendre le message illisible à toute personne n’ayant pas la clé. Ici, la clé est la même pour le client et le serveur (clé partagée).

## À quoi sert l’encapsulation ?

On place le message original dans une enveloppe chiffrée. Seul le destinataire ayant la clé peut ouvrir l’enveloppe et lire le contenu.

## Limites de cette version

- Pas d’authentification forte
- Pas de gestion de plusieurs clients
- Pas d’interface réseau virtuelle (pas de vrai tunnel IP)
- Clé statique (pas d’échange dynamique)

## Ce qu’on apprend avec ce workflow

- Les bases du réseau (UDP)
- Le chiffrement symétrique appliqué
- La logique d’un tunnel sécurisé
- Les fondations d’un vrai VPN

---

> ***Ce workflow est conçu pour être pédagogique et accessible, même sans connaissance réseau avancée.***
