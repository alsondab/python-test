def Operators ():
    X=float(input("Enter X: "))
    Y=float(input("Enter Y: "))
    ADD=X+Y
    MULT=X*Y
    DIV=X/Y
    SUB=X-Y
    DIFF=X%Y
    return ADD,MULT,DIV,SUB,DIFF

ADD,MULT,DIV,SUB,DIFF=Operators()
print("Add=",ADD)
print("MULT=",MULT)
print("DIV=",DIV)
print("SUB=",SUB)
print("DIFF=",DIFF)