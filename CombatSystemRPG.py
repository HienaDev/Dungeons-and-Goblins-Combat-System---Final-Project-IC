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
        "maxHealth" : health,
        "mana" : mana,
        "maxMana" : mana,
        "armor" : armor,
        "damage" : damage,
        "initiative" : initiative,
        "loyalty" : loyalty,
        "poisoned" : poisoned,
        "alive" : alive
    }

    return (character)


#Function to roll iniative of each character
def rollInitiative(character):

    d20 = random.randrange(1, 20)
    if (character["alive"] == 1):
        print("\n" + character["name"] + " rolled a " + str(d20) + " his iniative is: " + colored(str(d20 + character["initiative"]), "yellow"))
        time.sleep(1.5)
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

        for x in range(len(order) - 1):

            if (order[x] < order[x + 1]):

                #Swap order if iniative in next index is higher
                auxTurn = order[x]
                order[x] = order[x + 1]
                order[x + 1] = auxTurn  

                #If iniative in next index is smaller also swap character order in the characters array
                auxCharacter = characters[x]
                characters[x] = characters[x + 1]
                characters[x + 1] = auxCharacter
            
            elif (order[x] == order[x + 1]):

                if (characters[x]["initiative"] < characters[x + 1]["initiative"]):
                    auxTurn = order[x]
                    order[x] = order[x + 1]
                    order[x + 1] = auxTurn  

                    auxCharacter = characters[x]
                    characters[x] = characters[x + 1]
                    characters[x + 1] = auxCharacter

                    
    return(order, characters)
    

def printChoices(loyalty):

    choiceIndex = 0
    print("Who do you want to target? ")
    for x in charactersUnsorted:
        if (x["loyalty"] == loyalty):
            choiceIndex += 1
            print("\n " + str(choiceIndex) + " - " + x["name"], end= "")
            print(" [ " + colored("HP: " , "green") + str(x["health"]) + "/" + str(x["maxHealth"]), end = " |")
            print(colored(" Mana ", "blue") + str(x["mana"]), end = " |")
            print(colored(" Armor: ", "grey") + str(x["armor"]), end = " |")
            print(colored(" Damage: ", "red") + str(x["damage"]), end = " |")
            print(colored(" Poisoned: ", "green" , attrs= ["bold"]) + str(x["poisoned"]) + " ]")

    print("\n 0 - Go Back")


def targetChoice(friendship):

    if (friendship == 0):
        while(True):

            printChoices("evil")

            attackDecision = input("\n").translate({ord(c): None for c in string.whitespace}).lower()
            
            if ((attackDecision == "1" and goblin["alive"] == 1) or (attackDecision == "goblin" and goblin["alive"] == 1)):

                return (goblin)
            
            elif ((attackDecision == "2" and ogre["alive"] == 1) or (attackDecision == "ogre" and ogre["alive"] == 1)):

                return (ogre)
            
            elif ((attackDecision == "3" and goblinShaman["alive"] == 1) or (attackDecision == "goblinshaman" and goblinShaman["alive"] == 1)):

                return (goblinShaman)
            
            elif (attackDecision == "0"):

                return ("0")
            else:
                clear()
                print("----------------------------------------")
                print("You need to choose a valid " + colored("Enemy", "red", attrs=["bold"]) + " to attack\n")
                print("----------------------------------------")
                continue

    elif(friendship == 1):

        while (True):

            printChoices("good")

            attackDecision = input("\n" ).translate({ord(c): None for c in string.whitespace}).lower()
            if ((attackDecision == "1" and rogue["alive"] == 1) or (attackDecision == "rogue" and rogue["alive"] == 1)):

                    return (rogue)

            elif ((attackDecision == "2" and priest["alive"] == 1) or (attackDecision == "priest" and priest["alive"] == 1)):

                    return (priest)

            elif ((attackDecision == "3" and warrior["alive"] == 1) or (attackDecision == "warrior" and warrior["alive"] == 1)):

                    return (warrior)

            elif (attackDecision == "0"):

                return ("0")

            else:
                clear()
                print("-----------------------------")
                print("You need to choose a valid " + colored("Ally", "white", attrs=["bold"]) + "!")
                print("-----------------------------\n")
            

    return (attackDecision)

