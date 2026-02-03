1"""
Projet : Relevé de Notes des Élèves
Auteur : Amadou Dème
Année : 2026
Description : Connexion à la base de données MySQL
"""

import mysql.connector
from mysql.connector import Error
from tkinter import messagebox

# Configuration de la base de données
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "TON_MOT_DE_PASSE_MYSQL",  # Remplace par ton vrai mot de passe
    "database": "releve_notes"
}

def create_connection():
    """Créer une connexion à la base de données MySQL"""
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        if connection.is_connected():
            print("Connexion MySQL réussie")
            return connection
    except Error as e:
        messagebox.showerror("Erreur MySQL", f"Erreur de connexion : {e}")
        return None

def close_connection(connection):
    """Fermer la connexion à la base de données"""
    if connection and connection.is_connected():
        connection.close()
        print("Connexion MySQL fermée")

def create_table():
    """Créer la table élèves si elle n'existe pas"""
    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS eleves (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nom VARCHAR(100),
            prenom VARCHAR(100),
            classe VARCHAR(50),
            matricule VARCHAR(50),
            math DECIMAL(5,2),
            francais DECIMAL(5,2),
            anglais DECIMAL(5,2),
            moyenne DECIMAL(5,2),
            date_inscription DATE
        )
        """)
        conn.commit()
        cursor.close()
        close_connection(conn)
