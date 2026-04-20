from Data.dao_salle import DataSalle


class ServiceSalle:

    def __init__(self):
        self.dao_salle = DataSalle()

    def ajouter_salle(self, salle):
        if not salle.code or not salle.description or not salle.categorie:
            return False, "Veuillez remplir tous les champs obligatoires."

        if salle.capacite < 1:
            return False, "La capacité doit être supérieure à 0."

        self.dao_salle.insert_salle(salle)
        return True, f"Salle '{salle.code}' ajoutée avec succès."

    def modifier_salle(self, salle):
        if not salle.code or not salle.description or not salle.categorie:
            return False, "Informations incomplètes pour la modification."

        if salle.capacite < 1:
            return False, "La capacité doit être valide (>= 1)."

        self.dao_salle.update_salle(salle)
        return True, f"Salle '{salle.code}' mise à jour avec succès."

    def supprimer_salle(self, code):
        self.dao_salle.delete_salle(code)
        return f"Salle '{code}' supprimée."

    def rechercher_salle(self, code):
        salle = self.dao_salle.get_salle(code)
        if salle:
            return salle
        return None

    def recuperer_salles(self):
        return self.dao_salle.get_salles()