import time

import os

import pynput
from pynput.keyboard import Key, Controller

keyboard = Controller()

variables = {}

commande = 'start cmd'

pip = "pip "
install = "install "

nombre_variables = int(input("Nombre de bibliothèques à installer : "))

for i in range(1, nombre_variables + 1):
    nom_variable = "library_" + str(i)
    valeur_variable = input(f"nom de la library pour {nom_variable} : ")
    variables[nom_variable] = valeur_variable

for nom_variable, contenu_variable in variables.items():
    
    os.system(commande)

    time.sleep(1)

    keyboard.type(pip)
    keyboard.type(install)
    keyboard.type(contenu_variable)

    time.sleep(1)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    time.sleep(30)

    keyboard.press(Key.alt)
    keyboard.press(Key.f4)
    keyboard.release(Key.f4)
    keyboard.release(Key.alt)
