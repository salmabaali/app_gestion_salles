class DataSalle:
    pass
from models.salle import Salle
def main():
    s1 = Salle("A1", "Salle info", "Laboratoire", 30)
    print(s1.afficher_infos())
if __name__ == "__main__":
    main()