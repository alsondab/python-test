'''def a () :

    a = int (input("ENTER a NUMBER : \n"))
    i=0
    print (f"\nthe a of {a} is:")
    for i in a (0,11) :
        result = a*i
        print (f"{a}*{i} = {result}")
    return a,i,result

a()
'''

def a (a,mult) :
    print(f"a of {a} from 0 to {mult}")
    for i in a (0,mult+1) :
        result = a*i
        print(f"{a}*{i}= {result}")
    return a , i , result

a(2,5)