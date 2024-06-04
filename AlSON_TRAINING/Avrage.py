'''def avrage():
    cpt = 0
    while cpt < 5:
        cpt += 1
        Grade = float(input(f"Enter your grade {cpt}: "))
        sum=Grade+Grade+Grade+Grade+Grade
        Moyen= sum/5

    if Moyen<=9 :
        print(f"{Moyen} :( TRY AGAIN NEXT TIME.")
    elif Moyen==10 :
        print(f":|")    
    elif Moyen>=11 or Moyen<=15:
        print(":)")
    else :
        print(":) :) :)")
    return Moyen




Moyen = avrage()
#print("your different grades are \n Math:{} \n BD: {} \n NETWORKING: {} \n UML: {} English: {}".format())
'''

def Average_Grade () :
    i = 0
    while cpt < 5:
      cpt += 1
      grade = float(input("Enter your first grade {}:".format(cpt)))
      Sum = grade + grade + grade + grade + grade 
      Average = Sum/5
    print("Your total grade is {}".format(Average))
    
    if Average < 10 :
       print(":(")
    elif Average == 10 :
        print(":|")
    elif Average <=15 :
        print(":)")
    else:
       print("Well done")
              
    return Average

Average = Average_Grade()

