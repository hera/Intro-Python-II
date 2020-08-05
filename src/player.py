class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def __repr__(self):
        return f"Player(name={self.name}, current_room={self.current_room})"

    def __str__(self):
        return f"{self.name} in {self.current_room}"

    def set_room(self, room):
        self.current_room = room