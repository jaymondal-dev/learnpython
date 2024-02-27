import sqlite3 #importing database software
conn=sqlite3.connect('test1.sqlite') # creating a database and connecting with it 
cor=conn.cursor() # creatinfg the cursor
cor.execute('''CREATE TABLE test (email text,count INTEGER )''') #creating the table
fname=input("the file name \n") #asking a promt for datbase name
if len(fname)<1:
    fname='mbox-short.txt'
f=open(fname)
for i in f: #a for loop that will read through text file and insert the data according to the 
    if not i.startswith("From:"): continue 
    pieces=i.split()
    email=pieces[1]
    cor.execute('SELECT count FROM test WHERE email=? ',(email,))
    row=cor.fetchone()
    if row==None:
        cor.execute('INSERT INTO test (email,count) VALUES (?,1)',(email,))
    else:
        cor.execute('UPDATE test SET count = count+1 WHERE email=? ',(email,))
    conn.commit()

string='SELECT email,count FROM test ORDER BY count DESC LIMIT 10'
t=open('see.txt','w')
for i in cor.execute(string):
    print(str(i[0]),i[1])
    
    t.write(i[0]+'  '+str(i[1])+'\n')
cor.close()
t.close()
