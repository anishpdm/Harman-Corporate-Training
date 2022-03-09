import sqlite3

connection = sqlite3.connect("college.db")    # Create a  Db

getRoll=input("Enter Roll Number to be Updated ? ")

getName=input("Enter New Name : ")
getAdmno=input("Enter Admno Name : ")
getCollege=input("Enter College Name : ")


connection.execute("UPDATE STUDENT \
 SET NAME= '"+getName+"',ADMNO="+getAdmno+",COLLEGE='"+getCollege+"' \
  WHERE ROLLNUMBER="+getRoll)

connection.commit()
print("Updated Succesfully")

result = connection.execute("SELECT * FROM STUDENT")

for i in result:
    print("id =>", i[0])
    print("Name => ", i[1])
    print("Roll Number =>", i[2])
    print("Admno =>  ", i[3])

    print("College => ", i[4])




