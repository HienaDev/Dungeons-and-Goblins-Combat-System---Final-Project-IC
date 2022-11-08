import sys
from termcolor import colored, cprint  #run on console: pip install termcolor


#Function to create a character
def createCharacter(name, health, mana, armor, damage, initiative, loyalty, poisoned):

    character = {
        "name" : name,
        "health" : health,
        "mana" : mana,
        "armor" : armor,
        "damage" : damage,
        "initiative" : initiative,
        "loyalty" : loyalty,
        "poisoned" : poisoned
    }

    return (character)


rogue = createCharacter(colored("Rogue", "white", attrs=["bold"]), 25, 10, 2, 5, 10, "good", 3)   
goblinShaman = createCharacter(colored("Goblin Shaman", "red", attrs=["bold"]), 30, 20, 23, 5, 6, "evil", 2)   
priest = createCharacter(colored("Priest", "white", attrs=["bold"]), 20, 25, 0, 2, 6, "good", 5)  
warrior = createCharacter(colored("Warrior", "white", attrs=["bold"]), 32, 5, 2, 5, 2, "good", 2)  
goblin = createCharacter(colored("Goblin", "red", attrs=["bold"]), 17, 5, 23, 5, 9, "evil", 1)
ogre = createCharacter(colored("Ogre", "red", attrs=["bold"]), 63, 5, 33, 10, 2, "evil", 0)


