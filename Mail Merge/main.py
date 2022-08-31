with open("Input/Names/names.txt") as names:
    for name in names.readlines():
        with open("Input/Letters/starting_letter.txt") as letter, \
                open(f"Output/ReadyToSend/{name[:-1]}.txt", "w") as new_file:
            for line in letter.readlines():
                new_file.write(line.replace("name", name[:-1]))



# PLACEHOLDER = "name"
# with open("Input/Names/names.txt") as names_file:
#     names = names_file.readlines()
#
# with open("Input/Letters/starting_letter.txt") as letter_file:
#     letter_contents = letter_file.read()
#     for name in names:
#         stripped_name = name.strip()
#         new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
#         with open(f"Output/ReadyToSend/letter_for_{stripped_name}.txt", "w") as completed_letter:
#             completed_letter.write(new_letter)
