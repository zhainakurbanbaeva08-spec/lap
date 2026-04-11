class Logger:
    @staticmethod
    def log(event, player, filename: str):
        with open(filename, "a", encoding="utf-8") as f:
            line = f"{event.timestamp};{player.id};{event.type};{event.data}\n"
            f.write(line)
Logger.log(e, p, "logs.txt")
with open("logs.txt", "r", encoding="utf-8") as f:
    content=f.read()
    print(content)