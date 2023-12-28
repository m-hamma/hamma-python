# Python ne tient pas compte des croisillons # qui pr�c�dent les commentaires !
# Ce script est �crit avec l'�diteur du plugin PyDev sous Eclipse et Linux Mint 18.3.
# Les lignes 8 et 9 indiquent au fichier '1erModule.py' le chemin absolu de l'interpr�teur
# Python 3.5 sous Linux Mint 18.3 et l'encodage du texte.
# Dans le cas de Eclipse/PyDev, ils ne sont pas vraiment n�cessaires !
#!/usr/bin/python3.5 # Ici un cas particulier du # et Python le prend en compte !
# -*-coding:UTF-8 -* # Ici un cas particulier du # et Python le prend en compte !
# FONCTION Utilisateur calculant la Table de Multiplication par nb de 1*nb � maxi*nb.
def table(nb, maxi): # D�BUT du programme
    i = 0 # Le compteur i avec valeur 0 au d�part
    while i < maxi: # Tant que i est strictement inf�rieur � la variable maxi
        print(i + 1, '*', nb, '=', (i + 1) * nb) # Pour afficher le r�sultat des calculs
        i += 1 # Incr�mentation i de 1 � chaque tour de boucle
# POUR LANCER CE SCRIPT en 2 �tapes :
#   le curseur �tant dans l'�diteur, pressez CTRL+ALT+ENTER puis choisissez
#   la Console � utiliser, et � nouveau dans l'�diteur CRTL+ALT+ENTER.
#   La Console attend maintenant vos entr�es de table...
print("-Lorsque vous verrez ci-dessous les 3 chevrons de Python, entrez votre table de multiplication sous la forme table(nb, maxi) et validez par Entrée.")

# Par exemple table(76, 10) va vous afficher la table des 76, de 1x76=76 jusqu'� 10x76=760.
#- � chaque apparition des 3 chevrons vous pouvez recommencer avec une nouvelle table.
#- Pour fermer le programme, cliquez dans la Console sur le Bouton rouge ci-dessus (Terminate current console).")
# FIN du programme