#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Fichier: test_data.py
# Auteur: Marc COATANHAY

"""
    Tests pour le module csvdata.
"""

# Import des modules
from data import *
import unittest

# Définitions constantes et variables globales

# Définitions fonctions et classes
class CsvTest(unittest.TestCase):
    def test_initCsv(self):
        afficher_calculs = False
        reponses = ["01/01/2020", "07:20", "302°18'", "11:47:26", "22°54'",
                        "16:14", "57°44'"]
        resultats = []
        lever_coucher = Csv(7, [0,1,2,3,4,5,6])
        for i in range(0,7):
            resultats.append(lever_coucher.donnees[i][0])
        if(afficher_calculs):
            print(lever_coucher)
        self.assertEqual(reponses, resultats)

if (__name__ == "__main__"):
    unittest.main()