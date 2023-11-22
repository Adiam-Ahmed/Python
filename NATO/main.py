import pandas

data = pandas.read_csv("Python/NATO/nato_letters.csv")

# Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# Create a list of the phonetic code words from a word that the user inputs and handle errors.
def generate():
    while True:
        word = input("Enter a word: ").upper()
        output_list = []

        for letter in word:
            try:
                output_list.append(phonetic_dict[letter])
            except KeyError:
                print(f"Sorry, '{letter}' is not in the English alphabet. Please enter a valid word.")
                break

        if len(output_list) == len(word):
            print(output_list)
            break

generate()
