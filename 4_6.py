def computepay(h,r):
    if(h>40):
        x = 40*r
        y = (h-40)*r*1.5
        k = x+y
        return k
    else:
        k = h*r 
        return k

hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter rate:")
r = float(rate)
p = computepay(h,r)
print("Pay",p)
