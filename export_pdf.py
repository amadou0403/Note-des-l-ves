"""
Projet : Relevé de Notes des Élèves
Auteur : Amadou Dème
Année : 2026
Description : Export des relevés de notes en PDF
"""

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from database import create_connection, close_connection
from tkinter import simpledialog, messagebox

def export_pdf():
    matricule = simpledialog.askstring("Export PDF", "Entrer le matricule de l'élève :")
    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM eleves WHERE matricule=%s", (matricule,))
        result = cursor.fetchone()
        cursor.close()
        close_connection(conn)

        if not result:
            messagebox.showwarning("Erreur", "Élève non trouvé !")
            return

        # Création du PDF
        file_name = f"{result[3]}_{result[1]}_{result[2]}_releve.pdf"
        c = canvas.Canvas(file_name, pagesize=A4)
        c.setFont("Helvetica-Bold", 20)
        c.drawString(180, 800, "Relevé de Notes des Élèves")

        c.setFont("Helvetica", 14)
        c.drawString(50, 750, f"Nom : {result[1]}")
        c.drawString(50, 730, f"Prénom : {result[2]}")
        c.drawString(50, 710, f"Classe : {result[3]}")
        c.drawString(50, 690, f"Matricule : {result[4]}")
        c.drawString(50, 670, f"Date inscription : {result[9]}")

        c.drawString(50, 630, f"Mathématiques : {result[5]}")
        c.drawString(50, 610, f"Français : {result[6]}")
        c.drawString(50, 590, f"Anglais : {result[7]}")
        c.drawString(50, 570, f"Moyenne générale : {result[8]}")

        c.save()
        messagebox.showinfo("Succès", f"Relevé PDF créé : {file_name}")
