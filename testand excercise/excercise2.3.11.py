hour=input("give me the details about hours ?\n")
try:
    hours=float(hour)
except:
    print("numeric")
rat=input("give me the hourly rate \n ")

try:
    rate=float(rat)
except:
    print("numeric")


try:
    if hours>=40 :
        payment=str((hours*rate)*1.5)
        print("here is the payment you get\n "+payment)
        

    
    else:
     

        payment=str((hours*rate))
        print("here is the payment you get\n "+payment)
except :
    print("lololololo")

    