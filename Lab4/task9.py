import ast
class Logger:
    @staticmethod
    def read_logs(filename: str):
        events = []
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                timestamp, player_id, event_type, data = line.strip().split(";", 3)
                event = Event(event_type, ast.literal_eval(data))
                event.timestamp = datetime.fromisoformat(timestamp)
                events.append(event)
        return events
events = Logger.read_logs("logs.txt")
print(events)