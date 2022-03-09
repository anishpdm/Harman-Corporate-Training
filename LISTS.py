student = []
count = int(input("Enter Total number of students ?"))
for i in range(0, count):
    name = input("Enter name ? ")
    email = input("Enter email id ?")
    mystudent={"name": name,"email": email.lower()}
    student.append(mystudent)


for i in student:
    print(i['name'])
    print(i["email"])




