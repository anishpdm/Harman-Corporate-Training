import sqlite3

conn = sqlite3.connect('test.db')
print("Opened database successfully")

listOfTables = conn.execute(

   """SELECT name FROM sqlite_master WHERE type='table'
 
   AND name='COMPANY'; """).fetchall()

print(listOfTables)

if listOfTables != []:

   print('Table found!')

else:


   conn.execute('''CREATE TABLE COMPANY
         (ID INTEGER PRIMARY KEY AUTOINCREMENT,
         NAME           TEXT    NOT NULL,
         AGE            INTEGER     NOT NULL,
         ADDRESS        CHAR(50),
         SALARY         REAL);''')
   print("Table created successfully")



conn.execute("INSERT INTO COMPANY (NAME,AGE,ADDRESS,SALARY) \
      VALUES ( 'Paul', 32, 'California', 20000.00 )");



conn.commit()
print("Records created successfully")

cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
for row in cursor:
   print("ID = ", row[0])
   print("NAME = ", row[1])
   print("ADDRESS = ", row[2])
   print("SALARY = ", row[3], "\n")

print("Operation done successfully")

conn.close()
