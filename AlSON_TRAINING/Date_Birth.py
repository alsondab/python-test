def Calculate_date_birth():
    datej=(input("Enter your Day of birth : "))
    datem=(input("Enter your month of birth : "))
    date=int(input("Enter your year of birth : "))
    actualyear=2023
    actualyear-=date
    print("You were born on{} in {} in the year {} so you're {}years old".format(datej,datem,date,actualyear))
    


#actualyear,date,datej,datem=Calculate_date_birth()
#print("You were born on {} in {} in the year {} so you're {}years old".format(datej,datem,date,actualyear))
