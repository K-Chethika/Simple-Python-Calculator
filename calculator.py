def select_op(choice):
    if choice == '#':
        return -1  # Terminate
    if choice == '$':
        return 0   # Reset
    if choice in ['+', '-', '*', '/', '^', '%']:
        return choice  # Return valid operation
    return None  # Invalid input

while True:
    print("Select operation.")
    print("1. Add       : + ")
    print("2. Subtract  : - ")
    print("3. Multiply  : * ")
    print("4. Divide    : / ")
    print("5. Power     : ^ ")
    print("6. Remainder : % ")
    print("7. Terminate : # ")
    print("8. Reset     : $ ")
    
    try:
        choice = input("Enter choice (+, -, *, /, ^, %, #, $): ")
        print(choice)
    except EOFError:
        print("Done. Terminating")
        break

    operation = select_op(choice)

    if operation == -1:
        print("Done. Terminating")
        break
    elif operation == 0:
        print("Resetting Calculator.")
        continue
    elif operation is None:
        print("Unrecognized operation")
        continue

    try:
        first_number_input = input("Enter first number: ")
        print(first_number_input)
        
        if first_number_input.endswith('$'):
            continue  # Reset the calculator
        elif first_number_input.endswith('#'):
            print("Done. Terminating")
            break
        else:
            first_number = int(first_number_input)

        second_number_input = input("Enter second number: ")
        print(second_number_input)

        if second_number_input.endswith('$'):
            continue  # Reset the calculator
        elif second_number_input.endswith('#'):
            print("Done. Terminating")
            break
        else:
            second_number = int(second_number_input)
    
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        continue
    except Exception:
        print("Error occurred. Terminating.")
        break

    if operation == '+':
        result = first_number + second_number
    elif operation == '-':
        result = first_number - second_number
    elif operation == '*':
        result = first_number * second_number
    elif operation == '/':
        if second_number == 0:
            print("float division by zero")
            result = None
        else:
            result = first_number / second_number
    elif operation == '^':
        result = first_number ** second_number
    elif operation == '%':
        result = first_number % second_number

    if result is not None:
        print(float(first_number), choice, float(second_number), "=", float(result))
    else:
        print(float(first_number), choice, float(second_number), "=", "None")
