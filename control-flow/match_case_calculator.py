
print("input two numbers at a time: ")
num1 =int(input("enter the first number:"))
num2 =int(input ("enter the second number:"))

operation = input("choose the operation (+, -, * , / ):")

match operation:
    case "+":
        result = num1 + num2
        print (f"The result is {result}")

    case "-":
        result = num1 - num2
        print (f"The result is {result}")

    case "*":
        result = num1*num2
        print(f"The result is {result}")

    case "/":
        if num2 ==0:
            print (f"can't divided by zero. ")
        else:
            result = num1/num2
            print (f"The result is {result}")
    case _:
        print ("invalide operation. please choose operation ,+ ,-, *, or /")            

    






