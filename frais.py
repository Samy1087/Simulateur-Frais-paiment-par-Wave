def montant(montant):
    """Cette fonction permet d'appliquer un pourcentage à une somme lors d'une transaction."""
    frais_wave = 0.01
    frais_max = 5000
    frais = montant * frais_wave
    frais_en_dessous_de_700 = 5
    frais_au_dessus_de_700 = 10
    frais = min(frais, frais_max)
    if montant <= 700:
        print(f"Montant envoyé : {montant + frais_en_dessous_de_700}")
        print(f"Frais : {frais_en_dessous_de_700}")
        print(f"Montant reçu : {montant}")
    elif montant >= 800 and montant <= 900:
        print(f"Montant envoyé : {montant + frais_au_dessus_de_700}")
        print(f"Frais : {frais_au_dessus_de_700}")
        print(f"Montant reçu : {montant}")
    else:
        print(f"Montant envoyé : {montant + frais}")
        print(f"Frais : {frais}")
        print(f"Montant reçu : {montant}")

def principal():
    """Fonction principale avec gestion d'erreur."""
    try :
        montant_entree = int(input("Veuillez saisir un montant : "))
        montant(montant_entree)
    except ValueError:
        print("Veuillez saisir un nombre valide !")
    except Exception as e :
        print(f"Erreur inattendue : {e}")
    
# Le programme démarre ici.

if __name__ == '__main__':
    principal()
