import random
import string
from termcolor import colored, cprint  #run on console: pip install termcolor
import time
import os

#Function to create a character
def createCharacter(name, health, mana, armor, damage, initiative, loyalty, poisoned, alive):

    character = {
        "name" : name,
        "health" : health,
        "mana" : mana,
        "armor" : armor,
        "damage" : damage,
        "initiative" : initiative,
        "loyalty" : loyalty,
        "poisoned" : poisoned,
        "alive" : alive
    }

    return (character)


#Function to create an array of characters
def allCharacters(characters):

    return (characters)


#Function to roll iniative of each character
def rollInitiative(character):

    d20 = random.randrange(1, 20)
    print("\n" + character["name"] + " rolled a " + str(d20) + " his iniative is: " + colored(str(d20 + character["initiative"]), "yellow"))
    time.sleep(2)
    return (d20 + character["initiative"])


#Function that creates a tuple with the iniative roll of each character
def turnOrder(characters):

    order = []

    for character in characters:

        order.append(rollInitiative(character))
    
    return(order)


#Function to sort the character list by iniative order
def sortOrder(order, characters):

    auxTurn = 0
    auxCharacter = ""

    for i in range(len(order)):

        for x in range(len(order)):

            if (x < len(order) - 1):

                if (order[x] < order[x + 1]):

                    #Swap order if iniative in next index is higher
                    auxTurn = order[x]
                    order[x] = order[x + 1]
                    order[x + 1] = auxTurn  

                    #If iniative in next index is smaller also swap character order in the characters array
                    auxCharacter = characters[x]
                    characters[x] = characters[x + 1]
                    characters[x + 1] = auxCharacter

                    
    return(order, characters)
    

def printChoices(loyalty):

    choiceIndex = 0
    print("Who do you want to target? ")
    for x in characters:
        if (x["loyalty"] == loyalty):
            choiceIndex += 1
            print("\n " + str(choiceIndex) + " - " + x["name"], end= "")
            print(" [ " + colored("HP: " , "green") + str(x["health"]), end = " /")
            print(colored(" Mana ", "blue") + str(x["mana"]), end = " /")
            print(colored(" Armor: ", "grey") + str(x["armor"]), end = " /")
            print(colored(" Damage: ", "red") + str(x["damage"]), end = " /")
            print(colored(" Poisoned: ", "green" , attrs= ["bold"]) + str(x["poisoned"]) + " ]")

    print("\n 0 - Go Back")


def targetChoice(friendship):

    if (friendship == 0):
        while(True):

            printChoices("evil")

            attackDecision = input("\n").translate({ord(c): None for c in string.whitespace}).lower()
            
            if (attackDecision == "1" or attackDecision == "goblin"):

                return (goblin)
            
            elif (attackDecision == "2" or attackDecision == "ogre"):

                return (ogre)
            
            elif (attackDecision == "3" or attackDecision == "goblinshaman"):

                return (goblinShaman)
            
            elif (attackDecision == "0"):

                return ("0")
            else:
                clear()
                print("You need to choose an " + colored("Enemy", "red", attrs=["bold"]) + " to attack\n")
                continue

    elif(friendship == 1):

        printChoices("good")

        attackDecision = input("\n" ).translate({ord(c): None for c in string.whitespace}).lower()
        if (attackDecision == "1"):
                return (warrior)
        elif (attackDecision == "2"):
                return (priest)
        else:
            print("You need to choose an " + colored("Ally", "white", attrs=["bold"]) + "!\n")
            

    return (attackDecision)


#What rushdown spell does
def rushdown():
    
    d4=random.randrange(1,4)
    spellmpcost = 5

    if (warrior["mana"] < spellmpcost):

        print("You dont have enough mana to cast the spell!")

    else:
        target = targetChoice(0)
        if (target == "0"):
            return ("0")
        print( target["name"] + " health before attack: " + str(target["health"]))
        target["health"] = target["health"] - (warrior["damage"] + d4)
        print("\nWarrior dealt " + colored(str((warrior["damage"] + d4)), "red", attrs=["bold"]) + " damage to the " + target["name"] + "\n")
        print( target["name"] + " health after attack: " + str(target["health"]))
        
           
        
          
#What exorcism spell does
def exorcism():

    d4=random.randrange(1,4)
    spellmpcost = 5

    if (warrior["mana"] < spellmpcost):

        print("You dont have enough mana to cast the spell!")

    else:
        target = targetChoice(0)
        if (target == "0"):
            return ("0")
        print( target["name"] + " health before attack: " + str(target["health"]))
        target["health"] = target["health"] - (d4 * 2)
        print("\nWarrior dealt " + str(2 * d4) + " damage to the " + target["name"] + "\n")
        print( target["name"] + " health after attack: " + str(target["health"]))
        
    pass

