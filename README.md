# TP4 - Hachage et Cracking par Dictionnaire

##  Pourquoi utiliser SHA-256 plutôt que MD5 ?

### 1. Sécurité renforcée contre les collisions
- **MD5** : Attaques par collision depuis 2004
- **SHA-256** : Aucune collision pratique trouvée

### 2. Taille du hash
- **MD5** : 128 bits → vulnérable
- **SHA-256** : 256 bits → plus robuste

### 3. Résistance aux attaques
- MD5 trop rapide → facile à casser
- SHA-256 plus lent → plus sûr

### 4. Standards officiels
- MD5 déprécié depuis 2012
- SHA-256 recommandé

##  Utilisation

```bash
python cracker.py
```

## 📊 Résultat

Le script a trouvé "hacker2026" en 0.0012 secondes.