def shield():

    spellmpcost = 8

    if (goblinShaman["mana"] < spellmpcost):

        print("You dont have enough mana to cast the spell!")

    else: 

        print(colored("\n-----------------------------", "red"))
        print(goblinShaman["name"] + "gives shield  " + colored("enemy", "red") + "!\n")
        pass





#What the arrow rain spell does
def arrowRain():

    d10 = random.randrange(1,10)
    spellmpcost = 8

    if (rogue["mana"] < spellmpcost):

        print("You dont have enough mana to cast the spell!")

    else:

        print(colored("\n-----------------------------", "yellow"))
        print(rogue["name"] + " attacks every " + colored("enemy", "red") + "!\n")

        for target in characters:

            if(target["loyalty"] == "evil"):
                if (((rogue["damage"] / 2) + d10) - target["armor"] > 0):
                    target["health"] = target["health"] - (int(((rogue["damage"] / 2) + d10)) - target["armor"])
                    print( target["name"] + " took " + colored(str((int(rogue["damage"] / 2)) + d10 - target["armor"]), "red", attrs = ["bold"]) + " damage!")
                    print(target["name"] + " now has " + colored(str(target["health"]), "green", attrs = ["bold"]) + " health!")
                else:
                    print (target["name"] + " took no damage!")
        print(colored("-----------------------------\n", "yellow"))


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

        print(colored("\n-----------------------------", "yellow"))
        target["health"] = target["health"] - (warrior["damage"] + d4)
        print( target["name"] + " took " + colored(str((warrior["damage"] + d4)), "red", attrs = ["bold"]) + " damage!")
        print(target["name"] + " now has " + colored(str(target["health"]), "green", attrs = ["bold"]) + " health!")
        print(colored("-----------------------------\n", "yellow"))
        
           
        
          
#What exorcism spell does
def exorcism():

    d4=random.randrange(1,4)
    spellMpCost = 5

    if (priest["mana"] < spellMpCost):

        print("You dont have enough mana to cast the spell!")

    else:
        target = targetChoice(0)
        if (target == "0"):
            return ("0")

        print(colored("\n-----------------------------", "yellow"))
        target["health"] = target["health"] - (d4 * 2)
        print( target["name"] + " took " + colored(str((d4 * 2)), "red", attrs = ["bold"]) + " damage!")
        print(target["name"] + " now has " + colored(str(target["health"]), "green", attrs = ["bold"]) + " health!")
        print(colored("-----------------------------\n", "yellow"))
    

def mend():

    d6 = random.randrange(1,6)
    spellMpCost = 3

    if (priest["mana"] < spellMpCost):

        print("You dont have enough mana to cast the spell!")
        return("0")

    else:

        
        target = targetChoice(1)

        if (target == "0"):
            return ("0")
        print(colored("\n-----------------------------", "yellow"))
        if (target["health"] + (d6 + priest["damage"]) < target["maxHealth"]):

            target["health"] = target["health"] + (d6 + priest["damage"])
            print("\nPriest healed " + str((target["damage"] + d6)) + " life points to the " + target["name"] + "!\n")
            print( target["name"] + " now has " + str(target["health"]) + colored(" HP", "green"))
        
        else:

            print("\nPriest healed " + str(target["maxHealth"] - target["health"]) + " life points to the " + target["name"] + "!\n")
            target["health"] = target["maxHealth"]
            print( target["name"] + " now has " + str(target["health"]) + colored(" HP", "green"))
            
        print(colored("-----------------------------\n", "yellow"))

    




