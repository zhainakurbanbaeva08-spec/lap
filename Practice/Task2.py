with open("file.txt", "w", encoding="utf-8") as f:
    for i in range(1,11):
        f.write(str(i) + "\n")

with open("file.txt", "r", encoding="utf-8") as f:
    content=f.read()
    print(content)