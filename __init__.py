from flask import Flask, render_template, request, redirect, jsonify, json
import sqlite3
from urllib.request import urlopen

def get_db_connection():
    conn = sqlite3.connect('/home/jarry/www/flask/database.db')  # Remplacez 'database.db' par le chemin de votre base de données SQLite.
    conn.row_factory = sqlite3.Row  # Accès aux colonnes par nom.
    return conn
    
app = Flask(__name__) #creating flask app name

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/resume_1')
def resume_1():
    return render_template("resume_1.html")

@app.route('/resume_2')
def resume_2():
    return render_template("resume_2.html")

@app.route('/resume_template')
def resume_template():
    return render_template("resume_template.html")

# Création d'une nouvelle route pour la lecture de la BDD
@app.route("/consultation/")
def ReadBDD():
    conn = get_db_connection()  # Utilisation de la fonction définie pour la connexion
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM livres;')
    data = cursor.fetchall()
    conn.close()
    
    # Rendre le template HTML et transmettre les données
    return render_template('read_data.html', data=data)

if(__name__ == "__main__"):
    app.run()
