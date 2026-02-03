"""
Projet : Relevé de Notes des Élèves
Auteur : Amadou Dème
Année : 2026
Description : Gestion des élèves (CRUD + calcul moyenne)
"""

import tkinter as tk
from tkinter import messagebox, simpledialog
from database import create_connection, close_connection
import datetime

def eleves_screen(parent):
    eleves_win = tk.Toplevel(parent)
    eleves_win.title("Gestion des élèves")
    eleves_win.geometry("900x600")
    eleves_win.resizable(False, False)

    tk.Label(eleves_win, text="Gestion des élèves", font=("Arial", 20, "bold")).pack(pady=10)

    # Fonction pour ajouter un élève
    def add_student():
        nom = simpledialog.askstring("Nom", "Nom de l'élève :")
        prenom = simpledialog.askstring("Prénom", "Prénom de l'élève :")
        classe = simpledialog.askstring("Classe", "Classe :")
        matricule = simpledialog.askstring("Matricule", "Matricule :")
        math = simpledialog.askfloat("Math", "Note en Mathématiques :")
        francais = simpledialog.askfloat("Français", "Note en Français :")
        anglais = simpledialog.askfloat("Anglais", "Note en Anglais :")
        moyenne = round((math + francais + anglais)/3, 2)
        date_inscription = datetime.date.today()

        conn = create_connection()
        if conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO eleves (nom, prenom, classe, matricule, math, francais, anglais, moyenne, date_inscription)
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """, (nom, prenom, classe, matricule, math, francais, anglais, moyenne, date_inscription))
            conn.commit()
            cursor.close()
            close_connection(conn)
            messagebox.showinfo("Succès", f"Élève {nom} {prenom} ajouté avec succès !")

    # Fonction pour rechercher un élève par matricule
    def search_student():
        matricule = simpledialog.askstring("Recherche", "Entrer le matricule de l'élève :")
        conn = create_connection()
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM eleves WHERE matricule=%s", (matricule,))
            result = cursor.fetchone()
            cursor.close()
            close_connection(conn)
            if result:
                info = f"Nom : {result[1]}\nPrénom : {result[2]}\nClasse : {result[3]}\nMath : {result[5]}\nFrançais : {result[6]}\nAnglais : {result[7]}\nMoyenne : {result[8]}\nDate inscription : {result[9]}"
                messagebox.showinfo("Résultat", info)
            else:
                messagebox.showwarning("Erreur", "Élève non trouvé !")

    # Fonction pour supprimer un élève
    def delete_student():
        matricule = simpledialog.askstring("Suppression", "Entrer le matricule de l'élève à supprimer :")
        conn = create_connection()
        if conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM eleves WHERE matricule=%s", (matricule,))
            conn.commit()
            cursor.close()
            close_connection(conn)
            messagebox.showinfo("Succès", f"Élève avec matricule {matricule} supprimé !")

    # Boutons
    tk.Button(eleves_win, text="Ajouter un élève", font=("Arial", 14), width=20, command=add_student).pack(pady=10)
    tk.Button(eleves_win, text="Rechercher un élève", font=("Arial", 14), width=20, command=search_student).pack(pady=10)
    tk.Button(eleves_win, text="Supprimer un élève", font=("Arial", 14), width=20, command=delete_student).pack(pady=10)
