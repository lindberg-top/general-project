class Character:
    def __init__(self, hp, armour, name):
        self.hp = hp
        self.armour = armour
        self.name = name
        
    def attack(self):
        print(f"{self.name} атакует!")
        
    
    def hp(self):
        print(f"{self.hp} ")