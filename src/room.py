class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None
        self.items = []

    def __repr__(self):
        return f"Room(name={self.name}, description={self.description})"

    def __str__(self):
        return f"You are in {self.name}.\n\n{self.description}"

    def add_item(self, item):
        self.items.append(item)

    def show_items(self):
        print("\nThis place contains:")
        for item in self.items:
            print(f"{item.name}\t {item.description}")
        if not len(self.items):
            print("Nothing")
    
    def remove_item(self, item_name):
        for index in range(len(self.items)):
            if self.items[index].name == item_name:
                return self.items.pop(index)
        print(f"There's no {item_name} in this room.")
        return None