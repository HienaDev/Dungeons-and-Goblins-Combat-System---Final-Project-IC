import random
import string
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


#Function to create an array of characters
def allCharacters(characters):

    return (characters)


#Function to roll iniative of each character
def rollInitiative(character):

    d20 = random.randrange(1, 20)
    print(character["name"] + " rolled a " + str(d20) + " his turn order is: " + str(d20 + character["initiative"]))
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
    

def targetChoice(friendship):

    if (friendship == 0):
        while(True):
            attackDecision = input("Who do you want to attack? \n 1 - Spider \n 2 - Ogre \n 3 - Monster\n\n" ).translate({ord(c): None for c in string.whitespace}).lower()
            if (attackDecision == "1"):
                return goblin
            elif (attackDecision == "2"):
                return (ogre)
            elif (attackDecision == "3"):
                return goblinShaman
            else:
                print("You need to choose an enemy to attack\n")
                continue
    elif(friendship == 1):
        attackDecision = input("Who do you want to target? \n 1 - Warrior \n 2 - Priest\n\n" ).translate({ord(c): None for c in string.whitespace}).lower()
        if (attackDecision == "1"):
                return (priest)
        elif (attackDecision == "2"):
                return (warrior)
        else:
            print("You need to choose an enemy to attack\n")
            

    return (attackDecision)


#What rushdown spell does
def rushdown():
    
    d4=random.randrange(1,4)
    spellmpcost = 5

    if (warrior["mana"] < spellmpcost):

        print("You dont have enough mana to cast the spell!")

    else:
        enemy = targetChoice(0)
        print( enemy["name"] + " health before attack: " + str(enemy["health"]))
        enemy["health"] = enemy["health"] - (warrior["damage"] + d4)
        print("\nWarrior dealt ", end="")
        print(colored(str((warrior["damage"] + d4)), "red"), end ="")
        print(" damage to the " + enemy["name"] + "\n")
        print( enemy["name"] + " health after attack: " + str(enemy["health"]))
        
           
        
          
#What exorcism spell does
def exorcism():

    d4=random.randrange(1,4)
    spellmpcost = 5

    if (warrior["mana"] < spellmpcost):

        print("You dont have enough mana to cast the spell!")

    else:
        enemy = targetChoice(0)
        print( enemy["name"] + " health before attack: " + str(enemy["health"]))
        enemy["health"] = enemy["health"] - (d4 * 2)
        print("\nWarrior dealt " + str(2 * d4) + " damage to the " + enemy["name"] + "\n")
        print( enemy["name"] + " health after attack: " + str(enemy["health"]))
        
    pass

def mend():
    d6=random.randrange(1,6)
    spellmpcost = 3

    if (warrior["mana"] < spellmpcost):

        print("You dont have enough mana to cast the spell!")

    else:
        enemy = targetChoice(1)
        enemy["health"] = enemy["health"] + (d6 + priest["damage"])
        print("\nPriest healed " + str((warrior["damage"] + d6)) + " life points to the Warrior!\n")
        print( enemy["name"] + " health after attack: " + str(enemy["health"]))
    pass

def taunt():
    pass

def ArrowRain():
    pass

def poison():
    d4 = random.randrange(1,4)
    spellmpCost = 5


    if (warrior["mana"] < spellmpCost):

        print("You dont have enough mana to cast the spell!")

        enemy = targetChoice(0)
        print( enemy["name"] + " health before attack: " + str(enemy["health"]))
        enemy["health"] = enemy["health"] - (d4 * 2)
        print("\nWarrior dealt " + str(2 * d4) + " damage to the " + enemy["name"] + "\n")
        print( enemy["name"] + " health after attack: " + str(enemy["health"]))
    

    enemy = 0

    pass

def dmgReduction():
    enemy
    pass




#Warrior choosing a spell
def spellchooseW(character):

    while(True):
        print("--------------------------")
        choice = input("What spell will you choose: \n 1 - RushDown\n\n").translate({ord(c): None for c in string.whitespace}).lower()
        if (choice == "1" or choice == "rushdown"):
            rushdown()
            break
        else:
            print("You need to choose a spell\n")
            continue


#Priest choosing a spell
def spellChooseP(character):

    while(True):
        print(colored("--------------------------", ))
        choice = input("What spell will you choose: \n 1 - Exorcism \n 2 - Mend\n\n").translate({ord(c): None for c in string.whitespace}).lower()
        if (choice == "1" or choice == "exorcism"):
            exorcism()
            break
        elif (choice == "2" or choice == "mend"):
            mend()
            break
        else:
            print("\nYou have to choose a spell\n")
            pass



    
#def magicspells():
#    spells = ['rushdown', 'exorcism', 'mend']
#    if input ('rushdown')


#Function that shows character's attack order
def whoGoesFirst(characters):
    
    print("Turn order:\n")
    i = 0
    
    for x in characters:
        i += 1
        print(str(i) + " - " + x["name"])



#Function to know who is using each spell
def spellPhase(character):

    if (character["name"] == "Priest"):

        spellChooseP(character)

    elif (character["name"] == "Warrior"):

        spellchooseW(character)
    
    else:
        
        print(character["name"] + " uses a spell!")


#Function to attack
def attackPhase(character):

    print("\n" + character["name"] + " attacks\n")


#Function to decide what action each character does
def chooseAction(character):

    if (character["poisoned"] > 0):
        character["poisoned"] = character["poisoned"] - 1
        print(character["name"] + " is poisoned he takes " + colored(poisonDamage, "green", attrs=["bold"]) + " damage!")
        character["health"] = character["health"] - poisonDamage
        print("Health is now " + str(character["health"]) + colored("\nPoisoned", "green", attrs=["bold"]) + " turns left: " + str(character["poisoned"]))
    	

    while(True):

        print("--------------------------")
        print("You are: " + character["name"])
        choice = input("Would you like to: \n 1 - Attack \n 2 - Use a spell?\n\n").translate({ord(c): None for c in string.whitespace}).lower()

        if (choice == "1"):

            attackPhase(character)
            break

        elif (choice == "2"):

            spellPhase(character)
            break

        else:

            pass


#Function for every action in the action phase
def actionPhase(characters):

    for character in characters:

        chooseAction(character)


poisonDamage = 5
rogue = createCharacter(colored("Rogue", "white", attrs=["bold"]), 25, 10, 2, 5, 10, "good", 3)   
goblinShaman = createCharacter(colored("Goblin Shaman", "red", attrs=["bold"]), 30, 20, 23, 5, 6, "evil", 2)   
priest = createCharacter(colored("Priest", "white", attrs=["bold"]), 20, 25, 0, 2, 6, "good", 5)  
warrior = createCharacter(colored("Warrior", "white", attrs=["bold"]), 32, 5, 2, 5, 2, "good", 2)  
goblin = createCharacter(colored("Goblin", "red", attrs=["bold"]), 17, 5, 23, 5, 9, "evil", 1)
ogre = createCharacter(colored("Ogre", "red", attrs=["bold"]), 63, 5, 33, 10, 2, "evil", 0)

characters = allCharacters([rogue, goblinShaman, priest, warrior, goblin, ogre])
for x in characters:
    print(str(x))
order = turnOrder(characters)
print(str(order))
order, characters = sortOrder(order, characters)
print(str(order))
print("----------------------------------------")
whoGoesFirst(characters)
actionPhase(characters)

