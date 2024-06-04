def choix_compte(somme ,minutes ,jours):
    compte_p=17225
    compte_uta_money=176249
    print("vous allez souscrire",somme,"fr pour",minutes,"minutes valables",jours,"jours")
    print(" 1.Compte principale ")
    print(" 2.Compte UTA money ")
    compte=int(input("Entrer votre choix :"))
    if compte==1 :
        print(compte_p-somme)
        return 0
    if compte==2 :
        code_secret=str(input("Entrer votre code secret :"))
        if code_secret=="0901" :
            print("Felicitation!!!!")
            print("Il vous reste :",compte_uta_money-somme)
    else :
        print("erreur!!")
               
    

code=str(input("entrer le code d'operation : "))
if code=="#2024#":
    print("bienvenue sur RESEAU UTA")
    print("1.appel")
    print("2.internet")
    print("3.SMS")

    choix=int(input("Entrer votre choix :"))
    if choix==1 :
        print("1.jour")
        print("2.mois")
        print("3.Semaine")
        choix_appel=int(input("entrer votre forfait appel:"))
        if choix_appel==1 :
            print("1.100fr pour 15 min")
            print("2.200fr pour 40min ")
            print("3.500fr pour 100 min ")
            choix_court=int(input("Entrer votre montant :"))
            if choix_court==1:
                choix_compte(100,15,1)
            if choix_court==2 :
                choix_compte(200,40,1)
            if choix_court==3 :
                choix_compte(500,100,1)
            else :
                print("erreur!!")
        if choix_appel==2 :
            print("1.2500fr pour 400 min")
            print("2.5000fr pour 1000min ")
            print("3.10000fr pour 10000 min ")
            choix_court=int(input("Entrer votre montant :"))
            if choix_court==1:
                choix_compte(2500,400,30)
            if choix_court==2 :
                choix_compte(5000,1000,30)
            if choix_court==3 :
                choix_compte(10000,10000,30)
            else :
                print("erreur!!")
        if choix_appel==3 :
            print("1.1000fr pour 150 min")
            print("2.1500fr pour 200min ")
            print("3.2000fr pour 300 min ")
            choix_court=int(input("Entrer votre montant :"))
            if choix_court==1:
                choix_compte(1000,150,7)
            if choix_court==2 :
                choix_compte(1500,200,7)
            if choix_court==3 :
                choix_compte(2000,300,7)
            else :
                print("erreur!!")
        
        else :
            print("Eurreur!!")
            
    if choix==2 :
        print("1.jour")
        print("2.mois")
        print("3.Semaine")
        choix_internet=int(input("entrer votre forfait internet :"))
        if choix_internet==1 :
            print("1.100fr pour 15 MO")
            print("2.200fr pour 40 MO")
            print("3.500fr pour 100 MO ")
            choix_court=int(input("Entrer votre montant :"))
            if choix_court==1:
                choix_compte(100,15,1)
            if choix_court==2 :
                choix_compte(200,40,1)
            if choix_court==3 :
                choix_compte(500,100,1)
            else :
                print("erreur!!")
        if choix_internet==2 :
            print("1.2500fr pour 400 MO")
            print("2.5000fr pour 1000 MO ")
            print("3.10000fr pour 10000 MO ")
            choix_court=int(input("Entrer votre montant :"))
            if choix_court==1:
                choix_compte(2500,400,30)
            if choix_court==2 :
                choix_compte(5000,1000,30)
            if choix_court==3 :
                choix_compte(10000,10000,30)
            else :
                print("erreur!!")
        if choix_internet==3 :
            print("1.1000fr pour 150 MO")
            print("2.1500fr pour 200MO ")
            print("3.2000fr pour 300MO ")
            choix_court=int(input("Entrer votre montant :"))
            if choix_court==1:
                choix_compte(1000,150,7)
            if choix_court==2 :
                choix_compte(1500,200,7)
            if choix_court==3 :
                choix_compte(2000,300,7)
            else :
                print("erreur!!")
        
        else :
            print("Eurreur!!")
            
    if choix==3 :        
        print("1.jour")
        print("2.mois")
        print("3.Semaine")
        choix_sms=int(input("entrer votre forfait SMS  :"))
        if choix_sms==1 :
            print("1.100fr pour 15 SMS")
            print("2.200fr pour 40SMS")
            print("3.500fr pour 100SMS ")
            choix_court=int(input("Entrer votre montant :"))
            if choix_court==1:
                choix_compte(100,15,1)
            if choix_court==2 :
                choix_compte(200,40,1)
            if choix_court==3 :
                choix_compte(500,100,1)
            else :
                print("erreur!!")
        if choix_sms==2 :
            print("1.2500fr pour 400 SMS")
            print("2.5000fr pour 1000SMS ")
            print("3.10000fr pour 10000 SMS ")
            choix_court=int(input("Entrer votre montant :"))
            if choix_court==1:
                choix_compte(2500,400,30)
            if choix_court==2 :
                choix_compte(5000,1000,30)
            if choix_court==3 :
                choix_compte(10000,10000,30)
            else :
                print("erreur!!")
        if choix_sms==3 :
            print("1.1000fr pour 150 SMS")
            print("2.1500fr pour 200SMS ")
            print("3.2000fr pour 300 SMS ")
            choix_court=int(input("Entrer votre montant :"))
            if choix_court==1:
                choix_compte(1000,150,7)
            if choix_court==2 :
                choix_compte(1500,200,7)
            if choix_court==3 :
                choix_compte(2000,300,7)
            else :
                print("erreur!!")
        
    else :
        print("Eurreur!!")