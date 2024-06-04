'''def hello_wolrd ():
    nom_person=input("Enter your name :")
    age_personne=int(input("Enter your Age :"))
    return nom_person,age_personne
    
nom_person,age_personne=hello_wolrd()
print("Hi {} your're {} welcome to this university".format(nom_person,age_personne))'''

'''
def salut () :

    while True:
        try :
            nomP=str(input("Enter your name :"))
            ageP=int(input("Enter your name :"))
            print("Hello {} you're {}".format(nomP,ageP))
            print("You entered your credentials succesfully :) ")
            break
        except ValueError:
            print("verify if your credentials are correct !!")
        except Exception:
            print("An unexpected error occured please try again !")
    return nomP,ageP

salut()   

'''

def salut () :
    while True :
        try :
            name = str (input("Enter your name : "))
            age = int(input("Enter your age : "))
            print(f"hi {name} you're {age}")
            print("success!!")
            break
        except ValueError :
            print("Check if your credentials are correct and try again !!")
        except Exception :
            print("an unexpected error occured please try again !!")
    return name,age
    

