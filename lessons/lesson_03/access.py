import os
os.system('cls' if os.name == 'nt' else 'clear')

class GameObject:
    health = 100 # Public Attribute
    def __init__(self, damage, power, status):
        self.damage = damage # instance attribute
        self._power = power # Protected variable add a prefix _ (single underscore)
        self.__status = status # Private variable add a prefix __ (double underscore)
    
    def getStatus(self):
        return self.__status

class Player(GameObject):
    rank = 10 # Public Attribute
    def __init__(self, name, damage, power, status):
        self.name = name # instance attribute
        super().__init__(damage, power, status)

player = Player("MuddyGames", 10, 20, "alive")
print(player.health)
print(player.rank)
print(player._power)
# print(player.__status) wont work on private variable
print(player.getStatus())