#Warrior choosing a spell
def spellChooseWarrior():
    spellMpCost = 5
    if (warrior["mana"] < spellMpCost):
        pass

    while(True):

        choice = input("What spell will you choose: \n 1 - RushDown (" + colored(str(warrior["damage"] + 1), "red") + "-" + colored(str(warrior["damage"] + 4), "red") + ") Cost: " + colored("5", "blue") +"\n 0 - Go Back\n\n").translate({ord(c): None for c in string.whitespace}).lower()

        if (choice == "1" or choice == "rushdown"):

            if (rushdown() == "0"):
                continue
            break
        
        elif (choice == "0"):

            return ("0")

        else:

            print("\nYou need to choose a spell\n")
            continue


#Rogue choosing a spell
def spellChooseRogue():

    spellMpCost = 8

    if (goblinShaman["mana"] < spellMpCost):

        print("You dont have enough mana to cast the spell!")


    while(True):

        print("What spell will you choose: ")
        print(" 1 - Arrow Rain ( AOE " + colored(str(int((rogue["damage"] / 2)) + 1), "red") + "-" + colored(str(int((rogue["damage"] / 2)) + 10), "red") + ") Cost: " + colored("8", "blue"))
        print(" 0 - Go Back\n\n")
        choice = input().translate({ord(c): None for c in string.whitespace}).lower()
        if (choice == "1" or choice == "arrowrain"):
            arrowRain()
            break

        elif (choice == "0"):

            return ("0")

        else:
            print("\nYou need to choose a spell\n")
            pass



#Priest choosing a spell
def spellChoosePriest():

    while(True):

        print("What spell will you choose: ")
        print(" 1 - Exorcism (" + colored("2", "red") + "-" + colored("8", "red") + ") Cost: " + colored("5", "blue"))
        print(" 2 - Mend (" + colored(priest["damage"] + 1, "green") + "-" + colored(priest["damage"] + 6, "green") + ") Cost: " + colored("3", "blue"))
        print(" 0 - Go Back\n\n")

        choice = input().translate({ord(c): None for c in string.whitespace}).lower()

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

            print("\nYou need to choose a spell\n")
            pass


def spellChooseGS():
    
    d3 = random.randrange(1,3)

    if (goblinShaman["mana"] > 5):
        if (d3 == 1 or d3 == 2):

            poison()

        elif (d3 == 3):
            if (goblinShaman["mana"] > 7):

                protection()

            else:

                rest()


    else:

        rest()
    

            




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

        if (spellChoosePriest() == "0"):
            return("0")
        return ("1")

    elif (character["name"] == warrior["name"]):

        if (spellChooseWarrior() == "0"):
            return("0")
        return("1")

    elif (character["name"] == rogue["name"]):

        if (spellChooseRogue() == "0"):
            return("0")
        return("1")

    else:
        
        if (character["name"] == goblinShaman["name"]):
            spellChooseGS()
        return("1")


#Function to attack
def attackPhase(character):

    if (character["loyalty"] == "good"):

        target = targetChoice(0)

        if (target == "0"):
            return "0"

        print(colored("\n-----------------------------", "yellow"))
        print(character["name"] + " attacks " + target["name"])


        if ((character["damage"] - target["armor"]) > 0):
            target["health"] = target["health"] - (character["damage"] - target["armor"])
            print( target["name"] + " took " + colored(str(character["damage"] - target["armor"]), "red", attrs = ["bold"]) + " damage!")
            print(target["name"] + " now has " + colored(str(target["health"]), "green", attrs = ["bold"]) + " health!")
        else:
            print (target["name"] + " took no damage!")
        print(colored("-----------------------------\n", "yellow"))
        

    elif (character["loyalty"] == "evil"):

        print("\n" + character["name"] + " is deciding what to do...")
        time.sleep(5)

        while(True):
            target = random.randrange(1, 3)
       

            if (target == 1 and priest["alive"] == 1):

                target = priest
                break

            elif (target == 2 and warrior["alive"] == 1):

                target = warrior
                break   

            elif (target == 3 and rogue["alive"] == 1):

                target = rogue
                break

        print(colored("\n-----------------------------", "red"))
        print("" + character["name"] + " attacks " + target["name"])

        if ((character["damage"] - target["armor"]) > 0):
            target["health"] = target["health"] - (character["damage"] - target["armor"])
            print(target["name"] + " took " + colored(str(character["damage"] - target["armor"]), "red", attrs = ["bold"]) + " damage!")
            print(target["name"] + " now has " + colored(str(target["health"]), "green", attrs = ["bold"]) + " health!")
            
        else:
            print ("" + target["name"] + " took no damage!")
        print(colored("-----------------------------\n", "red"))

