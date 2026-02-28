import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
p_data = {row.letter:row.code for (index, row) in data.iterrows()}

while True:

    word_input = str(input("Enter the word: ")).upper()
    try:
        f_data = [p_data[letter] for letter in word_input]
        print(f_data)
        break
    except KeyError:
        print("enter the letters only")