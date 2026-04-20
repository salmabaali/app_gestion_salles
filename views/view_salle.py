import customtkinter as ctk
from models.salle import Salle
from services.services_salle import ServiceSalle
from tkinter import messagebox


class ViewSalle(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Gestion des salles")
        self.geometry("540x430")

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

        self.btn_ajouter = ctk.CTkButton(self.cadre_actions, text="Ajouter", command=self.ajouter_salle)
        self.btn_ajouter.grid(row=0, column=0, padx=5)

        self.btn_modifier = ctk.CTkButton(self.cadre_actions, text="Modifier", command=self.modifier_salle)
        self.btn_modifier.grid(row=0, column=1, padx=5)

        self.btn_supprimer = ctk.CTkButton(self.cadre_actions, text="Supprimer", command=self.supprimer_salle)
        self.btn_supprimer.grid(row=0, column=2, padx=5)

        self.btn_rechercher = ctk.CTkButton(self.cadre_actions, text="Rechercher", command=self.rechercher_salle)
        self.btn_rechercher.grid(row=0, column=3, padx=5)

        self.zone_affichage = ctk.CTkTextbox(self, height=120)
        self.zone_affichage.pack(pady=10, padx=10, fill="x")



    def ajouter_salle(self):
        try:
            salle = Salle(
                self.input_code.get(),
                self.input_desc.get(),
                self.input_cat.get(),
                int(self.input_cap.get())
            )

            success, msg = self.service_salle.ajouter_salle(salle)

            if success:
                messagebox.showinfo("Succès", msg)
            else:
                messagebox.showerror("Erreur", msg)

        except:
            messagebox.showerror("Erreur", "Veuillez entrer une capacité valide")






    def modifier_salle(self):
        try:
            salle = Salle(
                self.input_code.get(),
                self.input_desc.get(),
                self.input_cat.get(),
                int(self.input_cap.get())
            )

            success, msg = self.service_salle.modifier_salle(salle)

            if success:
                messagebox.showinfo("Modification", msg)
            else:
                messagebox.showerror("Erreur", msg)

        except:
            messagebox.showerror("Erreur", "Erreur lors de la modification")








    def supprimer_salle(self):
        code = self.input_code.get()
        self.service_salle.supprimer_salle(code)

        self.zone_affichage.insert("end", "\nSalle supprimée")


    def rechercher_salle(self):
        code = self.input_code.get()
        salle = self.service_salle.rechercher_salle(code)

        self.zone_affichage.delete("1.0", "end")

        if salle:
            self.zone_affichage.insert(
                "end",
                f"{salle.code} | {salle.description} | {salle.categorie} | {salle.capacite}"
            )
        else:
            self.zone_affichage.insert("end", "Aucune salle trouvée")