def rest(character):
#In rest, the characters have the chance to rest up, loosing the action in the round but regaining mana 

    manaRecover = int(character["maxMana"] * (2/3))

    if (character["mana"] + manaRecover < character["maxMana"]):   


        print(character["name"] + "rested and recovered " + str(manaRecover) + " points! ")

        character["mana"] = character["mana"] + manaRecover

    else: 
        character["mana"] = character["maxMana"]

        print(character["name"] + " healed " + (character["maxMana"]) - (character["mana"]))

#Function to decide what action each character does and check if character is poisoned
def chooseAction(character):

    #If the character is poisoned and alive, he takes 5 damage
    if (character["poisoned"] > 0 and character["health"] > 0):

        character["poisoned"] = character["poisoned"] - 1
        print(colored("\n-----------------------------\n", "green") + character["name"] + " is poisoned he takes " + colored(poisonDamage, "green", attrs=["bold"]) + " damage!")
        character["health"] = character["health"] - poisonDamage
        print("Health is now " + str(character["health"]) + colored("\nPoisoned", "green", attrs=["bold"]) + " turns left: " + str(character["poisoned"]) + colored("\n-------------------------------\n", "green"))
        
    
    #If character is alive he acts
    while(True and character["alive"] == 1):
            
        #If its an ally character (loyalty = good) he chooses what to do 
        if (character["loyalty"] == "good"):

            print("--------------------------")
            print("You are: " + character["name"])
            choice = input("Would you like to: \n 1 - Attack \n 2 - Use a spell \n 3 - Rest (Recover "+ colored("mana", "blue") +")\n\n").translate({ord(c): None for c in string.whitespace}).lower()

        #If its an enemy character (loyalty = evil) his actions are randomly chosen
        else:

            #If the enemy is a goblinShaman he has a chance of using spells, since he's the only spell caster on the enemy side
            if (character["name"] != goblinShaman["name"]):
                
                d4 = random.randrange(1, 5)
                
                #20% chance of the Goblin Shaman attacking 
                if (d4 == 1):

                    choice == "1"

                #80% chance of the Goblin Shaman casting a spell
                else:

                    #If Goblin Shaman doesnt have enough mana to cast a spell he rests to recover mana
                    if (goblinShaman["mana"] < 6):

                        rest()

                    #If Goblin Shaman has enough mana he will cast a random spell
                    else:

                        choice == "2"

            #If it's an enemy other than the Goblin Shaman he always attacks
            else:

                choice == "1"
                

        #If character is attacking he goes into Attack Phase
        if (choice == "1"):

            if (attackPhase(character) != "0"):
                break
            

        #If character is casting a spell he goes into Spell Phase
        elif (choice == "2"):

            if (spellPhase(character) != "0"):
                break
    


