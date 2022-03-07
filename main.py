import random
import setup

def setting():
    name = input("Type your name first. Think about it for a while, you know...\n>>> ")
    try:
        your_type = int(input("Whom do you feel most? Type 0 for Gopnick, 1 for Turnickman, 2 for Zoomer, 3 for Student and 4 for Granny \n>>> "))
        you = setup.Gopnik(name) if your_type == 0 else setup.Turnickman(name) if your_type == 1 else setup.Zoomer(name) if your_type == 2 else setup.Student(name) if your_type == 3 else setup.Granny(name)
        return name, you
    except ValueError:
        print("Okay. I think you should read before play.")
        return setting()
    
current_stage = setup.Iskra()
name, you = setting()
print("All your friends are avid partygoers. So are you - of course, would you be friends otherwise?")
print("But you live in Sykhiv district. Every of your attempts to get out of this pretty village end up in the Battle of the Five Armies.")
print("Today is the same day as always.")



def fight(enemy, you):
    if you.hp <= 0:
        return "Lose"
    if enemy.hp <= 0:
        current_stage.enemy.beaten = True
        return you
    else :
        print(f"Your pack : {[x.descr for x in you.pack]}")
        weapon = input("Print i to consider your enemy. Write the name of your weapon to hit. Print f to try to fool an enemy and s to try to scare your enemy: \n>>> ")

        if weapon == "i":
            print(current_stage.enemy.type)
            print(str(current_stage.enemy)+"\n")
            return fight(enemy, you)

        elif weapon == "f":
            chance = (you.inteligence/current_stage.enemy.inteligence * 100) - random.randint(0, 50)
            if random.randint(0, 100) > chance:
                print("You couldn't fool him and got a strike. Damn.")
                you.hp -= 20
                return fight(enemy, you)
            elif random.randint(0, 100) <= chance:
                print("Heh, what a fool! Easy win)")
                enemy.hp -= 200
                return fight(enemy, you)

        elif weapon == "s":
            chance = (you.charisma/current_stage.enemy.charisma * 100) - random.randint(0, 50)
            if random.randint(0, 100) > chance:
                print("You couldn't scare him. Damn. Your hp got lower.")
                you.hp -= 20
                return fight(enemy, you)
            elif random.randint(0, 100) <= chance:
                print("Heh, what a coward! Easy win)")
                enemy.hp -= 200
                return fight(enemy, you)

        elif weapon in [x.descr for x in you.pack]:
            weapon = [x for x in you.pack if x.descr == weapon][0]
            enemy.hp -= you.damage * weapon.damageboost
            you.hp -= enemy.damage
            print(f"A good strike! You got also though. Your chance to win : {'High' if you.hp > enemy.hp else 'Low'}")
            if weapon.type == "Support":
                you.pack.remove(weapon)
            return fight(enemy, you)
        else :
            print(f"No {weapon} in your pack")
            return fight(enemy, you)

def use_local():
    if current_stage.feature == "Market":
        print("Your money : " + str(you.money) + ", your pack : " + str([x.descr for x in you.pack]))
        items = [setup.Stick(), setup.Thermos(), setup.Chain(), setup.Energy(), setup.Gloves(), setup.Knife()]
        for i in items :
            print(type(i).__name__ + " : " + str(i.price))
        to_buy = input("Type 0 if you wanna buy nothing. If you want to buy an item, write it's name.\n>>> ")
        if to_buy in ["Stick", "Thermos", "Chain", "Energy", "Gloves", "Knife"] :
            to_append = ["Stick", "Thermos", "Chain", "Energy", "Gloves", "Knife"].index(to_buy)
            if items[to_append].price <= you.money :
                you.pack.append(items[to_append])
                you.money -= items[to_append].price
                use_local()
            else :
                print("Not enough money")
                use_local()
        elif to_buy == "0":
            return
        else :
            print("No such item on market : " + to_buy)
            use_local()
    elif current_stage.feature == "Training fields":
        print("Your money : " + str(you.money))
        to_train = input("If you're to cool to train, type 0. You can become fitter by paying some money type 1 \n>>> ")
        if to_train == "0" :
            return
        elif to_train == "1" and you.money >= 10 :
            you.hp += 10
            you.damage += 5
            you.agility += 5
            you.money -= 10
        else :
            print("Improper input. Get more cash or type proper command")
            use_local()
    elif current_stage.feature == "Church":
        print("Do you have some money? Donate it to church. You'd better do so.")
        to_decide = input("Type 0 to donate money. Type 1 if you are a poor atheist.\n>>> ")
        if to_decide == "0" and you.money >=10:
            print("Very good. May God bless you!")
            you.money -= 10
            return
        elif to_decide == "1":
            print("A granny decided to scream on you. Welp...")
            you.charisma -= 10
            return
        else :
            print("Type proper input : 0 or 1.")
            use_local()


while True:
    try :
        def take_input():
            try :
                action = int(input("What will you do now? Type" + (f" 0 for fight," if current_stage.enemy.beaten==None else " 0 for passing to the next checkpoint")+ (" 1 for using local features: \n>>> " )))
                return action
            except ValueError :
                print("Type proper input")
                return take_input()

        if current_stage.enemy == None or current_stage.enemy.beaten == None:
            current_stage.enemy = random.choice([setup.Gopnik("Sanya"), setup.Turnickman("Nazik"), setup.Zoomer("Svitozar"), setup.Student("Sergo"), setup.Granny("Orys'ka")])
        print("\n"+str(current_stage))
        action = take_input()
        if action == 0 and current_stage.enemy.beaten != True:
            result = fight(current_stage.enemy, you)
            print("Your hp : " + str(you.hp) + ", enemy hp : "+ str(current_stage.enemy.hp))
            if type(result)==str:
                print("Too uncareful! You got beaten and went home. Better luck next time!")
                break
            else:
                print("Huh. That was a tough fight. As usual. Go forward. Don't forget to heal by drinking energy drink.")
                you.money += 50
        elif action == 0 and current_stage.enemy.beaten == True:
            current_stage = current_stage.neighbour
            pass
        elif action == 1 :
            use_local()
        else :
            print("Wrong input.")
            pass
    except AttributeError :
        print("That was easier than it looked. Don't forget you've come here to have fun. There your friends are!")
        break

