"""
Projet : Relevé de Notes des Élèves
Auteur : Amadou Dème
Année : 2026
Description : Gestion de la connexion Admin / Utilisateur
"""

import tkinter as tk
from tkinter import messagebox

# Utilisateurs et mots de passe (exemple académique)
USERS = {
    "admin": "Admin@2026",  # accès complet
    "user": "User@2026"     # accès limité
}

def login_screen(parent):
    login_win = tk.Toplevel(parent)
    login_win.title("Connexion")
    login_win.geometry("400x300")
    login_win.resizable(False, False)

    tk.Label(login_win, text="Nom d'utilisateur :", font=("Arial", 12)).pack(pady=10)
    username_entry = tk.Entry(login_win, font=("Arial", 12))
    username_entry.pack()

    tk.Label(login_win, text="Mot de passe :", font=("Arial", 12)).pack(pady=10)
    password_entry = tk.Entry(login_win, font=("Arial", 12), show="*")
    password_entry.pack()

    def check_login():
        username = username_entry.get()
        password = password_entry.get()

        if username in USERS and USERS[username] == password:
            messagebox.showinfo("Connexion réussie", f"Bienvenue {username} !")
            login_win.destroy()
        else:
            messagebox.showerror("Erreur", "Nom d'utilisateur ou mot de passe incorrect")

    tk.Button(login_win, text="Se connecter", font=("Arial", 12), command=check_login).pack(pady=20)
