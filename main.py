"""
Projet : Relevé de Notes des Élèves
Auteur : Amadou Dème
Année : 2026
Description : Point d'entrée de l'application avec interface principale
"""

import tkinter as tk
from tkinter import messagebox
from auth import login_screen
from eleves import eleves_screen

# Fenêtre principale
root = tk.Tk()
root.title("Relevé de Notes des Élèves - Amadou Dème")
root.geometry("800x500")
root.resizable(False, False)

# Logo (si tu as un logo)
try:
    from tkinter import PhotoImage
    logo = PhotoImage(file="assets/logo.png")
    tk.Label(root, image=logo).pack(pady=10)
except:
    tk.Label(root, text="Relevé de Notes des Élèves", font=("Arial", 24, "bold")).pack(pady=20)

# Boutons
tk.Button(root, text="Connexion", font=("Arial", 16), width=20, command=lambda: login_screen(root)).pack(pady=10)
tk.Button(root, text="Gestion des Élèves", font=("Arial", 16), width=20, command=lambda: eleves_screen(root)).pack(pady=10)
tk.Button(root, text="Quitter", font=("Arial", 16), width=20, command=root.destroy).pack(pady=10)

root.mainloop()
