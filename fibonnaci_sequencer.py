# defining the function
def fibonacci_sequence(terms):

    # creating the terms and ensuring that only whole numbers are validated
    if terms<=0:
        print("Enter a valid \"whole\" number")
        return

    # starting numbers
    sequence = []
    a, b = 0,1

    for _ in range(terms):
        sequence.append(a)
        a,b = b, a+b

    print(f"The fibonacci sequence with {terms} terms: ")
    print(sequence)

try:
    noct_input = int(input("Enter a whole number: "))
    fibonacci_sequence(noct_input)
except ValueError:
    print("Enter a whole number.")


