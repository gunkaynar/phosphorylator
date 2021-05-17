import sqlite3

conn = sqlite3.connect('phosphorylator2.db')
cursor = conn.cursor()

try:
	cursor.execute("DROP TABLE records");
except:
	print("No previous data to delete")

cursor.execute("""CREATE TABLE records(`mouse` text, `dif` text, `site` text, 'human' text)""")
f = open('near_match.txt')
for line in f:
    items= line.split('\t')
    F = items[0]
    G = items[1].split(' ')[0]
    H = items[1].split(' ')[1]
    H = H.replace('\n','')
    H = H.replace('\r','')
    I = items[1].split(' ')[2]

    cursor.execute("INSERT INTO records VALUES (?,?,?,?)",(F,G,H,I));
    #print("({}) ({}) ({})".format(F,G,H));
conn.commit()


cursor.execute("SELECT * FROM records WHERE mouse=? ORDER BY dif",("Q9EQW7",));
rows = cursor.fetchall();
for row in rows:
    print("mouse: {}".format(row[0]));
    print("dif: {}".format(row[1]));
    print("site: {}".format(row[2]));
    print("human: {}".format(row[3]));
    
    
f.close()

