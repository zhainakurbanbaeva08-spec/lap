class Player:
    def __init__(self, player_id: int, name: str, hp: int):
        self.id = player_id
        self.name = name
        self._hp = hp
        self._inventory = []
    def __del__(self):
        print(f"Player {self.name} удалён")

p = Player(1, "Bob", 50)
del p