# defining the function for the calculator
def basic_calculator():
    while True:

        # taking input for the first number
        noct1 = input("Enter a number (or enter \"quit\" to exit the app): ").strip()

        # exiting the app
        if noct1.lower() == "quit":
            print("Exiting the app. Goodbye.")
            break

        # Making sure numbers or decimals are the only accepted input
        try:
            numb1 = float(noct1)
        except ValueError:
            print("Only numbers or decimals are allowed")
            break

        # taking input for second number
        noct2 = input("Enter second number (or enter \"quit\"): ").strip()

        # exiting the app
        if noct2.lower() == "quit":
            print("Exiting the app. Goodbye.")

        # Making sure numbers or decimals are the only accepted input
        try:
            numb2 = float(noct2)
        except ValueError:
            print("Only numbers or decimals are allowed")
            break

        # Establishing the allowed operators
        operators = ("+", "-", "/", "*", "%")
        # taking input for operators
        operator = input("Enter an operator(+, /, -, *, %): ")

        # making sure only established operators are allowed
        if operator not in operators:
            print("Enter an operator from the given options")
            continue

        # setting up operators:
        if operator == "+":
            new_numb = numb1 + numb2
            print(f"{numb1} + {numb2} = {new_numb}")

        if operator == "*":
            new_numb = numb1 * numb2
            print(f"{numb1} * {numb2} = {new_numb}")

        if operator == "-":
            new_numb = numb1 - numb2
            print(f"{numb1} - {numb2} = {new_numb}")

        if operator == "/":
            if numb2 == 0:
                print("Error: Division by zero is not allowed.")
                continue
            else:
                new_numb = numb1/numb2
                print(f"{numb1} / {numb2} = {new_numb}")

        if operator == "%":
            if numb2 == 0:
                print("Error: Modulus by zero is not allowed")
                continue
            else:
                new_numb = numb1 % numb2
                print(f"{numb1} % {numb2} = {new_numb}")

        # checking if user wants to continue using the calculator, if not app quits
        again = input("Would you like to continue performing calculations? (yes/no): ").lower()
        if again != "yes":
            print("Goodbye. See you later :).")
            break

# running the function
basic_calculator()