# fonction vue : print() <-pour afficher
#input()<- pour lire au clavier
#type()<- pour retourner le type d'une donnee
# str.format()<- formater une chaine 

#division
'''num1= int(input('Enter a num : '))
num2= int(input('Enter another num : '))
dev =  num1//num2
print ("the division of these nums =",dev)'''

#fonction format 
'''ageP=22
prixHT=2000.34
A_P="l'age de la personne est {}ans et le prix hors tax est {}fcf"
print(A_P.format(ageP,prixHT))'''
# print ("l'age de la personne est {}ans et le prix hors tax est {}fcf "format(ageP,prixHT))

'''nomJoueur= input("choose a name :")
print("bienvenu ," ,format(nomJoueur) )
print(type(nomJoueur))'''

'''
num1 = int(input("Enter your grade :"))
num2 = int(input("Enter the second grade :"))
moy = (num1 + num2)//2
print("your moy is {}",moy) '''
'''
#Identification

id_user =""
user_password = ""

print("\t\tidentification page.")

IDent = input("Enter your the user Id : ")
PssW = input("Enter your the user password : ")

if IDent == id_user and PssW == user_password:
    print("Welcome to this site")
else:
    print("Wrong credentials\nPlease enter your credentials again")''' 


'''
random_latter = str(input("Enter a latter :"))

if random_latter in "euioay":
    print(" it's a vowel ")
else:
    print("It's a consonant")'''

    