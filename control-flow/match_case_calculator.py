#prompt the user
try:
    num1 = float(input("Enter the first number:"))
    num2 = float(input("Enter the second number:"))
except ValueError:
    print("Invalid input. Please enter valid numbers.")

#the operator of choice
operator_of_choice = input("Choose the operation(+, -, *, /):")

#operation in action

match operator_of_choice:
    case '+':
        result = num1 + num2
        print(f"The result is {result}")
    case '-':
        result = num1 - num2
        print(f"The result is {result}")
    case '*':
        result = num1 * num2
        print(f"The result is {result}")
    case '/':
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            result = num1 / num2
            print(f"The result is {result}")
    case _: 
        print("Invalid operation. Pleas choose from +, -, *, /.")