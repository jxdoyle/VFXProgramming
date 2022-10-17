import os
os.system('cls' if os.name == 'nt' else 'clear')

class GameObject:
    def __init__(self, health):
        self.health = health
    def draw(self):
        print(f"GameObject Draw health: {self.health}")
        pass

class Controller:
    def movement(self):
        print("Controller Movement")
        pass

class Player(GameObject, Controller):
    def __init__(self, health):
        super().__init__(health)

    def draw(self): # Override draw method
        print("Player Draw")
        pass

    def move(self):
        print("Player Move")
        pass

class Boss(GameObject):
    def __init__(self):
        super().__init__(100)

    def ai(self):
        print("Boss AI")
        pass

gameObject = Player(100) # Instance of Player
gameObject.draw() # Inherited from GameObject
gameObject.move() # Method of Player Class
gameObject.movement() # Method of Controller

gameObject = Boss() # Instance of Boss
gameObject.draw() # Inherited from GameObject
gameObject.ai() # Method of Boss Class

