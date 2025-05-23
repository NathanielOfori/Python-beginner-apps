#defining function
def email_validates(email):

    # checking and making sure there is exactly 1 @
    if email.count("@") != 1:
        return False

    #splitting the email into 2 separate parts ie. username and domain
    username,domain = email.split("@")

    # checking that neither parts are empty
    if len(username)==0:
        return False
    if len(domain)==0:
        return False

    # ensuring the domain has a "."
    if '.' not in domain:
        return False

    if ' ' in email:
        return False

    return True

while True:
    noct_email = input("Enter your email to check validation (or type \"quit\" to exit the app): ")
    if noct_email == "quit":
        print("Exiting the app. Goodbye.")
        break

    if email_validates(noct_email):
        print("Hurrah. Your email is valid!")
    else:
        print("Uh oh. Your email is not valid.")

    again = input("Would you like to check validity of another email? (yes/no): ")
    if again != "yes":
        print("Goodbye. See you later :). ")
        break









