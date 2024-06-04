import math
def sphere():
    Rayon=float(input("Entter a number : "))
    volume=(4*math.pi*(Rayon**3))/3
    return volume

volume=sphere()
print("The volume is : {}",format(volume,".2f"))