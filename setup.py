
#items Classes
class Item():
    def __init__(self) -> None:
        self.price = 0
        self.type = None
        self.effect = None
        self.descr = ""

class Knife(Item) :
    def __init__(self) -> None:
        super().__init__()
        self.price = 50
        self.type = "Attack"
        self.damageboost = 2
        self.effect = "Bleed"
        self.descr = "Knife"

    def __str__(self) -> str:
        return "A dishonored and disgusting weapon, but an effective and popular one"

class Gloves(Item) :
    def __init__(self) -> None:
        super().__init__()
        self.price = 50
        self.type = "Attack"
        self.damageboost = 1.5
        self.effect = "Shock"
        self.descr = "Gloves"
    
    def __str__(self) -> str:
        return "Yeah, that's for a real men. Float like a butterfly, sting like a bee"

class Chain(Item) :
    def __init__(self) -> None:
        super().__init__()
        self.price = 30
        self.type = "Attack"
        self.damageboost = 1.5
        self.effect = "Painful"
        self.descr = "Chain"

    def __str__(self) -> str:
        return "Strange zoomer fashion element. It can harm anybody though"

class Thermos(Item) :
    def __init__(self) -> None:
        super().__init__()
        self.price = 15
        self.type = "Attack"
        self.damageboost = 1.25
        self.effect = "Painful"
        self.descr = "Thermos"
    
    def __str__(self) -> str:
        return "A heavy metal thing. Do some madmen use it to fight? :/"

class Stick(Item) :
    def __init__(self) -> None:
        super().__init__()
        self.price = 15
        self.type = "Attack"
        self.damageboost = 1.25
        self.effect = "Painful"
        self.descr = "Stick"
    
    def __str__(self) -> str:
        return "A usual walking stick (at first sight at least)"

class Energy(Item) :
    def __init__(self) -> None:
        super().__init__()
        self.price = 10
        self.type = "Support"
        self.damageboost = 3
        self.descr = "Energy"
    
    def __str__(self) -> str:
        return "Increases your overall power for a while and restores your hp. Never drink it everyday irl."


#locations Classes
class Location():
    def __init__(self) -> None:
        self.enemy = None
        self.feature = None
        self.neighbour = None

class Iskra(Location) :
    def __init__(self) -> None:
        super().__init__()
        self.feature = "Market"
        self.neighbour = Dovzhenka()
    
    def __str__(self) -> str:
        return f"Iskra Market. There is a {self.feature}. You might take a look." +  (f" Oh, and there is {self.enemy.name} - your enemy." if self.enemy.beaten==None else "")

class Dovzhenka(Location):
    def __init__(self) -> None:
        super().__init__()
        self.feature = "Training fields"
        self.neighbour = UpperShuvar()
    def __str__(self) -> str:
        return f"Dovzhenka Cinema. There is a {self.feature}. You might take a look." +  (f" Oh, and there is {self.enemy.name} - your enemy." if self.enemy.beaten==None else "")

class UpperShuvar(Location):
    def __init__(self) -> None:
        super().__init__()
        self.feature = "Market"
        self.neighbour = LowerShuvar()

    def __str__(self) -> str:
        return f"Upper Shuvar Market. There is a {self.feature}. You might take a look." +  (f" Oh, and there is {self.enemy.name} - your enemy." if self.enemy.beaten==None else "")

class LowerShuvar(Location):
    def __init__(self) -> None:
        super().__init__()
        self.feature = "Church"
        self.neighbour = Crossroads()

    def __str__(self) -> str:
        return f"Lower Shuvar Market. There is a {self.feature}. You might take a look." +  (f" Oh, and there is {self.enemy.name} - your enemy." if self.enemy.beaten==None else "")

class Crossroads(Location):
    def __init__(self) -> None:
        super().__init__()
        self.neighbour = "Final"

    def __str__(self) -> str:
        return f"Crossroads. Your final destination." +  (f" Oh, and there is {self.enemy.name} - your enemy." if self.enemy.beaten==None else "")


#characters Classes
class Player():
    def __init__(self, name) -> None:
        self.money = 100
        self.hp = 100
        self.damage = 10
        self.agility = 10
        self.inteligence = 100
        self.charisma = 50
        self.name = name
        self.pack = []
        self.beaten = None

class Gopnik(Player):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.hp += 10
        self.damage += 5
        self.agility -= 5
        self.inteligence -= 10
        self.charisma += 20
        self.type = "Gopnick"
        self.pack.append(Knife())

    def __str__(self) -> str:
        return "A dangerous-looking guy. Nobody would ask him what time it is."

class Turnickman(Player):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.hp += 20
        self.damage += 10
        self.agility -= 9
        self.inteligence -= 15
        self.charisma += 30
        self.type = "Turnickman"
        self.pack.append(Gloves())

    def __str__(self) -> str:
        return "That fit one looks dangerous. He wasn't definitely spending time reading books."

class Zoomer(Player):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.hp -= 10
        self.damage -= 1
        self.agility += 10
        self.inteligence += 5
        self.charisma -= 5
        self.type = "Zoomer"
        self.pack.append(Chain())

    def __str__(self) -> str:
        return "A carefree young boy. Smart and swift."

class Student(Player):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.hp += 5
        self.damage -= 2
        self.agility += 5
        self.inteligence += 20
        self.charisma -= 10
        self.type = "Student"
        self.pack.append(Thermos())

    def __str__(self) -> str:
        return "A tired, strange man with no weapons. Don't try to fool him."

class Granny(Player):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.hp -= 10
        self.damage -= 5
        self.agility -= 10
        self.inteligence += 10
        self.charisma += 30
        self.type = "Granny"
        self.pack.append(Stick())

    def __str__(self) -> str:
        return "An old, wise and respected woman. Looking a bit aggressive, to be honest."
