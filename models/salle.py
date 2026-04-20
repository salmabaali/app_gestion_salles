class Salle:
    pass
class Salle:
    def __init__(self, code, description, categorie, capacite):
        self.code = code
        self.description = description
        self.categorie = categorie
        self.capacite = capacite

    def afficher_infos(self):
        return f"Salle {self.code} | {self.description} | {self.categorie} | Capacité: {self.capacite}"

    def __str__(self):
        return self.afficher_infos()