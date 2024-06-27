def calculator():
    print("Enter the operation you want to perform:")
    print("1.Addition/n2.substraction\n3.Multiplication/n4.division")
    choice =int(input("Enter your choice:"))
    if choice ==1:
        print("Enter the number you want to add.")
        num1=int(input("Enter the first number:"))
        num2 =int(input("Enter the second number:"))
        print("the sum of the members is:",num1+num2)
    elif choice == 2:
        print("enter the number if we want to sub.")
        num1=int(input("Enter the first number: "))
        num2=int(input("enter the second numbere."))
        print("the sub of the members is :",num1-num2)
    elif choice ==3:
        print("enter the number we want to multi[lay.")
        num1=int(input("enter the first number:"))
        num2=int(input("Enter the second number:"))
        print("the multiplay of members is:",num1*num2)
    elif choice ==3:
        print("enter the number we want to divide.")
        num1=int(input("enter the first number:"))
        num2=int(input("Enter the second number:"))
        if num2==0:
            print("cannot divide by zero")
            print("the Quotient of the numbers is:",num1/num2)
        calculator()
            
        

