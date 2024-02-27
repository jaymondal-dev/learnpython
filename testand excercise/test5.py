score=(input("what\'s your score?\n"))
sc1=float(score)
def cmputegrade(sc):
    
    if sc>=0 and sc<=1.0:
        if sc>=0.9:
            print("A")
        elif sc>=0.8:
            print("B")
        elif sc>=0.7:
            print("c")
        elif sc>=0.6:
            print("D")
        else:
            print("F")
    else:
        print("give the right value")
    
cm=cmputegrade(sc1)
    
print(cm)
