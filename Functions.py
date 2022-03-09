
#define
# def printNmae(name):
#     for i in name:
#         print(i)
#
#
# def test():
#     pass
#
# nameList=["Anoop","Rahul","Tom"]
#
# #call
# printNmae(nameList)
#
#

# def multiply(a):
#     c = a*5
#     return c

# num_list=[1,3,5,32,78,90,2,7,9]
#
# odd_list= list(map( lambda x:x*2,num_list))
#
# print(odd_list)


# a = ("Anish","Rahul","Amjith")
# b = ("Kerala","TamilNadu","Karnataka","AndraPradesh")
# c= zip(a,b)
# print(tuple(c))



import CalculatorPackage


x=int(input("Enter num 1 => "))
y=int(input("Enter num 2 => "))
result=CalculatorPackage.addNumbers(x,y)

resul2=CalculatorPackage.Multiply(x,y)

print(result)
print(resul2)





