#using def function
def computepay(h, r):  
    if h>40:
        oh=(h-40)*(r*0.5)
        nh=h*r
        p=oh+nh
    else:
        p=h*r   
    print("Pay", p)
    return
hrs = input("Enter Hours:")
rat = input("Enter Rate:")
h=float(hrs)
r=float(rat)
p = computepay(h, r)