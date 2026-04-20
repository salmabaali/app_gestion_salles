
import customtkinter as ctk
from models.salle import Salle
from services.services_salle import ServiceSalle


class ViewSalle(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.title("Gestion des salles")

        self.geometry("520x420")

        self.service_salle = ServiceSalle()


        self.cadre_info = ctk.CTkFrame(self)
        self.cadre_info.pack(pady=10, padx=10, fill="x")

        ctk.CTkLabel(self.cadre_info, text="Code salle").grid(row=0, column=0, padx=5, pady=5)
        self.input_code = ctk.CTkEntry(self.cadre_info)
        self.input_code.grid(row=0, column=1, padx=5, pady=5)


        ctk.CTkLabel(self.cadre_info, text="Description").grid(row=1, column=0, padx=5, pady=5)
        self.input_desc = ctk.CTkEntry(self.cadre_info)
        self.input_desc.grid(row=1, column=1, padx=5, pady=5)

        ctk.CTkLabel(self.cadre_info, text="Catégorie").grid(row=2, column=0, padx=5, pady=5)
        self.input_cat = ctk.CTkEntry(self.cadre_info)
        self.input_cat.grid(row=2, column=1, padx=5, pady=5)
        ctk.CTkLabel(self.cadre_info, text="Capacité").grid(row=3, column=0, padx=5, pady=5)
        self.input_cap = ctk.CTkEntry(self.cadre_info)
        self.input_cap.grid(row=3, column=1, padx=5, pady=5)


        self.cadre_actions = ctk.CTkFrame(self)
        self.cadre_actions.pack(pady=10)

        self.btn_ajouter = ctk.CTkButton(self.cadre_actions, text="Ajouter salle", command=self.ajouter_salle)
        self.btn_ajouter.grid(row=0, column=0, padx=5)

        self.btn_modifier = ctk.CTkButton(self.cadre_actions, text="Modifier salle", command=self.modifier_salle)
        self.btn_modifier.grid(row=0, column=1, padx=5)

        self.btn_supprimer = ctk.CTkButton(self.cadre_actions, text="Supprimer salle", command=self.supprimer_salle)
        self.btn_supprimer.grid(row=0, column=2, padx=5)

        self.btn_rechercher = ctk.CTkButton(self.cadre_actions, text="Rechercher salle", command=self.rechercher_salle)
        self.btn_rechercher.grid(row=0, column=3, padx=5)

    def ajouter_salle(self):
        try:
            salle = Salle(
                self.input_code.get(),
                self.input_desc.get(),
                self.input_cat.get(),
                int(self.input_cap.get())
            )

            success, msg = self.service_salle.ajouter_salle(salle)
            print(f"[INFO] Résultat ajout : {msg}")
            self.input_code.delete(0, "end")
            self.input_desc.delete(0, "end")
            self.input_cat.delete(0, "end")
            self.input_cap.delete(0, "end")

        except:
            print("Erreur : vérifiez la capacité (nombre requis)")

    def modifier_salle(self):
        try:
            salle = Salle(
                self.input_code.get(),
                self.input_desc.get(),
                self.input_cat.get(),
                int(self.input_cap.get())
            )

            success, msg = self.service_salle.modifier_salle(salle)
            print(f"[INFO] Modification : {msg}")

        except:
            print("Erreur lors de la modification")

    def supprimer_salle(self):
        code = self.input_code.get()
        msg = self.service_salle.supprimer_salle(code)
        print("Suppression :", msg)

    def rechercher_salle(self):
        code = self.input_code.get()
        salle = self.service_salle.rechercher_salle(code)

        if salle:
            self.input_desc.delete(0, "end")
            self.input_desc.insert(0, salle.description)

            self.input_cat.delete(0, "end")
            self.input_cat.insert(0, salle.categorie)

            self.input_cap.delete(0, "end")
            self.input_cap.insert(0, salle.capacite)

            print(f"Salle {code} trouvée et affichée")
        else:
            print("Aucune salle trouvée malheuresement :(")