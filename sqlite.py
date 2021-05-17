import sqlite3

conn = sqlite3.connect('phosphorylator.db')
cursor = conn.cursor()

try:
	cursor.execute("DROP TABLE records");
except:
	print("No previous data to delete")

cursor.execute("""CREATE TABLE records(`mouse` text, `match` text, `human` text, `both` text, `only` text)""")
f = open('phos_last.txt')
for line in f:
    items= line.split('\t')
    items[4] = items[4].replace("\n","");
    items[4] = items[4].replace("\r","");
    A = items[0]
    B = items[1]
    C = items[2]
    D = items[3]
    E = items[4]
    cursor.execute("INSERT INTO records VALUES (?,?,?,?,?)",(A,B,C,D,E,));
    print("({}) ({}) ({}) ({}) ({})".format(A,B,C,D,E));
conn.commit()

cursor.execute("SELECT * FROM records WHERE mouse=?",("Q99KD5",));
row = cursor.fetchone();
print("mouse: {}".format(row[0]));
print("match: {}".format(row[1]));
print("human: {}".format(row[2]));
print("both: {}".format(row[3]));
print("only: {}".format(row[4]));

f.close()

