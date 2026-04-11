
class Player:
    def __init__(self, player_id, name, hp):
        self._id=player_id
        self.name=name.strip().title()
        self.hp=max(0,hp)
    def __str__(self):
        return f"PLayer(id={self._id}, name='{self.name}',hp={self.hp})"
    def __del__(self):
         print(f"Player {self._name} удалён")

p=Player(1, "John",120)
print(p)
p2=Player(2,"Alex",-50)
print(p2)
p3=Player(3, "Max", 150)
print(p3)