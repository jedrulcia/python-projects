import pandas

alphabet_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")

alphabet_dictionary = {row.letter: row.code for index, row in alphabet_data_frame.iterrows()}

message = input("Enter a message: ").upper()
encrypted_message = [alphabet_dictionary[letter] for letter in message if letter in alphabet_dictionary.keys()]

print(encrypted_message)

