# Chiffrement symétrique — Plan d’apprentissage & Exercices

## 1. Introduction au chiffrement symétrique

- Définition et principe (chiffrement/déchiffrement avec une clé unique)
- Cas d’usage (VPN, stockage, messagerie)
- Avantages et limites

---

## 2. Les principaux algorithmes

- **AES (Advanced Encryption Standard)**
  - Présentation, tailles de clé (128, 192, 256 bits)
  - Modes de fonctionnement (ECB, CBC, GCM…)
- **ChaCha20**
  - Présentation, différences avec AES
  - Avantages (performance, sécurité sur matériel sans accélération AES)
- **Autres (en bref)**
  - DES (obsolète), 3DES, Blowfish, etc.

---

## 3. Gestion des clés partagées

- Génération d’une clé forte (aléatoire)
- Stockage sécurisé (fichier, variable d’environnement)
- Partage de clé (hors scope, mais mentionner l’importance)

---

## 4. Librairies Python pour le chiffrement

- `pycryptodome`
- `cryptography`
- Comparaison rapide, installation

---

## 5. Exercices pratiques

### Exercice 1 : Chiffrer et déchiffrer un message avec AES (mode CBC)

1. Installer `pycryptodome` ou `cryptography`.
   1. `python -m venv venv`
   2. `source venv/bin/activate` (Linux/macOS) ou `venv\Scripts\activate` (Windows)
   3. `pip install pycryptodome cryptography`
   4. `pip install --upgrade pip`
2. Générer une clé aléatoire de 256 bits.

   1. ```python
      from Crypto.Random import get_random_bytes
      key = get_random_bytes(32)  # 256 bits
      ```

3. Chiffrer une chaîne de caractères.

   1. ```python
        from Crypto.Cipher import AES
        from Crypto.Random import get_random_bytes

        # Clé et IV
        key = get_random_bytes(32)  # 256 bits
        iv = get_random_bytes(16)   # 128 bits pour AES

        # Chiffrement
        cipher = AES.new(key, AES.MODE_GCM, iv)
        message = b"Message secret a chiffrer"
        ciphertext, tag = cipher.encrypt_and_digest(message)
        print(f"Chiffré : {ciphertext.hex()}")
        print(f"Tag : {tag.hex()}")
        ```

4. Déchiffrer et vérifier que le message d’origine est retrouvé.

    1. ```python
        # Déchiffrement
        decipher = AES.new(key, AES.MODE_GCM, iv)
        decipher.update(b"")  # Si des données supplémentaires sont authentifiées
        decrypted = decipher.decrypt_and_verify(ciphertext, tag)
        print(f"Déchiffré : {decrypted.decode()}")
        ```

5. Expérimenter avec différents modes utilisant AEAD (CBC, GCM).
    1. GCM (Galois/Counter Mode)
        Chiffrement + authentification (AEAD)
        Rapide, très utilisé (TLS, VPN…)
        Authentifie aussi des données non chiffrées (AAD)
        Nonce/IV : unique, jamais réutilisé avec la même clé
        Tag d’authentification généré
    2. EAX
        Chiffrement + authentification (AEAD)
        Plus simple à implémenter que GCM
        Authentifie aussi des données non chiffrées (AAD)
        Nonce/IV : unique, mais plus tolérant que GCM
        Tag d’authentification généré
    3. CCM (Counter with CBC-MAC)
        Chiffrement + authentification (AEAD)
        Utilisé dans le standard IEEE 802.15.4 (IoT)
        Authentifie aussi des données non chiffrées (AAD)
        Nonce/IV : unique, taille stricte (7 à 13 octets)
        Plus lent que GCM/EAX
    4. SIV (Synthetic IV)
        Chiffrement + authentification (AEAD)
        Résistant à la réutilisation accidentelle du nonce (propriété « misuse-resistant »)
        Authentifie aussi des données non chiffrées (AAD)
        Peut réutiliser le même nonce sans compromettre la sécurité
        Plus lent, mais très sûr pour les usages critiques
    5. OCB (Offset Codebook)
        Chiffrement + authentification (AEAD)
        Très rapide, efficace
        Authentifie aussi des données non chiffrées (AAD)
        Nonce/IV : unique, jamais réutilisé avec la même clé
        Breveté (attention à l’utilisation commerciale)

#### 🧩 Les méthodes AEAD importantes

