def power():
    Base=float(input("Enter a base :"))
    expo=int(input("Enter the exponent :"))
    powe=Base**expo
    #print(f"{Base}**{expo}")
    return Base,expo,powe

Base,expo,powe=power()
print(f"{Base}**{expo}")
print("The power of the base {} and the exponent {} is {}: ".format(Base,expo,powe))