class EventIterator:
    def __init__(self, events):
        self.events = events
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index >= len(self.events):
            raise StopIteration
        event = self.events[self.index]
        self.index=self.index+1
        return event
events = [Event("ATTACK", {"damage": 10}), Event("HEAL", {"heal": 5})]
for e in EventIterator(events):
    print(e)