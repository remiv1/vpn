# WORKFLOW — Niveau 2 : VPN réaliste

## 1. Initialisation

- Démarrer le serveur VPN (création interface TUN/TAP, écoute handshake)
- Démarrer le(s) client(s) VPN (création interface TUN/TAP, préparation handshake)

## 2. Handshake

- Échange de clés publiques entre client et serveur
- Vérification et acceptation (cookie anti-DoS)
- Établissement du canal sécurisé

## 3. Transmission de paquets

- Capture des paquets IP sur l’interface TUN/TAP
- Encapsulation et chiffrement
- Transmission via UDP/TCP
- Désencapsulation côté distant et injection dans TUN/TAP

## 4. Rotation de clés

- Déclenchement périodique ou sur événement
- Échange de nouvelles clés publiques
- Mise à jour des clés de session

## 5. Routage

- Redirection des paquets IP selon la table de routage minimale
- Gestion multi-clients (identification, routage)

## 6. Sécurité

- Surveillance des cookies anti-DoS
- Logs des handshakes et rotations de clés

## 7. Tests et validation

- Ping à travers le tunnel
- Curl à travers le tunnel
- Vérification des logs
- Test de la rotation de clé

## 8. Documentation

- Mise à jour de la documentation technique et des schémas
- Comparaison avec le niveau 1
- Analyse des limites et axes d’amélioration
