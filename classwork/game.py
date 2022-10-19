import random
import os
os.system('cls' if os.name == 'nt' else 'clear')

class GameObject:
    def __init__(self, name, score = 0, health = 100):
        self.name = name
        self.score = score
        self.health = health
    
    def getName(self):
        return self.name

    def getScore(self):
        return self.score
        
    def updateScore(self, score):
        self.score = self.score + score

    def getHealth(self):
        return self.health
    
    def updateHealth(self, damage):
        self.health = self.health - damage

    def __str__(self) -> str:
        return f"{self.name} " + "\n" + f"Score: {self.score}"

class Player(GameObject):
    def __init__(self, player_name):
        super().__init__(player_name)

class Boss(GameObject):
    def __init__(self, boss_name):
        super().__init__(boss_name)

player = Player("Daisy")
boss = Boss("Morgoth")

### simple game with 3 rounds where either the player or boss wins
# have player and boss do random damage to each other between 1-30
# the one with the most health after "wins"

rounds = 3
for i in range(rounds):
    print("Round: " + str(i+1))
    player_damage = random.randint(1,30)
    player.updateHealth(player_damage)
    print(f"Player Health Remaining: {player.getHealth()}")

    boss_damage = random.randint(1,30)
    boss.updateHealth(boss_damage)
    print(f"Boss Health Remaining: {boss.getHealth()}")

    if i == 2 and player.getHealth() >= boss.getHealth():
        player.updateScore(100)
        print("\n" + f"Winner: {player}")

    if i == 2 and player.getHealth() < boss.getHealth():
        boss.updateScore(100)
        print("\n" + f"Winner: {boss}")
