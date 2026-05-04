class Hero:
    def __init__(self, name, energy, inventory, money):
        self.name = name
        self.energy = energy
        self.inventory = inventory
        self.bonds = {} 
        self.money = money 

    def happiness(self):
        if self.energy > 100:
            return "Happy"
        return "Sad"

    def spend(self, amount):
        if self.money >= amount:
            self.money -= amount
            return True
        else:
            print(f"Not enough coins! {self.name} only has {self.money}.")
            return False

    def buy(self, item, cost):
        print(f"\n{self.name} is trying to buy {item} for {cost} coins...")
        if self.spend(cost):
            self.inventory.append(item)
            print(f"Success! {item} was added to inventory.")
        else:
            print(f"Transaction failed.")

    def check_balance(self):
        print(f"{self.name}'s remaining balance: {self.money} coins")

    def hang_out_with(self, *friends):
        self.energy += 30
        for friend in friends:
            friend.energy += 30
            self.bonds[friend.name] = self.bonds.get(friend.name, 0) + 40
            friend.bonds[self.name] = friend.bonds.get(self.name, 0) + 40

    def check_relationship(self, friend):
        bond = self.bonds.get(friend.name, 0)
        if bond >= 100:
            return "In Love"
        elif bond >= 50:
            return "Friends"
        return "Acquaintances"

    def status(self):
        print(f"{self.name} | Energy: {self.energy} | Mood: {self.happiness()} | Bonds: {self.bonds}")

p002 = Hero("Player_002", 25, ["Fists"], 100)
p71 = Hero("Player_71", 40, ["Map"], 50)
p429 = Hero("Player_429", 10, ["Compass"], 10)

p002.buy("Sword", 40)
p002.check_balance()
p002.buy("Magic Armor", 200)
print(f"\n{p002.name}'s final inventory: {p002.inventory}")