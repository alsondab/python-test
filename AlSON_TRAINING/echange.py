def Echange():
    val1=input("Enter the first num :")
    val2=input("Enter the first num :")
    val3=input("Enter the first num :")

    '''val=val1
    val1=val2
    val2=val'''

    val1,val2,val3=val3,val2,val1
    
    return val1,val2,val3

val1,val2,val3=Echange()
print(f" A={val1} \n B={val2} \n C={val3}")