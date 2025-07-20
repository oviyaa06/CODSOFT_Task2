# Simple Arithimetic Calculator 
print(""" 
Enter any operation:- 
    addition -> +
    subtraction -> -
    multiplication -> *
    division -> /
    remainder -> %
    exponent -> **
      """)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
oper = input("Enter operation to perform: ")
if oper == '+':
    print(f"Addition of num1 and num2 is: {num1+num2}")
elif oper == '-':
    print(f"Subtraction of num1 and num2 is: {num1-num2}")
elif oper == '*':
    print(f"Multiplication of num1 and num2 is: {num1*num2}")
elif oper == '/':
    print(f"Division of num1 and num2 is: {num1/num2}")
elif oper == '%':
    print(f"Remainder of num1 and num2 is: {num1%num2}")
elif oper == '**':
    print(f"Exponent of num1 and num2 is: {num1**num2}")
else:
    print("Invalid operator!")



    
