from Hello_world import salut

salut ()

def  IDENT () :#pw) :
    
    while True :
        try :
            pw = int (input("Enter your password :"))
           # pw = int (input(f"Enter password {pw}"))
            print(" \t\t\t SUCCESS!! ")
            break
        except ValueError :
            print("\n ERROR TRY ONLY NUMBERS !! ")
        except Exception :
            print("\n Wrong Password !! ")
    return pw

IDENT()


from Date_Birth import Calculate_date_birth

Calculate_date_birth ()
 