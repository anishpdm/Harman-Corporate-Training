while True:
    print(" Select an Option from the Menu")
    print("1. Add 2 numbers")
    print("2. Subtract 2 numbers")
    print("3. Multiply 2 numbers")
    print("4. Divide 2 numbers")
    print("5. EXIT")

    choice=int(input("Select Choice ?"))
    if choice==1:
        x=int(input("Enter 1st number "))
        y=int(input("Enter 2st number "))
        z=x+y
        print(z)
    elif choice==2:
        x = int(input("Enter 1st number "))
        y = int(input("Enter 2st number "))
        z=x-y
        print(z)
    elif choice==3:
        x = int(input("Enter 1st number "))
        y = int(input("Enter 2st number "))
        z=x*y
        print(z)
    elif choice==4:
        x = int(input("Enter 1st number "))
        y = int(input("Enter 2st number "))
        z=x/y
        print(z)
    elif choice == 5:
        break
    else:
        print("Invalid Choice")


