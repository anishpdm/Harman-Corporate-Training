 # ZeroDivisionError , NameError, IOError, ValueError, EOFerror

try:
    age = 12
    if age < 18:
        raise ValueError("Age for Voting is minimum 18+")
    else:
        print("Eligible for Vote")

except ZeroDivisionError as e:
    print("Division Not possible by ZERO" + str(e))
except ValueError as e:
    print(str(e))

except:
    print("Exception occured")
else:
    print("Executed succesfully")
finally:
    print("Harman Ltd")
