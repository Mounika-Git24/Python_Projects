import pandas

data = pandas.read_csv("NATO_Alphabets.csv")
alpha_dict = {row.letter: row.code for (index, row) in data.iterrows()}

user_word = input("Enter a word: ").upper()
word_code = [alpha_dict[letter] for letter in user_word]
print(word_code)

