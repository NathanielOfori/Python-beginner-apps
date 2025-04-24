# define palindrome checker function
def palindrome_valid(text):

    '''
    ensuring there is no unnecessary space before and after the text
    removing all spaces in text
    and making all text lowercase so as to be uniform.
    '''


    noct_new_text = text.strip().replace(" ", "").lower()

    if noct_new_text == noct_new_text[::-1]:
        return True
    else:
        return False


# Taking user input
noct_input_text = input("Enter a word: ")

if palindrome_valid(noct_input_text):
    print(f"Your word, \"{noct_input_text}\" is a palindrome.")
else:
    print(f"Oops! Your word, \"{noct_input_text}\" is not a palindrome.")