1. `update(data)`
    Authentifie des données non chiffrées (AAD).
    Equivalent à `update()` d’un HMAC.
    Toutes les données passées à `encrypt()` ou `decrypt()` sont automatiquement authentifiées.
2. `encrypt(plaintext)`
    Chiffre et authentifie le texte.
3. `decrypt(ciphertext)`
    Déchiffre mais ne valide pas encore l’authenticité.
4. `digest()`
    Produit le tag d’authentification (MAC tag).
5. `verify(tag)`
    Vérifie que le tag est correct.
    Lève ValueError si le message a été modifié ou si la clé/nonce est incorrecte.
6. `encrypt_and_digest(plaintext)`
    Effectue `encrypt()` + `digest()` en une seule opération.

### Exercice 2 : Chiffrer un fichier avec ChaCha20

1. Générer une clé et un nonce.

    ```python
    from Crypto.Cipher import ChaCha20
    from Crypto.Random import get_random_bytes

    key = get_random_bytes(32)  # 256 bits
    nonce = get_random_bytes(12)  # 96 bits
    ```

2. Chiffrer le contenu d’un fichier texte.

    ```python
    cipher = ChaCha20.new(key=key, nonce=nonce)
    with open("fichier.txt", "rb") as f:
        plaintext = f.read()
    ciphertext = cipher.encrypt(plaintext)  # type: ignore
    with open("fichier_chiffre.txt", "wb") as f:
        f.write(ciphertext)  # type: ignore
    print("Fichier chiffré avec ChaCha20.")
    ```

3. Déchiffrer et vérifier l’intégrité.

    ```python
    decipher = ChaCha20.new(key=key, nonce=nonce)
    with open("fichier_chiffre.txt", "rb") as f:
        ciphertext = f.read()
    decrypted = decipher.decrypt(ciphertext)  # type: ignore
    with open("fichier_dechiffre.txt", "wb") as f:
        f.write(decrypted)
    print("Fichier déchiffré avec ChaCha20.")
    ```

### Exercice 3 : Manipulation des erreurs

- Que se passe-t-il si la clé ou le nonce est incorrect ?
  - Le déchiffrement produit des données incorrectes.
- Que se passe-t-il si le message est modifié ?
  - avec chacha20 : le déchiffrement produit des données incorrectes.
  - avec chacha20-Poly1305 : une exception est levée lors de la vérification du tag d’authentification.
    - ```Erreur d'intégrité détectée : MAC check failed```

### Exercice 4 : Sécurité des clés

#### Générer et sauvegarder une clé dans un fichier sécurisé

```python
from Crypto.Random import get_random_bytes
import os

# Génération de la clé
key = get_random_bytes(32)  # 256 bits pour ChaCha20/AES

# Sauvegarde dans un fichier binaire
with open("ma_cle.key", "wb") as f:
    f.write(key)

# (Optionnel) Restreindre les permissions du fichier (Linux)
os.chmod("ma_cle.key", 0o600)  # Lecture/écriture uniquement pour le propriétaire
```

#### Lecture de la clé depuis le fichier pour chiffrer/déchiffrer

```python
with open("ma_cle.key", "rb") as f:
    key = f.read()
# Utiliser 'key' pour initialiser le cipher
```

**Bonnes pratiques** :

- Ne jamais stocker la clé en clair dans le code source.
- Protéger le fichier de clé (permissions, stockage hors du répertoire public).
- Utiliser un gestionnaire de secrets pour les projets professionnels :
  - HashiCorp Vault,
  - AWS KMS,
  - Azure Key Vault,
  - Google Cloud KMS,
  - Pass pour les environnements locaux.

---

## 6. Pour aller plus loin

- Liens vers la doc officielle des librairies
  - [PyCryptodome](https://www.pycryptodome.org/src/cipher/aes)
  - [Cryptography](https://cryptography.io/en/latest/)
- Bonnes pratiques (jamais réutiliser un IV/nonce, ne jamais stocker la clé en clair, gérer les droits d’accès)
- Introduction rapide à la cryptographie asymétrique (pour le partage de clé)

---

## 7. Ressources complémentaires

- [PyCryptodome documentation](https://www.pycryptodome.org/src/cipher/aes)
- [Cryptography documentation](https://cryptography.io/en/latest/)
- [OWASP — Cryptographic Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html)

---

> ***Objectif*** : Comprendre et expérimenter le chiffrement symétrique en Python, prêt à l’intégrer dans un tunnel VPN minimaliste.
