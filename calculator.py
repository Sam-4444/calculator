# define the operators as a set
operators={"+","-","*","/"}

# getting entrances(digits)
try:
 num1=int(input("enter a number : "))
 num2=int(input("enter second number :"))
except ValueError:
 print("entrance is not an integer !")


# getting the entrances(operators)
op=input("enter the operator :")
if op not in operators:
 print("that is not a valid operator !")
 exit()


#  doing the operations
if op=="+":
    print("the addition equals to :",num1+num2)
elif op=="-":
    print("the subtraction equals to : ",num1-num2)
elif op=="*":
    print("the multiplication equals to : ",num1*num2)
elif op=="/":
    print("the division equals to : ",num1/num2)