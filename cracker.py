import hashlib
import time

def hash_password(password):
    """Prend un mot de passe en clair et retourne son hash SHA-256."""
    encoded_pass = password.encode('utf-8')
    hash_obj = hashlib.sha256(encoded_pass)
    return hash_obj.hexdigest()

def crack_hash(target_hash, dictionary_file):
    """Tente de trouver le mot de passe correspondant au hash donné."""
    print(f"[*] Début de l'attaque sur le hash : {target_hash[:10]}...")
    
    try:
        with open(dictionary_file, 'r') as file:
            for word in file:
                clean_word = word.strip()
                word_hash = hash_password(clean_word)
                
                if word_hash == target_hash:
                    print(f"\n[+] SUCCÈS ! Mot de passe trouvé : '{clean_word}'")
                    return True
                    
        print("\n[-] Échec. Le mot de passe n'est pas dans le dictionnaire.")
        return False
        
    except FileNotFoundError:
        print("[-] Erreur : Fichier dictionnaire introuvable.")

if __name__ == "__main__":
    stolen_hash = "f11a4f02a9ebf5cc43e3ef7ff3deef2c56a7de7e5cfa5bd1adfb836e5cc18c64"
    
    print("--- OUTIL DE CRACKING ---")
    start_time = time.time()
    
    crack_hash(stolen_hash, "dico.txt")
    
    end_time = time.time()
    print(f"[*] Durée de l'opération : {round(end_time - start_time, 4)} secondes.")
