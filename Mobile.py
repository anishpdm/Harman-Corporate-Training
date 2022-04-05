import sqlite3 as s
from prettytable import PrettyTable

connection = s.connect("Mobile.db")

listoftables = connection.execute("SELECT name from sqlite_master WHERE type='table' AND name='SMARTPHONES'").fetchall()

if listoftables != []:
    print("Table already exist")
else:
    connection.execute(''' CREATE TABLE SMARTPHONES(
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    SERIAL_NUMBER INTEGER,
                    MODEL_NAME TEXT,
                    BRAND TEXT,
                    MANUFACTURE_YEAR INTEGER,
                    MANUFACTURE_MONTH TEXT,
                    PRICE INTEGER


    ) ''')
    print("Table created Successfully")

while True:
    print("Select an option from menu")
    print("1.Add a Smart Phone ")
    print("2.View all Smart Phones ")
    print("3.Search a Smart Phone using Serial Number ")
    print("4.Update a Smart Phone using Serial Number ")
    print("5.Delete a Smart Phone using Serial Number ")
    print("6.View the Most expensive Phone ")
    print("7.View the Less expensive Phone ")
    print("8.View the Average cost of a  Phone ")
    print("9. Display Total count of SmartPhones in stock ")
    print("10. Display Total Amount of SmartPhones in stock ")
    print("11. Display Total Amount of SmartPhones in stock based on each brand")
    print("12. Display the SmartPhones based on Price range ")

    print("13.Exit ")

    choice = int(input("Enter a choice: "))

    if choice == 1:
        getSno = input("Enter Serial Number: ")
        getMname = input("Enter Model Name: ")
        getBrand = input("Enter Brand: ")
        getManuyear = input("Enter Manufacture Year: ")
        getManumonth = input("Enter Manufacture Month: ")
        getPrice = input("Enter Price: ")

        connection.execute(" INSERT INTO SMARTPHONES(SERIAL_NUMBER, MODEL_NAME, BRAND, MANUFACTURE_YEAR, \
        MANUFACTURE_MONTH, PRICE) VALUES(" + getSno + ",'" + getMname + "','" + getBrand + "'," + getManuyear + ",\
        '" + getManumonth + "'," + getPrice + ")")
        connection.commit()
        print("Inserted Successfully")

    elif choice == 2:
        result = connection.execute("SELECT * FROM SMARTPHONES")
        table = PrettyTable(["Id", "Serial Number", "Model Name", "Brand", "Manufacture Year","Manufacture Month","Price"])

        for i in result:
            table.add_row([i[0],i[1],i[2],i[3],i[4],i[5],i[6]])
        print(table)

    elif choice == 3:
        getSno = input("Enter Serial number: ")

        result = connection.execute("SELECT * FROM SMARTPHONES WHERE SERIAL_NUMBER="+getSno)
        table = PrettyTable(["Id", "Serial Number", "Model Name", "Brand", "Manufacture Year","Manufacture Month","Price"])

        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6]])
        print(table)

    elif choice == 4:
        getSno = input("Enter Serial number: ")

        getNsno = input("Enter New Serial Number: ")
        getNmname = input("Enter New Model Name: ")
        getNbrand = input("Enter New Brand: ")
        getNmanuyear = input("Enter New Manufacture Year: ")
        getNmanumonth = input("Enter New Manufacture Month: ")
        getNprice = input("Enter New Price: ")

        result = connection.execute(" UPDATE SMARTPHONES SET SERIAL_NUMBER=" + getNsno + ", MODEL_NAME='" + getNmname + "', \
        BRAND='" + getNbrand + "', MANUFACTURE_YEAR=" + getNmanuyear + ", MANUFACTURE_MONTH='" + getNmanumonth + "',\
        PRICE=" + getNprice + " WHERE SERIAL_NUMBER=" + getSno)
        connection.commit()
        print("Updated Successfully")

    elif choice == 5:
        getSno = input("Enter Serial number: ")

        result = connection.execute("DELETE FROM SMARTPHONES WHERE SERIAL_NUMBER=" + getSno)
        connection.commit()
        print("Deleted Successfully")


    elif choice == 6:
        result = connection.execute("SELECT * FROM SMARTPHONES WHERE PRICE=(SELECT MAX(PRICE) FROM SMARTPHONES) ")
        table = PrettyTable(
            ["Id", "Serial Number", "Model Name", "Brand", "Manufacture Year", "Manufacture Month", "Price"])

        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6]])
        print(table)



    elif choice == 7:
        result = connection.execute("SELECT * FROM SMARTPHONES WHERE PRICE=(SELECT MIN(PRICE) FROM SMARTPHONES)")
        table = PrettyTable(
            ["Id", "Serial Number", "Model Name", "Brand", "Manufacture Year", "Manufacture Month", "Price"])

        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6]])
        print(table)

    elif choice == 8:
        result = connection.execute("SELECT AVG(PRICE) as price FROM SMARTPHONES")

        for i in result:
            print("Price: ", i[0])

    elif choice == 9:
        result = connection.execute("SELECT COUNT(*) as count FROM SMARTPHONES")

        for i in result:
            print("Total Items : ", i[0])

    elif choice == 10:
        result = connection.execute("SELECT SUM(PRICE) as price FROM SMARTPHONES")

        for i in result:
            print("Price: ", i[0])

    elif choice == 11:
        result = connection.execute("SELECT BRAND,SUM(PRICE) as price FROM SMARTPHONES GROUP BY BRAND ORDER BY BRAND ASC")

        table = PrettyTable(
            ["Brand", "Price"])

        for i in result:
            table.add_row([i[0], i[1]])
        print(table)

    elif choice == 12:
        lowerAmount=input("Enter Lower price ?")
        HigherAmount=input("Enter Higher price ?")

        result = connection.execute("SELECT * FROM SMARTPHONES WHERE PRICE BETWEEN "+lowerAmount+" AND "+HigherAmount + " ORDER BY PRICE")
        table = PrettyTable(
            ["Id", "Serial Number", "Model Name", "Brand", "Manufacture Year", "Manufacture Month", "Price"])

        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6]])
        print(table)

    elif choice == 13:
        connection.close()
        break

    else:
        print("Invalid Option")