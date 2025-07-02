firstNum = input("Enter your first number: ")
secondNum = input("Enter your second number: ")
whatOp = input("Enter an operation (+, -, *, /): ")

if whatOp == "/" and secondNum == "0":
    print("Cannot divide by zero!")
else:
    answer = eval(firstNum + whatOp + secondNum)
    print(f"Your answer is: {answer}!")
    
