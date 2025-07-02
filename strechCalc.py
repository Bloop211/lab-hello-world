user_input = input("Enter your expression (e.g., 10 * 4): ")
parts = user_input.split()

first_number_str = parts[0]
operator_symbol = parts[1]
second_number_str = parts[2]

if operator_symbol == "/" and second_number_str == "0":
    print("So sorry! Cannot divide by zero!")
elif operator_symbol == "+" or operator_symbol == "-" or operator_symbol == "*" or operator_symbol == "/":
    expression = first_number_str + operator_symbol + second_number_str
    answer = eval(expression)
    print(f"Okay, the answer is: {answer:.2f}!")
else:
    print("Ohh. You put an invalid operator!")