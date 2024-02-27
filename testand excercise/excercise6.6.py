def count():
    string=input("give your string here >\n")
    letter=input("give the letter you want to count >\n")
    cn=0
    for i in string:
        if i==letter:
            cn+=1
    print(letter," is ",cn," times.")

count()