def mend():
    d6=random.randrange(1,6)
    spellmpcost = 3

    if (warrior["mana"] < spellmpcost):

        print("You dont have enough mana to cast the spell!")

    else:

        target = targetChoice(1)
        if (target == "0"):
            return ("0")
        target["health"] = target["health"] + (d6 + priest["damage"])
        print("\nPriest healed " + str((warrior["damage"] + d6)) + " life points to the Warrior!\n")
        print( target["name"] + " health after attack: " + str(target["health"]))

    pass

def poison(character):
    
    d4=random.randrange(1,4)
    character["Poison"] = (character["Poison"] + d4)
    print("Character gets poisonend for " + d4 +" rounds!")


def protection(character):
    if character["loyalty"] == "evil":
        goblinShaman
    elif character["loyalty"] == "good":
        priest
    pass

    characters["armor"] *2

    pass

def rest(characters):
    if characters["mana"] == 0:
        characters["mana"] == characters["mana"] + int(characters["mana"] * 2)



#Warrior choosing a spell
def spellChooseW(character):
    spellMpCost = 5
    if (warrior["mana"] < spellMpCost):
        pass

    while(True):

        print("--------------------------")
        choice = input("What spell will you choose: \n 1 - RushDown \n 0 - Go Back\n\n").translate({ord(c): None for c in string.whitespace}).lower()

        if (choice == "1" or choice == "rushdown"):

            if (rushdown() == "0"):
                continue
            break
        
        elif (choice == "0"):

            return ("0")

        else:

            print("You need to choose a spell\n")
            continue


#Priest choosing a spell
def spellChooseP(character):

    while(True):

        print(colored("--------------------------", ))
        choice = input("What spell will you choose: \n 1 - Exorcism \n 2 - Mend \n 0 - Go Back\n\n").translate({ord(c): None for c in string.whitespace}).lower()

        if (choice == "1" or choice == "exorcism"):

            if (exorcism() == "0"):
                continue
            break

        elif (choice == "2" or choice == "mend"):

            if (mend() == "0"):
                continue
            break
        
        elif (choice == "0"):

            return ("0")

        else:

            print("\nYou have to choose a spell\n")
            pass

def spellChooseP(character):

    while(True):

        print(colored("--------------------------", ))
        choice = input("What spell will you choose: \n 1 - Exorcism \n 2 - Mend \n 0 - Go Back\n\n").translate({ord(c): None for c in string.whitespace}).lower()

        if (choice == "1" or choice == "exorcism"):

            if (exorcism() == "0"):
                continue
            break

        elif (choice == "2" or choice == "mend"):

            if (mend() == "0"):
                continue
            break
        
        elif (choice == "0"):

            return ("0")

        else:

            print("\nYou have to choose a spell\n")
            pass



def spellChooseGS(character):
    
    spellMpCost = 3

    if (goblinShaman["mana"] < spellMpCost):

        print("You dont have enough mana to cast the spell!")


    while(True):
        print(colored("--------------------------", ))
        choice = input("What spell will you choose: \n 1 - Poison \n 2 - Protection\n\n").translate({ord(c): None for c in string.whitespace}).lower()
        if (choice == "1" or choice == "Poison"):
            poison()
            break
        elif (choice == "2" or choice == "protection"):
            protection()
            break
        else:
            print("\nYou have to choose a spell\n")
            pass



#Function that shows character's attack order
def whoGoesFirst(characters):
    
    print("Turn order:\n")

    i = 0
    
    for x in characters:

        i += 1
        print(str(i) + " - " + x["name"])



#Function to know who is using each spell
def spellPhase(character):

    if (character["name"] == priest["name"]):

        if (spellChooseP(character) == "0"):
            return("0")
        return ("1")

    elif (character["name"] == warrior["name"]):

        if (spellChooseW(character) == "0"):
            return("0")
        return("1")
    
    else:
        
        print(character["name"] + " uses a spell!")
        return("1")


#Function to attack
def attackPhase(character):

    if (character["loyalty"] == "good"):

        target = targetChoice(0)

        if (target == "0"):
            return "0"

        print(character["name"] + " attacks " + target["name"])


        if ((character["damage"] - target["armor"]) > 0):
            target["health"] = target["health"] - (character["damage"] - target["armor"])
            print( target["name"] + " took " + colored(str(character["damage"] - target["armor"]), "red", attrs = ["bold"]) + " damage!")
            print(target["name"] + " now has " + colored(str(target["health"]), "green", attrs = ["bold"]) + " health!")
        else:
            print (target["name"] + " took no damage!")
        

    elif (character["loyalty"] == "evil"):

        print(character["name"] + " is deciding what to do...")
        time.sleep(5)

        target = random.randrange(1, 3)
       

        if (target == 1):
            target = priest
        elif (target == 2):
            target = warrior    
        elif (target == 3):
            target = rogue
        
        print(character["name"] + " attacks " + target["name"])

        if ((character["damage"] - target["armor"]) > 0):
            target["health"] = target["health"] - (character["damage"] - target["armor"])
            print( target["name"] + " took " + colored(str(character["damage"] - target["armor"]), "red", attrs = ["bold"]) + " damage!")
            print(target["name"] + " now has " + colored(str(target["health"]), "red", attrs = ["bold"]) + " health!")
        else:
            print (target["name"] + " took no damage!")
        



