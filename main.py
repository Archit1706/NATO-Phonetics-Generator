import pandas

# TODO 1. Create a dictionary in this format:
nato_phonetics = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(nato_phonetics)
nato_phonetics_dict = {row.letter: row.code for (index, row) in nato_phonetics.iterrows()}
# print(nato_phonetics_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word or name to get NATO Phonetic Mnemonics: ").upper()
output_list = [nato_phonetics_dict[letter] for letter in word]
print(f'The NATO list for {word}: {output_list}')
