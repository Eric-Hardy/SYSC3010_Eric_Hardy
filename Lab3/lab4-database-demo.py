#Exercise 3
import sqlite3
#connect to database file
dbconnect = sqlite3.connect("database.db");
#If we want to access columns by name we need to set
#row_factory to sqlite3.Row class
dbconnect.row_factory = sqlite3.Row;
#now we create a cursor to work with db
cursor = dbconnect.cursor();
#execute insert statement
#cursor.execute('''INSERT INTO temps values(date('now', '-1 day'), time('now'), "kitchen", 20.6)''');
temperature = 10.0
i = 0
while i < 5:
    i += 1
    #execute insert statement
    temperature += 1.1;
    cursor.execute('''INSERT INTO temps values(date('now', '-1 day'), time('now'), "kitchen", %f)'''% temperature);
dbconnect.commit();
#execute simple select statement
cursor.execute('SELECT * FROM temps');
#print data
for row in cursor:
    print(row['tdate'],row['ttime'],row['zone'],row['temperature']);
#close the connection
#dbconnect.close();




#Exercise 4
cursor.execute('''CREATE TABLE sensors (sensorID NUMERIC, type TEXT, zone TEXT)''');
cursor.execute('''INSERT INTO sensors values(1, "door", "kitchen")''');
cursor.execute('''INSERT INTO sensors values(2, "temperature", "kitchen")''');   
cursor.execute('''INSERT INTO sensors values(3, "door", "garage")''');
cursor.execute('''INSERT INTO sensors values(4, "motion", "garage")''');
cursor.execute('''INSERT INTO sensors values(5, "temperature", "garage")''');
dbconnect.commit();

cursor.execute('SELECT * FROM sensors WHERE zone="kitchen"');
#print data
for row in cursor:
    print(row['sensorID'],row['type'],row['zone']);

print("\n")
cursor.execute('SELECT * FROM sensors WHERE type="door"');
#print data
for row in cursor:
    print(row['sensorID'],row['type'],row['zone']);

cursor.execute('''DROP TABLE sensors''');
dbconnect.close();
