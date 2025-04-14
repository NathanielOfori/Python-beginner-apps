# Define the reverse_string function
def reverse_string():


    while True:
        # display App Name
        print('String Reversal App')

        # Taking user input
        noct_input = input("Enter a word (or type 'quit' to exit): ")

        # To quit the app
        if noct_input.lower()== "quit":
            print("Exiting the App. Goodbye.")
            break


        # Checking and making sure user input is strictly just letters and spaces
        if not noct_input.replace(" ", "").isalpha():
            print('Only letters and spaces are allowed as input!')
            continue

        # Checking and making sure user input is more than 1 letter
        if len(noct_input.replace(" ", ""))<=1:
            print("User input must be more than one letter.")
            continue

        # If all conditions are met, then reverse user input and print.
        reverse_noct_input = noct_input[::-1]
        print(f"Your reversed input is {reverse_noct_input}")

# run reverse_string function
reverse_string()