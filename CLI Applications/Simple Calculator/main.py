def result(operator, num_1, num_2):
    if operator == '+':
        return round(num_1 + num_2, 3)
    elif operator == '-':
        return round(num_1 - num_2, 3)
    elif operator == '*':
        return round(num_1 * num_2, 3)
    elif operator == '/':
        if num_2 != 0:
            return round(num_1 / num_2, 3)
        else:
            return "Error: Division by zero."
    else:
        return f"{operator} is not a valid operator."

def main():
    operator = input("Enter an operator (+, -, *, /): ").strip()
    try:
        num_1 = float(input("Enter the 1st number: ").strip())
        num_2 = float(input("Enter the 2nd number: ").strip())
        result_value = result(operator, num_1, num_2)
        print(f"{num_1} {operator} {num_2} = {result_value}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()
