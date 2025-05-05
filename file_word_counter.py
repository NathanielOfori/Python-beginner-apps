def file_word_counter(filename):
    try:
        with open(filename, "r") as file:
            text = file.read()


        text = text.lower()

        import string
        for punctuations in string.punctuation:
            text = text.replace(punctuations, "")

        words = text.split()

        word_count = {}

        for word in words:
            if word in word_count:
                word_count[word] +=1
            else:
                word_count[word]= 1

        print("\nWord Counts (A-Z): ")
        for word in sorted(word_count):
            print(f"{word}: {word_count[word]}")

    except FileNotFoundError:
        print("File not found. Check the name/path")

filename = input("Enter the name of the text file (example: notes.txt): ")

# Call the function with the provided file name
file_word_counter(filename)


