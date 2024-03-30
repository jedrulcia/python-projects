file = open("invited_names.txt")
names = [line.strip() for line in file.readlines()]
file.close()

for name in names:
    file = open("starting_letter.txt")
    text = file.read()
    file.close()
    new_text = text.replace("[name]", name)
    new_file = open(f"letter_for_{name}.txt", mode="w")
    new_file.write(new_text)
