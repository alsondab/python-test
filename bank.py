
class CompteBancaire:
    def __init__(self, numero_compte, nom, solde):
        self.numero_compte = numero_compte
        self.nom = nom
        self.solde = solde

    def versement(self, montant):
        self.solde += montant
        print(f"Versement de {montant} effectué. Nouveau solde : {self.solde}")

    def retrait(self, montant):
        if self.solde >= montant:
            self.solde -= montant
            print(f"Retrait de {montant} effectué. Nouveau solde : {self.solde}")
        else:
            print("Solde insuffisant pour effectuer le retrait.")

    def agios(self):
        agios = self.solde * 0.05
        self.solde -= agios
        print(f"Agios de {agios} appliqués. Nouveau solde : {self.solde}")

    def afficher(self):
        print(f"Numéro de compte : {self.numero_compte}")
        print(f"Propriétaire du compte : {self.nom}")
        print(f"Solde du compte : {self.solde}")



a= int(input("Enter Num Cpompt"))
b= str(input("Enter Nom"))
c= int(input("Enter ur solde"))
compte1 = CompteBancaire(a,b,c)

d= int(input("Enter amount of deposite "))
compte1.versement(d)

e= int(input("Enter amount u want "))
compte1.retrait(e)

compte1.agios()
compte1.afficher()