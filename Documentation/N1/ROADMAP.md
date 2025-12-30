# 🗺️ Roadmap — Mini‑VPN Minimaliste (Niveau 1)

## ⏳ Planning & Timing

| Étape                        | Description                                      | Durée estimée | Fait |
|------------------------------|--------------------------------------------------|---------------|------|
| Prise en main UDP            | Comprendre les sockets UDP en Python             | 0,5 jour      |  X   |
| Chiffrement symétrique       | Étudier AES/ChaCha20, clé partagée, libs Python  | 1 jour        |  X   |
| Tunnel logique               | Concevoir l'encapsulation/décapsulation          | 0,5 jour      |      |
| Développement Serveur        | Implémenter serveur UDP + déchiffrement          | 1 jour        |  X   |
| Développement Client         | Implémenter client UDP + chiffrement             | 1 jour        |  X   |
| Tests & Démo                 | Tester, démontrer, corriger                      | 0,5 jour      |      |
| Logs & CLI                   | Ajouter logs, interface ligne de commande        | 0,5 jour      |      |
| Documentation                | Rédiger docs, schémas, explications              | 0,5 jour      |      |

> **Total estimé : 5,5 jours**

## 📚 Connaissances à développer

- [X] Sockets UDP en Python (envoi/réception, non connecté)
- [X] Chiffrement symétrique (AES ou ChaCha20, modes, padding)
- [X] Gestion de clés partagées (génération, stockage sécurisé)
- [ ] Encapsulation/décapsulation de messages
- [ ] Structure d’un tunnel réseau logique
- [ ] Logging et bonnes pratiques CLI
- [ ] Tests unitaires et manuels
- [ ] Documentation technique claire

## 🛠️ Compétences à acquérir

- Programmation réseau bas niveau (UDP)
- Utilisation de bibliothèques de cryptographie (pycryptodome, cryptography)
- Sécurisation d’un échange de données
- Structuration d’un projet Python modulaire
- Rédaction de documentation pédagogique
- Démonstration technique (vidéo, CLI)

## 🎯 Objectif final

Avoir un tunnel chiffré fonctionnel, documenté, démontré, et compréhensible par un public technique débutant.

## 📦 Livrables

- Code source complet
  - client UDP minimaliste
  - serveur UDP minimaliste
  - module de chiffrement/déchiffrement
  - module d’encapsulation/décapsulation
  - scripts d’automatisation pour le déploiement rapide
- Documentation technique
  - architecture
  - explications (chiffrement, tunnel)
  - limites
  - notes d’évolution et pistes d’amélioration
  - exemples d’utilisation en ligne de commande
  - guide d’installation et d’utilisation
  - fichier README détaillé pour le projet Niveau 1
  - liste des dépendances et instructions d’installation
  - FAQ pour les problèmes courants rencontrés
  - comparaison avec un VPN complet (avantages/inconvénients)
- Vidéo de démonstration
  - lancement serveur
  - lancement client
  - envoi/réception messages chiffrés
- Tests unitaires et manuels
