from math import pi
def sphere_vol(r):
        return(4/3)*pi*r**3

r=float(input("Enter radius of the sphere(in cm):"))
if r<0:
     print("invalid radius")
else:
    volume=sphere_vol(r)
    print(f"Volume of the sphere: {volume: .5f}")
