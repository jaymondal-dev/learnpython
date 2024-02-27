print("hello I am stucked ")
hour=input("give me the details about hours ?\n")
rat=input("give me the hourly rate \n ")
hours=float(hour)
rate=float(rat)
if hours>=40 :
    payment=str((hours*rate)*1.5)
    print("here is the payment you get\n "+payment)
        

    
else:
     

    payment=str((hours*rate))
    print("here is the payment you get\n "+payment)