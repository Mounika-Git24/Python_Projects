import pandas

data = pandas.read_csv("NATO_Alphabets.csv")
alpha_dict = {row.letter: row.code for (index, row) in data.iterrows()}

end = False
while not end:
    user_word = input("Enter a word: ").upper()
    try:
        word_code = [alpha_dict[letter] for letter in user_word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        end = True
        print(word_code)

