import sqlite3

connection = sqlite3.connect("college.db")

listOfTables=connection.execute("SELECT name from sqlite_master WHERE type='table' AND name='STUDENT' ").fetchall()

if listOfTables!=[]:
    print("Table Already There ! ")
else:
    connection.execute(''' CREATE TABLE STUDENT(
                        ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        NAME TEXT,
                        ROLLNUMBER INTEGER,
                        ADMNO INTEGER,
                        COLLEGE TEXT);    ''')
    print("Table has created")


while True:
    print(" Select an Option from the Menu")
    print("1. Add a Student")
    print("2. Search a Student")
    print("3. Update a Student")
    print("4. Delete a Student")
    print("5. View all Students")
    print("6. EXIT ")


    choice=int(input("Enter  a Choice ? "))

    if choice == 1:
        getName = input("Enter Name : ")
        getRollNumber = input("Enter Roll Number : ")
        getAdmno = input("Enter Admno Number : ")
        getCollege = input("Enter College name : ")
        connection.execute("INSERT INTO STUDENT(NAME,ROLLNUMBER,ADMNO,COLLEGE) \
        VALUES('" + getName + "'," + getRollNumber + "," + getAdmno + ",'" + getCollege + "')")
        connection.commit()

        print("Inserted Succesfully")


    elif choice == 2:
        getRoll=input("Enter a Roll number to the searched ")
        result = connection.execute("SELECT * FROM STUDENT WHERE ROLLNUMBER="+getRoll)

        for i in result:
            print("id =>", i[0])
            print("Name => ", i[1])
            print("Roll Number =>", i[2])
            print("Admno =>  ", i[3])

            print("College => ", i[4])

    elif choice == 3:
        getRoll = input("Enter Roll Number to be Updated ? ")

        getName = input("Enter New Name : ")
        getAdmno = input("Enter Admno Name : ")
        getCollege = input("Enter College Name : ")

        connection.execute("UPDATE STUDENT \
         SET NAME= '" + getName + "',ADMNO=" + getAdmno + ",COLLEGE='" + getCollege + "' \
          WHERE ROLLNUMBER=" + getRoll)

        connection.commit()
        print("Updated Succesfully")


    elif choice == 4:
        getRoll = input("Enter Roll Number to be Deleted ? ")
        connection.execute("DELETE FROM STUDENT WHERE ROLLNUMBER=" + getRoll)

        connection.commit()
        print("Deleted Succesfully")

    elif choice == 5:

        result = connection.execute("SELECT * FROM STUDENT")

        for i in result:
            print("id =>", i[0])
            print("Name => ", i[1])
            print("Roll Number =>", i[2])
            print("Admno =>  ", i[3])

            print("College => ", i[4])

    elif choice == 6:
        connection.close()
        break



    else:
        print("Invalid Choice")





