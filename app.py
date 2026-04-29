class Hero:
    def __init__(self, name, energy, inventory):
        self.name = name
        self.energy = energy
        self.inventory = inventory

    def buy(self, item):
        self.inventory.append(item)
        print(self.inventory)

    def eat(self, inventory, food):
        print("Would you like to eat this?")

        if input().lower() == "yes":
            self.inventory.remove(food)
            self.energy += food["energy"]
        else: print("Maybe next time.")
        
        print(f"{self.name} ate {food['title']} and gained {food['energy']} energy.")
        print(f"Current energy: {self.energy}")

    def happiness(self):
        if self.energy > 100:
            return "Happy"
        else:
            return "Sad"


Player_002 = Hero("Player_002", 25, ["Fists"])
Player_002.buy({"title": "Chocolate", "energy": 50})
print(Player_002.__dict__)