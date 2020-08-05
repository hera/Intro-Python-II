class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []

    def __repr__(self):
        return f"Player(name={self.name}, current_room={self.current_room})"

    def __str__(self):
        return f"{self.name} in {self.current_room}"

    def set_room(self, room):
        self.current_room = room

    def add_item(self, item):
        self.items.append(item)
        print(f"You've taken a {item.name}.")
    
    def remove_item(self, item_name):
        for index in range(len(self.items)):
            if self.items[index].name == item_name:
                return self.items.pop(index)
        print(f"There's no {item_name} in your bag.")
        return None

    def show_items(self):
        print("\nYour bag now contains:")
        for item in self.items:
            print(f"{item.name}\t {item.description}")
        if not len(self.items):
            print("Nothing")