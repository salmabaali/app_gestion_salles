import json
import mysql.connector
from models.salle import Salle


class DataSalle:

    def get_connection(self):
        with open("Data/config.json") as f:
            config = json.load(f)

        conn = mysql.connector.connect(
            host=config["host"],
            user=config["user"],
            password=config["password"],
            database=config["database"]
        )
        return conn

    def insert_salle(self, salle):
        conn = self.get_connection()
        cursor = conn.cursor()

        query = "INSERT INTO salle (code, description, categorie, capacite) VALUES (%s, %s, %s, %s)"
        values = (salle.code, salle.description, salle.categorie, salle.capacite)

        cursor.execute(query, values)
        conn.commit()

        cursor.close()
        conn.close()

    def get_salles(self):
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM salle")
        results = cursor.fetchall()

        cursor.close()
        conn.close()

        return [Salle(*row) for row in results]