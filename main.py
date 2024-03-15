import json


# Récupération et stockage des données

def recuperation_fichier():
    
    with open('etudiants.json') as f:
        donnees = json.load(f)
        
    return donnees


# Réécriture des données dans le fichier JSON

def sauvegarder_eleve(eleves):
    
    with open('etudiants.json', 'w') as f:
        json.dump(eleves, f, indent=2)
        

# Ajout d'un nouvel élève

def ajouter_eleve(nom, prenom, classe):
    
    eleves = recuperation_fichier()

    eleves.append({"nom": nom, "prenom": prenom, "classe": classe})
    
    sauvegarder_eleve(eleves)
  

# Suppression d'un élève via son nom et son prénom    

def supprimer_eleve(nom, prenom):
    
    eleves = recuperation_fichier()
    
    eleves = [(eleve for eleve in eleves if not (eleve['nom'] == nom and eleve['prenom'] == prenom))]
    
    sauvegarder_eleve(eleves)


# Affichage des données de tous les élèves

def afficher_eleve():
    
    eleves = recuperation_fichier()
    for i in eleves:
        print(". ", i['nom'], i['prenom'], "  -  ", i['classe'])


# Affichage du menu

def affichage_menu():
    
    print("- Ajouter un élève : ajouter Nom Prenom Classe")
    print("- Supprimer un élève : supprimer Nom Prenom")
    print("- Afficher les données : afficher")
    print("- Quitter le programme : quitter")
 
 
# Message d'erreur

def affichage_syntaxe_non_correcte():
    
     print("Veuillez suivre le format demandé") 


# Saisie de la commande

def saisie_utilisateur():
    
    entree = str(input("Votre choix : ")).split()
    return entree


# Menu qui guide l'utilisateur en fonction de sa demande

def menu_principal():
    
    while True:
        
        affichage_menu()
        
        rep = saisie_utilisateur()
     
        if rep[0] == "ajouter":
         
            if len(rep) == 4 :     
                nom = rep[1]
                prenom = rep[2]
                classe = rep[3]
                ajouter_eleve(nom, prenom, classe)
            else : 
                affichage_syntaxe_non_correcte()

        elif rep[0] == "supprimer":
            
            if len(rep) == 3 :
                nom = rep[1]
                prenom = rep[2]
                supprimer_eleve(nom, prenom)
            else:
                affichage_syntaxe_non_correcte()

        elif rep[0] == "afficher":
            
            if len(rep) == 1:
                afficher_eleve()
            else:
                affichage_syntaxe_non_correcte()

        elif rep[0] == "quitter":
            break

        else:
            print("Choix non valide. Veuillez choisir un numéro valide.")


if __name__ == "__main__":
    
    print("Bienvenue ! Les fonctionnalités disponibles :")
    
    menu_principal()
    
    
    
