import pandas as pd
# Goal: As few lines of code as possible

# Create a dictionary of letters and phonetic code words
nato_dict = {row.letter: row.code for (index, row) in pd.read_csv("nato_phonetic_alphabet.csv").iterrows()}


# Create a list of the phonetic code words from a word that the user inputs
# Check for exceptions/errors that would crash program
def name_convert():
    name = input("What's your name? ").upper()
    try:
        nato_name = [nato_dict[letter] for letter in name]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
    else:
        print(f"Your NATO phonetic name is: {nato_name}")
    finally:
        name_convert()


name_convert()






