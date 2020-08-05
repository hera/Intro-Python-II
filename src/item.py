class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return f"Item(name={self.name}, description={self.description})"

    def __str__(self):
        return self.name


class Gem(Item):
    def __init__(self):
        super().__init__("Gem", "Purple and shiny.")

class Sword(Item):
    def __init__(self):
        super().__init__("Sword", "Nice and sharp.")

class Stone(Item):
    def __init__(self):
        super().__init__("Stone", "Just a stone.")

class Knife(Item):
    def __init__(self):
        super().__init__("Knife", "May come in handy.")

class Coin(Item):
    def __init__(self):
        super().__init__("Coin", "Every penny counts.")

