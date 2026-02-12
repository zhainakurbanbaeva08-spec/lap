names = ["Aйгерим", "Aслан", "Diana", "Ruslan", "Murat"]
with open("names.txt", "w", encoding="utf-8") as f:
    for name in names:
        f.write(name + "\n")

with open("names.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip().lower())
