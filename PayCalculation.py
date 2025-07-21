#pay calculation
hrs = input("Enter Hours:")
h = float(hrs)
rat= input('Enter rate')
r= float(rat)
if h<=40:
    h=h*r
    print(h)
if h>40:
    bh=h-40
    bh=bh*r*1.5
    hh=40*r
    fh=bh+hh
    print(fh)
    