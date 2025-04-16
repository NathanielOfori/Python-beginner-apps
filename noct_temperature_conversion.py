def convert_temperature():
    while True:
        # Display App Name
        print('Temperature Convertor App')

        # Taking user input for temperature value
        noct_user_input = input("Enter a temperature value (or type \"quit\" to exit): ").strip()

        # Handling keyword 'quit' to exit the app
        if noct_user_input.lower() == "quit":
            print("Exiting the App. Goodbye.")
            break

        #Checking if user input is a valid number / decimal
        try:
            temperature = float(noct_user_input)
        except ValueError:
            print("Only numbers and or decimals are allowed as input")
            continue

        # Taking user input to define the unit of temperature
        noct_temperature_unit = input("Enter preferred unit Unit of Temperature ('C' or 'F'): ").strip().upper()

        # Checking and making sure the user inputs accepted Units of Temperature
        if noct_temperature_unit not in ["C", "F"]:
            print("Allowed Units of Temperature are Celsius[C] or Fahrenheit[F]")
            continue

        #  Conversion of temp from Celsius to Fahrenheit if the users input was C
        if noct_temperature_unit == "C":
            new_temperature = (temperature*9/5) + 32
            print(f"Temperature {noct_user_input}°C = {new_temperature}°F")

        #  Conversion of temp from Fahrenheit to Celsius if the users input was F
        if noct_temperature_unit == "F":
            new_temperature = (temperature-32)*5/9
            print(f"Temperature {noct_user_input}°F = {new_temperature}°C")

# Run the function convert_temperature
convert_temperature()