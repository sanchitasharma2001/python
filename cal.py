print(" Enter 1 for addition \n Enter 2 for substraction \n Enter 3 for multiplication \n Enter 4 for division \n Enter 5 for modulo" )
s=input("Enter your choice : ")
a=float(input("Enter the value for a:"))
b=float(input("Enter the value for b:"))
if s==1:
    print(a+b)
elif s==2:
    print(a-b)
elif s==3:
    print(a*b)
elif s==4:
    print(a/b)
else:
    print(a%b)
