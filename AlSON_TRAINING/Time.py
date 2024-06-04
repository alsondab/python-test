'''def Time():
    Tsec=int(input("Enter second : "))
    h=Tsec//3600
    r=Tsec % 3600
    m=r//60
    s=r % 60
    return h,m,s

h,m,s=Time()
print(f"\t {h}h.{m}min.{s}sec.. ")
'''
def time () :
    while True :
        try :
            ts = int (input("Enter the sec : "))
            h=ts//3600
            r=ts % 3600
            m=r//60
            s=r % 60
            print(f"the time is {h}h {m}min and {s}sec")
            break 
        except ValueError :
            print("ENTER ONLY NUMERS !!! ")
        except Exception :
            print("An unexpected error occured try again !!! ")
    return h,m,s,

time()