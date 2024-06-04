"""
methode d'instance : function sur une instance (objet)
methode de classe : function sur une classe
method de statique : function independent mais lier a une classe
"""
#classe qui definit un humain
class Humain :
    #instance de class
    humain_existant = 0
    Lieu_Habitat = "La terre"

    #constructeur
    def __init__ (self,nom,ans) : #self= methode dinstance
        self.nom = nom
        self.ans = ans
        Humain.humain_existant += 1

    #methode d'instance
    def parler (self,message) :
        print("{} a dit {} ".format(self.nom,message))

    #methode d'instance
    def changer_Habitat (cls,nouveau_habiat) :#cls= methode de class
        Humain.Lieu_Habitat = nouveau_habiat
    changer_Habitat = classmethod(changer_Habitat)

#programe principal
h1=Humain ("ali",22)
print("ton nom est {} et tu as {}ans ".format(h1.nom,h1.ans))
print("Nombre d'humain creer = {}  ".format(Humain.humain_existant))

h1.nom = "Nass"
print("ton nom est {} ".format(h1.nom))

h1.parler(":Bonjour a tous : ) ") 
h1.parler("What's up ") 

print("planette actuel {} ".format(Humain.Lieu_Habitat))

Humain.changer_Habitat ("Jupiter")

print("planette actuel {} ".format(Humain.Lieu_Habitat))