#Function to decide what action each character does
def chooseAction(character):

    if (character["alive"] == 1):

        if (character["poisoned"] > 0 and character["health"] > 0):

            character["poisoned"] = character["poisoned"] - 1
            print("\n" + character["name"] + " is poisoned he takes " + colored(poisonDamage, "green", attrs=["bold"]) + " damage!")
            character["health"] = character["health"] - poisonDamage
            print("Health is now " + str(character["health"]) + colored("\nPoisoned", "green", attrs=["bold"]) + " turns left: " + str(character["poisoned"]) + "\n")
        
        if (character["health"] <= 0 and character["alive"] == 1):

            print(colored("--------------------------", "red",  attrs=["bold"]))
            print(" " + character["name"] + " is downed!")
            print(colored("--------------------------", "red",  attrs=["bold"]))
            character["alive"] = 0
            character["health"] = 0

        while(True and character["alive"] == 1):
            
            if (character["loyalty"] == "good"):

                print("--------------------------")
                print("You are: " + character["name"])
                choice = input("Would you like to: \n 1 - Attack \n 2 - Use a spell?\n\n").translate({ord(c): None for c in string.whitespace}).lower()

            else:

                choice = "1"


            if (choice == "1"):

                if (attackPhase(character) != "0"):
                    break
                
                else: 
                    pass

            elif (choice == "2"):

                if (spellPhase(character) != "0"):
                    break
            else:

                pass
    



#Function for every action in the action phase
def actionPhase(characters):

    for character in characters:
        
        chooseAction(character)


def whoWon():

    if (warrior["health"] + priest["health"] + rogue["health"]  <= 0):
        
        print(colored (" __     __ ____   _    _    _       ____    _____  _______ ", "red"))
        print(colored (" \ \   / // __ \ | |  | |  | |     / __ \  / ____||__   __|", "red"))
        print(colored ("  \ \_/ /| |  | || |  | |  | |    | |  | || (___     | |   ", "red"))
        print(colored ("   \   / | |  | || |  | |  | |    | |  | | \___ \    | |   ", "red"))
        print(colored ("    | |  | |__| || |__| |  | |____| |__| | ____) |   | |   ", "red"))
        print(colored ("    |_|   \____/  \____/   |______|\____/ |_____/    |_|   ", "red"))
        print("\n")
                                                                
    elif (ogre["health"] + goblin["health"] + goblinShaman["health"] <= 0 ):

        print(colored ("__     __ ____   _    _  __          __ _____  _   _ ", "yellow"))
        print(colored ("\ \   / // __ \ | |  | | \ \        / /|_   _|| \ | |", "yellow"))
        print(colored (" \ \_/ /| |  | || |  | |  \ \  /\  / /   | |  |  \| |", "yellow"))
        print(colored ("  \   / | |  | || |  | |   \ \/  \/ /    | |  | . ` |", "yellow"))
        print(colored ("   | |  | |__| || |__| |    \  /\  /    _| |_ | |\  |", "yellow"))
        print(colored ("   |_|   \____/  \____/      \/  \/    |_____||_| \_|", "yellow"))
        print("\n")

    else:
        print("It's a tie?")

#Initializing Variables

clear = lambda: os.system('cls')

poisonDamage = 5
rogue = createCharacter(colored("Rogue", "white", attrs=["bold"]), 30, 10, 2, 5, 10, "good", 0, 1)   
goblinShaman = createCharacter(colored("Goblin Shaman", "red", attrs=["bold"]), 20, 20, 23, 5, 6, "evil", 0, 1)   
priest = createCharacter(colored("Priest", "white", attrs=["bold"]), 20, 25, 0, 2, 6, "good", 0, 1)  
warrior = createCharacter(colored("Warrior", "white", attrs=["bold"]), 32, 5, 2, 5, 2, "good", 0, 1)  
goblin = createCharacter(colored("Goblin", "red", attrs=["bold"]), 30, 5, 23, 5, 9, "evil", 0, 1)
ogre = createCharacter(colored("Ogre", "red", attrs=["bold"]), 63, 5, 33, 10, 2, "evil", 0, 1)

characters = allCharacters([rogue, goblinShaman, priest, warrior, goblin, ogre])


while(warrior["health"] + priest["health"] + rogue["health"]  > 0 and ogre["health"] + goblin["health"] + goblinShaman["health"] > 0 ):

    clear()
    order = turnOrder(characters)
    order, characters = sortOrder(order, characters)
    time.sleep(3)
    print("----------------------------------------")
    whoGoesFirst(characters)
    actionPhase(characters)

whoWon()