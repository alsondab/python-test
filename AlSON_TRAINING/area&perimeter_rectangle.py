def rectangle():
    Length=float(input("Enter the Length: "))
    Width=float(input("Enter the Width: "))
    Area=Length*Width
    Perimeter=2*Length+Width
    return Area,Perimeter

Area,Perimeter=rectangle()
print("The Area of this rectangle is: ",Area)
print ("And is perimeter is: ",Perimeter)