def computepay(a,b):
   
    if a>=8:
        pay=(a*b)*1.5
        print("your payment is "+str(pay))
    else:
        pay=a*b
        print("your payment is "+str(pay))
    return computepay
x=computepay(12,30)
print(x)