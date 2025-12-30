# 📄 Page Portfolio — Projet Mini‑VPN Pédagogique janvier-février 2026

## 🏷️ Mini‑VPN pédagogique — Construction d’un protocole sécurisé étape par étape

### 🎯 Résumé du projet

Ce projet explore la création d’un VPN minimaliste, développé en trois niveaux progressifs.L’objectif est d’apprendre, démontrer et documenter la construction d’un tunnel chiffré, puis d’un protocole réseau complet, jusqu’à une version avancée avec API et interface.

Chaque niveau est :

- développé dans une branche Git dédiée
- documenté
- démontré en vidéo
- intégré dans le portfolio
- comparé au niveau précédent

Ce projet met en valeur mes compétences en réseau bas niveau, cryptographie appliquée, architecture logicielle, documentation technique, et pédagogie.

---

## 🧱 Structure du projet

### Branches Git

- v1-mini-vpn → Niveau 1 : tunnel chiffré minimaliste
- v2-protocol-vpn → Niveau 2 : protocole + TUN/TAP
- v3-advanced-vpn → Niveau 3 : version avancée (API + UI)
- main → version stable affichée sur le site

Chaque branche contient :

- code source
- documentation
- schémas
- vidéos de démonstration
- notes d’évolution

---

## 🟦 Niveau 1 — Mini‑VPN minimaliste

### 🎯 Objectif de cette branche N1

Créer un tunnel chiffré simple entre un client et un serveur, sans interface réseau virtuelle.

### 🔧 Fonctionnalités N1

- Serveur UDP minimal
- Client UDP minimal
- Chiffrement AES ou ChaCha20
- Clé partagée statique
- Encapsulation/décapsulation de messages
- Logs simples
- Démo en ligne de commande

### 📚 Documentation incluse N1

- Architecture du niveau 1
- Explication du chiffrement
- Explication du tunnel logique
- Limites du niveau 1
- Comparaison avec un VPN réel

### 🎥 Démonstration vidéo N1

- Lancement du serveur
- Lancement du client
- Envoi d’un message chiffré
- Déchiffrement côté serveur
- Retour d’un message chiffré

### 🧭 Ce que j’ai appris sur le N1

- Sockets UDP
- Chiffrement symétrique appliqué
- Encapsulation de données
- Structure d’un tunnel réseau
- Documentation technique claire

## 🟩 Niveau 2 — VPN réaliste (protocole + TUN/TAP)

### 🎯 Objectif de cette branche N2

Passer d’un tunnel logique à un tunnel réseau réel transportant des paquets IP.

### 🔧 Fonctionnalités N2

- Interface TUN/TAP
- Encapsulation de paquets IP
- Handshake maison (clé publique ↔ clé publique)
- Rotation de clés simple
- Cookies anti‑DoS
- Routage minimal
- Multi‑clients basique

### 📚 Documentation incluse N2

- Architecture du protocole
- Schéma du handshake
- Explication du routage
- Comparaison avec le niveau 1
- Limites du niveau 2

### 🎥 Démonstration vidéo N2

- Ping via le tunnel
- Curl via le tunnel
- Logs handshake
- Rotation de clé

### 🧭 Ce que j’ai appris N2

- Interfaces réseau virtuelles
- Handshake cryptographique
- Gestion de clés publiques
- Routage interne
- Sécurité protocolaire

---

## 🟥 Niveau 3 — VPN avancé (quasi‑pro)

### 🎯 Objectif du niveau N3

Créer un protocole complet, avec API d’administration et interface utilisateur.

### 🔧 Fonctionnalités N3

- Protocole complet
- Gestion des sessions
- ACL simples
- API Flask d’administration
- Interface React (dashboard)
- Monitoring minimal
- Tests réseau
- Comparaison avec WireGuard

### 📚 Documentation incluse N3

- Architecture complète
- Analyse de sécurité
- Analyse des limites
- Roadmap future

### 🎥 Démonstration vidéo N3

- Dashboard
- Connexion d’un client
- Monitoring
- ACL
- Logs

### 🧭 Ce que j’ai appris en N3

- Architecture réseau avancée
- API REST
- UI/UX technique
- Monitoring réseau
- Comparaison protocolaire

---

## 🌐 Intégration dans le site portfolio

### 🔧 Fonctionnement technique

Le site React interroge une API Flask qui renvoie :

- le README.md du projet
- les images
- les vidéos
- les schémas
- les catégories
- les liens GitHub

### 🎨 Interface utilisateur

- Menu de catégories (boutons bascule)
- Menu de sélection du niveau (1, 2, 3)
- Affichage dynamique du contenu
- Intégration vidéo
- Code extrait commenté
- Schémas SVG

### 🧭 Valeur ajoutée

Ce projet démontre :

- ma capacité à concevoir un protocole réseau
- ma compréhension de la cryptographie appliquée
- ma maîtrise du bas niveau
- ma capacité à documenter et transmettre
- ma progression versionnée et démontrée
