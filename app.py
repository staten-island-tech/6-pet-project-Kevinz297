class Hero:
    def __init__(self, name, energy, inventory):
        self.name = name
        self.energy = energy
        self.inventory = inventory

    def buy(self, item):
        self.inventory.append(item)
        print(self.inventory)

    def happiness(self):
        if self.energy > 50:
            return "Happy"
        else:
            return "Sad"


Player_002 = Hero("Player_002", 25, ["Fists"])
Player_002.buy({"title": "Chocolate", "energy": 50})
print(Player_002.__dict__)