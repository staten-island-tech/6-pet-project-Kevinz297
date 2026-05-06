class Character:
    def __init__(self, name, energy):
        self.name = name
        self.energy = energy

    def get_base_stats(self):
        return f"Name: {self.name} | Energy: {self.energy}"
    
class Hero(Character):
    def __init__(self, name, energy):
        super().__init__(name, energy)
        self.bond = 0
        self.max_energy = 150
    def check_status(self):
        if self.bond >= 100:
            return "In Love"
        elif self.bond >= 50:
            return "Close Friends"
        return "Acquaintances"

class Friend(Character):
    def __init__(self, name, energy, trait):
        super().__init__(name, energy)
        self.trait = trait

player_name = input("Enter a name: ")
player = Hero(player_name, 100)
npc = Friend("Alex", 100, "Kind")
print(f"Adventure Start: {player.name} is meeting {npc.name} ({npc.trait}).")

while True:
    status = player.check_status()
    print("-" * 40)
    print(player.get_base_stats())
    print(f"Bond with {npc.name}: {player.bond} ({status})")
    print("-" * 40)
    if player.energy <= 0:
        print(f"{player.name} OVEREXHAUSTION")
        print("YOU LOSE")
        break
    if player.bond >= 100:
        print(f"Success! {player.name} and {npc.name} are now {status}!")
        print("YOU WIN")
        break

    print("Choose an action:")
    print("1. Hang out (-25 Energy, +20 Bond)")
    print("2. Deep Conversation (-40 Energy, +45 Bond)")
    print("3. Rest (+50 Energy)")
    print("4. Give up")
    
    choice = input("Action (1-4): ")

    if choice == "1":
        player.energy -= 25
        player.bond += 20
        print(f"> {player.name} and {npc.name} went for a walk.")
    elif choice == "2":
        player.energy -= 40
        player.bond += 45
        print(f"> {player.name} shared secrets with {npc.name}.")
    elif choice == "3":
        player.energy += 50
        if player.energy > player.max_energy:
            player.energy = player.max_energy
        print(f"> {player.name} took a long nap.")
    elif choice == "4":
        print("You Quit")
        break
    else:
        print("Invalid choice. Try again.")