#Function for every action in the action phase
def actionPhase(characters):

    #Go through the character list which is ordered by iniative so each character can do through their action phase
    for character in characters:

        #In case one of the parties dies mid combat loop, this breaks the loop and exits to whoWon to display 
        if (ogre["health"] + goblin["health"] + goblinShaman["health"] <= 0):

            break
        elif (warrior["health"] + priest["health"] + rogue["health"] <= 0):

            break

        #Display the turn order everytime someone's turn starts
        whoGoesFirst(characters)

        #Check if any character died inbetween character turns, to make sure a dead character cannot act, and changes his alive value to 0
        for x in characters:

            if (x["health"] <= 0 and x["alive"] == 1):

                print(colored("\n--------------------------", "red",  attrs=["bold"]))
                print("     " + x["name"] + " is downed!")
                print(colored("--------------------------\n", "red",  attrs=["bold"]))
                x["alive"] = 0
                x["health"] = 0
                x["name"] = colored(x["name"], attrs= ["reverse"])

        
        """ for x in charactersUnsorted:
            if x["name"] == character["name"]:
                x["name"] = character["name"] """
        
        #Check if the character is alive, and if he is he takes his turn
        if (character["alive"] == 1):

            chooseAction(character)

            #Give time for the player to see what happened in that turn
            time.sleep(8)

        clear()


#Function to print on screen if you won or lost
def whoWon():

    #Prints YOU LOST if ally party has 0 combined health
    if (warrior["health"] + priest["health"] + rogue["health"]  <= 0):
        
        print(colored (" __     __ ____   _    _    _       ____    _____  _______ ", "red"))
        print(colored (" \ \   / // __ \ | |  | |  | |     / __ \  / ____||__   __|", "red"))
        print(colored ("  \ \_/ /| |  | || |  | |  | |    | |  | || (___     | |   ", "red"))
        print(colored ("   \   / | |  | || |  | |  | |    | |  | | \___ \    | |   ", "red"))
        print(colored ("    | |  | |__| || |__| |  | |____| |__| | ____) |   | |   ", "red"))
        print(colored ("    |_|   \____/  \____/   |______|\____/ |_____/    |_|   ", "red"))
        print("\n")

    #Prints YOU WIN if enemy party has 0 combined health                                                         
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


#Function to clear then terminal depending on what os we are on
def clear():

    #windows clear
    if (os.name == "nt"):

        os.system("cls")

    #linux or mac clear
    else:

        os.system("clear")

#Initializing Variables

#Defining the poison damage per turn each character takes
poisonDamage = 5

#Creating each character
rogue = createCharacter(colored("Rogue", "white", attrs=["bold"]), 22, 10, 0, 6, 10, "good", 0, 1)   
priest = createCharacter(colored("Priest", "white", attrs=["bold"]), 20, 25, 0, 2, 6, "good", 0, 1)  
warrior = createCharacter(colored("Warrior", "white", attrs=["bold"]), 32, 5, 2, 5, 2, "good", 0, 1)  
goblinShaman = createCharacter(colored("Goblin Shaman", "red", attrs=["bold"]), 20, 20, 0, 5, 5, "evil", 0, 1)   
goblin = createCharacter(colored("Goblin", "red", attrs=["bold"]), 10, 0, 0, 5, 7, "evil", 0, 1)
ogre = createCharacter(colored("Ogre", "red", attrs=["bold"]), 20, 0, 2, 3, 0, "evil", 0, 1)

#Creating an unsorted list for the fuction printChoices to always display the same options since the list characters will constantly be sorted
charactersUnsorted = [rogue, priest, warrior, goblin, ogre, goblinShaman]

#Creating a list with every character that will constantly be sorted by initiative order
characters = [rogue, priest, warrior, goblinShaman, goblin, ogre]


#Main combat loop 
while(warrior["health"] + priest["health"] + rogue["health"]  > 0 and ogre["health"] + goblin["health"] + goblinShaman["health"] > 0 ):

    clear()
    
    #Create a list with each character rolling its iniative
    order = turnOrder(characters)

    #Order the initiave list and the character list at the same time, so the characters are ordered by iniative
    order, characters = sortOrder(order, characters)

    #Give 2 seconds for the player to see each character's roll
    time.sleep(2)

    clear()

    #Iniate each character's action phase
    actionPhase(characters)

#Display YOU WIN or YOU LOSE depending on what party has a combined total of 0 health
whoWon()