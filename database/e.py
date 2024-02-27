import sqlite3 #import the file , most importantly sqllite

conn = sqlite3.connect('emaildb.sqlite')# connect with database
cur = conn.cursor() #create cursor

cur.execute('DROP TABLE IF EXISTS Counts')#unimportant

cur.execute('''
CREATE TABLE Counts (email TEXT, count INTEGER)''')#send the command to database
#start of file selction 
fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox-short.txt'#check for file name error
fh = open(fname)#open the file 
#open the file
for line in fh:#create the loop to iteate line by line
    if not line.startswith('From: '): continue#llok for the lines that starts with from
    pieces = line.split()
    email = pieces[1]#geting the email
    cur.execute('SELECT count FROM Counts WHERE email = ? ', (email,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (email, count)
                VALUES (?, 1)''', (email,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?',
                    (email,))
    conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
