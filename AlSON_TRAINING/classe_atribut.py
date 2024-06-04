'''class UnHumain :
    """
    classe des etre humain
    """
    humain_creer = 0
#atribut de class napartien pas a un objet en particulier mais qui appartient a tout les objet on peut dire un attribut commun 
#E t on le cree dans la def de la class pas dans la fuction
    #notre constructeur
    def __init__(self,c_prenom,c_age=0):
        print("Creation d'humain")
        self.prenom = c_prenom
        self.age = c_age
        UnHumain.humain_creer += 1

#creer une instance/appeler une class. on cree une instance qui est stocker dans une var h1
h1 = UnHumain ("Ali")
print("nom= {}, age= {}".format(h1.prenom,h1.age))
print("Humain existant {}".format(UnHumain.humain_creer))

h2 = UnHumain("Nass",27)
print("nom= {}, age= {}".format(h2.prenom,h2.age))
print("Humain existant {}".format(UnHumain.humain_creer))

h3 = UnHumain ("MHD",25)
print("nom= {}, age= {}".format(h3.prenom,h3.age))
print("Humain existant {}".format(UnHumain.humain_creer))

#modifier atribut d'un objet
h1.prenom = "Kader" 
print("nom= {}, age= {}".format(h1.prenom,h1.age))
'''