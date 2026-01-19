
# 🗺️ Roadmap — VPN réaliste (Niveau 2)

## ⏳ Planning & Timing

| Étape                     | Description                                  | Durée estimée | Fait |
|---------------------------|----------------------------------------------|---------------|------|
| Interface TUN/TAP         | Mise en place, configuration, tests          | 1 jour        |      |
| Encapsulation paquets IP  | Capture/injection, format, validation        | 1 jour        |      |
| Handshake maison          | Échange clés publiques, cookies anti-DoS     | 1 jour        |      |
| Rotation de clés          | Implémentation, tests de sécurité            | 0,5 jour      |      |
| Routage minimal           | Table de routage, multi-clients              | 1 jour        |      |
| Tests & Démo              | Ping, curl, logs, rotation de clé            | 0,5 jour      |      |
| Documentation & schémas   | Docs techniques, schémas, comparatif N1/N2   | 0,5 jour      |      |

> **Total estimé : 5,5 jours**

## 📚 Connaissances à développer

- Interfaces réseau virtuelles (TUN/TAP)
- Encapsulation/désencapsulation de paquets IP
- Handshake cryptographique (clé publique ↔ clé publique)
- Rotation de clés et gestion de sessions
- Cookies anti-DoS et sécurité protocolaire
- Routage interne et multi-clients
- Documentation technique et schémas

## 🛠️ Compétences à acquérir

- Programmation réseau avancée (TUN/TAP, routage)
- Sécurisation d’un protocole maison (handshake, cookies, rotation de clés)
- Gestion de plusieurs clients
- Analyse et documentation d’architecture réseau
- Démonstration technique (ping, curl, logs)

## 🎯 Objectif final

Mettre en place un tunnel VPN réaliste, chiffré, multi-clients, basé sur TUN/TAP, avec handshake sécurisé, rotation de clés, routage minimal, démontré et documenté.

## 📦 Livrables

- Code source complet
  - Serveur et client VPN avec TUN/TAP
  - Module d’encapsulation/désencapsulation IP
  - Handshake maison et rotation de clés
  - Gestion multi-clients et routage
  - Protection anti-DoS (cookies)
- Documentation technique
  - Architecture du protocole
  - Schéma du handshake
  - Explication du routage
  - Comparaison N1/N2
  - Limites du niveau 2
- Démonstration vidéo
  - Ping et curl via le tunnel
  - Logs handshake et rotation de clé
