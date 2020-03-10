#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Fichier: coordonnees.py
# Auteur: Marc COATANHAY
# Inspiré par le cours Python : magistère.education.fr

"""
    Charge les données d'un fichier csv dans un objet de class Csv.
    Les données se trouvent dans Csv.donnees sous forme de listes
    d'objets texte.
"""

from tkinter import Tk
from tkinter.filedialog import askopenfilename

class Csv:
    def __init__(
            self,
            nb_colonnes=0,
            liste_colonnes=[],
            nb_lignes_entete=1,
            fichier=""):
        if(nb_colonnes != 0):
            if fichier == "":
                root = Tk()
                name = askopenfilename(
                            parent=root,
                            filetypes=(
                                ("Fichier CSV", "*.csv"),
                                ("Fichier Texte", "*.txt"),
                                ("Tous les fichiers", "*.*")
                                    ),
                            title="Choisir un fichier")
                root.destroy()
            else:
                name = fichier

            # caractère séparateur du csv -peut être une virgule,
            # un point-virgule ou une tabulation notée \t
            sep = ";"

            if(name != ""):
                # Toutes les lignes du fichier sont récupérées dans
                # la variable data.
                f = open(name, "r")
                data = f.readlines()
                f.close()

                # on supprime les lignes d'en-tête qui ne nous intéressent pas
                data = data[nb_lignes_entete:]

                # On construit les listes de valeurs utiles
                self.donnees = []
                for i in range(nb_colonnes):
                    self.donnees.append([])

                # On remplit les les listes de valeurs utiles
                for ligne in data:
                    # on sépare les différents élément en utilisant
                    # le caractère séparateur défini
                    ligne = ligne.strip().split(sep)
                    # on rentre les valeurs dans les listes de valeurs utiles
                    for i in range(nb_colonnes):
                        self.donnees[i].append(ligne[liste_colonnes[i]])
                print("Les données sont en mémoire dans des listes python")
            else:
                print("Aucune donnée n'a été chargée")
        else:
            print("Aucune donnée n'a été chargée")

    def __repr__(self):
        return "{}".format(self.donnees)