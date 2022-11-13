import random
import string
from termcolor import colored, cprint  #run on console: pip install termcolor
import time
import os

#Deletes the user's input from displaying in the terminal
def deleteInput():

    print ("\033[A                             \033[A")


#Function to create a character as a dictionary
def createCharacter(name, health, mana, armor, damage, initiative, loyalty, poisoned, damageBoost, alive):

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
        "damageBoost" : damageBoost,
        "alive" : alive
    }

    return (character)


#Function to roll iniative of each character
def rollInitiative(character):

    #Rolls a 20 sided dice
    d20 = random.randrange(1, 21)

    #If the character is alive it prints the character's iniciate, else it skips that character
    if (character["alive"] == 1):
        print("\n" + character["name"] + " rolled a " + str(d20) + " his iniative is: " + colored(str(d20 + character["initiative"]), "yellow")) 
        time.sleep(1.5)
    
    #Returns the character's iniciative
    return (d20 + character["initiative"])


#Function that creates a list with the iniative roll of each character
def turnOrder(characters):

    #Initialize the list to append each initiave roll
    order = []

    #Go through every character in the character list and append his iniative
    for character in characters:

        order.append(rollInitiative(character))
    
    #Return a list with all the initiave rolls
    return(order)


#Function to sort the character list by iniative order
def sortOrder(order, characters):

    #Goes through the index from 0 to the length of the order list so it sorts "length amount of times"
    for i in range(len(order)):
        
        #Goes through the index from 0 to length - 1 of the order list
        for x in range(len(order) - 1):
            
            #If the number in the index is smaller then the next number (index + 1), they get swapped out
            if (order[x] < order[x + 1]):

                #Swap order if iniative in next index is higher
                #Saves old value on an auxiliar variable
                auxTurn = order[x]

                #The index becomes the next index's number
                order[x] = order[x + 1]

                #The next index becomes the saved number
                order[x + 1] = auxTurn  

                #If iniative in next index is smaller also swap character order in the characters array
                #Saves old character on an auxiliar variable
                auxCharacter = characters[x]

                #The index becomes the next index's number
                characters[x] = characters[x + 1]

                #The next index becomes the saved number
                characters[x + 1] = auxCharacter
            
            #If the characters have the same initiative roll, there's a check to see whose 
            #iniative his higher and put that character first
            elif (order[x] == order[x + 1]):

                #Check whose iniative is higher
                if (characters[x]["initiative"] < characters[x + 1]["initiative"]):
                    auxTurn = order[x]
                    order[x] = order[x + 1]
                    order[x + 1] = auxTurn  

                    auxCharacter = characters[x]
                    characters[x] = characters[x + 1]
                    characters[x + 1] = auxCharacter

    #Return the sorted list and the sorted character list
    return(order, characters)
    
#Function to print every choice depending on if its allies or enemies
def printChoices(loyalty):

    #Initial counter to print in order
    choiceIndex = 0

    #Display the options for every character in an unsorted list so the options 
    #are consistent with the target choice function
    print("Who do you want to target? ")
    for x in charactersUnsorted:
        if (x["loyalty"] == loyalty):
            
            choiceIndex += 1

            extra = 0

            print(str(choiceIndex) + " - " + x["name"], end = "")

            if (x["alive"]  == 0):
                extra = 8

            for _ in range(0, ((28 + extra) - len(x["name"]))):

                print(" ", end="")
            
            print("[ " + colored("HP: " , "green"), end="")
            if (x["health"] < 10):
                print("0", end="")
            print(str(x["health"]) + "/" + str(x["maxHealth"]), end = " |")

            print(colored(" Mana: ", "blue"), end="")
            if (x["mana"] < 10):
                print("0", end="")
            print(str(x["mana"]) + "/", end= "")

            if (x["maxMana"] < 10):
                print("0", end="")
            print(str(x["maxMana"]), end = " |")

            print(colored(" Armor: ", "grey") + str(x["armor"]), end = " |")
            print(colored(" Damage: ", "red") + str(x["damage"]), end = " |")
            print(colored(" Poisoned: ", "green" , attrs= ["bold"]) + str(x["poisoned"]), end = " |")
            if (x["damageBoost"] > 0):
                print(colored(" 2x Damage", "red", attrs= ["bold"] ) +  " ]")
            else:
                print(colored(" 2x Damage", "grey", attrs= ["bold"] ) +  " ]")

    print("\n 0 - Go Back")


#Function to choose who to target with spells
def targetChoice(friendship):

    #If its an ally attacking he gets enemy choices
    if (friendship == 0):

        attackDecision = ""

        #Loop so the player can only choose one of the options displayed or else it keeps asking again
        while(not attackDecision in (goblin, ogre, goblinShaman, "0")):

            #Prints all the possible choices for enemies
            printChoices("evil")

            #Receives the player choice
            attackDecision = input("\n").translate({ord(c): None for c in string.whitespace}).lower()
            deleteInput()
            
            #If he chooses 1  and the goblin is alive he gets the goblin as the target
            if ((attackDecision == "1" and goblin["alive"] == 1) or (attackDecision == "goblin" and goblin["alive"] == 1)):

                attackDecision = goblin
            
            #If he chooses 2 and the ogre is alive he gets the ogre as the target
            elif ((attackDecision == "2" and ogre["alive"] == 1) or (attackDecision == "ogre" and ogre["alive"] == 1)):

                attackDecision = ogre
            
            #If he chooses 3 and the goblin shaman is alive he gets the goblin shaman as the target
            elif ((attackDecision == "3" and goblinShaman["alive"] == 1) or (attackDecision == "goblinshaman" and goblinShaman["alive"] == 1)):

                attackDecision = goblinShaman
            
            #If he chooses 0 the function returns 0
            elif (attackDecision == "0"):

                attackDecision = "0"

            #If he doesnt choose a valid option he gets the options back to choose from
            else:
                clear()
                print("\n----------------------------------------")
                print("You need to choose a valid " + colored("Enemy", "red", attrs=["bold"]) + " to attack")
                print("----------------------------------------\n")


    #If its an ally trying to target an ally he gets ally choices
    elif(friendship == 1):

        attackDecision = ""

        #Loop so the player can only choose one of the options displayed or else it keeps asking again
        while (not attackDecision in (rogue, warrior, priest, "0")):

            #Prints all the possible choices for allies
            printChoices("good")

            #Gets the player's decision
            attackDecision = input("\n" ).translate({ord(c): None for c in string.whitespace}).lower()
            deleteInput()

            #If he chooses 1 and the rogue is alive he gets the rogue as the target
            if ((attackDecision == "1" and rogue["alive"] == 1) or (attackDecision == "rogue" and rogue["alive"] == 1)):

                attackDecision = rogue

            #If he chooses 2 and the priest is alive he gets the priest as the target
            elif ((attackDecision == "2" and priest["alive"] == 1) or (attackDecision == "priest" and priest["alive"] == 1)):

                attackDecision = priest

            #If he chooses 3 and the warrior is alive he gets the warrior as the target
            elif ((attackDecision == "3" and warrior["alive"] == 1) or (attackDecision == "warrior" and warrior["alive"] == 1)):

                attackDecision = warrior

            #If he chooses 0 the function returns 0
            elif (attackDecision == "0"):

                attackDecision = "0"

            #If he doesnt choose a valid option he gets the options back to choose from
            else:
                clear()
                print("-----------------------------")
                print("You need to choose a valid " + colored("Ally", "white", attrs=["bold"]) + "!")
                print("-----------------------------\n")
            
    #Returns the target for the action
    return (attackDecision)


#Use the goblin shamans's spell damage buff
def damageBuff():
    	
    #Roll a 7 sided dice
    d7 = random.randrange(1,8)

    print(colored("\n-----------------------------", "red"))

    #If the goblin shaman rolls a 1 (14% chance) he fails to cast the spell
    if (d7 == 1):

        print(goblinShaman["name"] + " tries to buff the" + colored(" enemies", "red") + " but fails!")

    #If he rolls anything other than the 1 (86% chance) he casts damage buff
    else:
        
        print(goblinShaman["name"] + " buffs the" + colored(" enemies ", "red") + "damage! ( " + colored("x2", "red") +" damage for the next turn )\n")
        for x in characters:
            if (x["loyalty"] == "evil"):
                x["damageBoost"] += 1

    print(colored("-----------------------------\n", "red"))





#Use the rogue's spell arrow rain
def arrowRain():

    #Roll a 10 sided dice
    d5 = random.randrange(1,6)

    #Arrow Rains's mana cost
    spellMpCost = 8

    #Reduces rogue's mana by the spell cost
    rogue["mana"] = rogue["mana"] - spellMpCost

    #Display the damage dealt by the rogue to the targets
    print(colored("\n-----------------------------\n", "white"))
    print(rogue["name"] + " attacks every " + colored("enemy", "red") + "!\n")

    for target in characters:

        if(target["loyalty"] == "evil" and target["alive"] == 1):
            if (((rogue["damage"] / 2) + d5) - target["armor"] > 0):
                target["health"] = target["health"] - (int(((rogue["damage"] / 2) + d5)) - target["armor"])
                print( target["name"] + " took " + colored(str((int(rogue["damage"] / 2)) + d5 - target["armor"]), "red", attrs = ["bold"]) + " damage!")
                print(target["name"] + " now has " + colored(str(target["health"]), "green", attrs = ["bold"]) + " health!\n")
            else:
                print (target["name"] + " took no damage!")

    print(colored("-----------------------------\n", "white"))

#Use the goblin shaman's spell poison
def poison():

    target = 0

    #Cycle happens until goblin shaman picks an ally that's alive
    while(not target in (priest, warrior, rogue)):
        
        target = random.randrange(1, 4)
    
        if (target == 1 and priest["alive"] == 1):

            target = priest 

        elif (target == 2 and warrior["alive"] == 1):

            target = warrior 

        elif (target == 3 and rogue["alive"] == 1):

            target = rogue

    #Roll a 4 sided dice to choose how many turns the target is poisoned for + 1
    d4 = random.randrange(2, 6)

    #Add the amount of turns rolled on the dice to the amount of turns the target is poisoned for
    target["poisoned"] += d4

    #Display how much poisoned was applied and to who
    print(colored("\n-----------------------------", "red"))
    print(goblinShaman["name"] + " applied the spell poison to " + target["name"] + " !")
    print (target["name"] + " is poisoned for " + str(d4) + " more rounds!")
    print(colored("-----------------------------\n", "red"))


#Use the warrior's spell exorcism
def rushDown():
    
    #Roll a 4 sided dice
    d4=random.randrange(1, 5)

    #Rushdown's mana cost
    spellMpCost = 5

    #If the warrior doesnt have enough mana to use rushdown he goes back to choosing spells
    if (warrior["mana"] < spellMpCost):

        print("You dont have enough mana to cast that spell!")
        return("0")

    #Else he casts rushdown
    else:
        
        #Choose who to target with rushdown
        target = targetChoice(0)

        #If he chooses 0 he goes back to choosing the spells
        if (target == "0"):
            return ("0")

        #Reduces warrior's mana by the spell cost
        warrior["mana"] = warrior["mana"] - spellMpCost
        
        #Display the damage dealt by the warrior to the target
        print(colored("\n-----------------------------", "white"))
        target["health"] = target["health"] - (warrior["damage"] + d4)
        print( target["name"] + " took " + colored(str((warrior["damage"] + d4)), "red", attrs = ["bold"]) + " damage!")
        print(target["name"] + " now has " + colored(str(target["health"]), "green", attrs = ["bold"]) + " health!")
        print(colored("-----------------------------\n", "white"))
        
           
        
          
#Use the priest's spell exorcism
def exorcism():

    #Roll a 4 sided dice
    d4=random.randrange(1, 5)

    #Excorcism's mana cost
    spellMpCost = 5

    #If the priest doesnt have enough mana to use mend he goes back to choosing spells
    if (priest["mana"] < spellMpCost):

        print("You dont have enough mana to cast that spell!")
        return("0")

    #Else he casts exorcism
    else:

        #Choose who to target with exorcism
        target = targetChoice(0)

        #If he chooses 0 he goes back to choosing the spells
        if (target == "0"):
            return ("0")

        #Reduces priest's mana by the spell cost
        priest["mana"] = priest["mana"] - spellMpCost

        #Display the damage dealt by the priest to the target
        print(colored("\n-----------------------------", "white"))
        target["health"] = target["health"] - (d4 * 2)
        print( target["name"] + " took " + colored(str((d4 * 2)), "red", attrs = ["bold"]) + " damage!")
        print(target["name"] + " now has " + colored(str(target["health"]), "green", attrs = ["bold"]) + " health!")
        print(colored("-----------------------------\n", "white"))
    

#Use the priest's spell mend
def mend():

    #Roll a 6 sided dice
    d6 = random.randrange(1, 7)

    #Mend's mana cost
    spellMpCost = 3

    #If the priest doesnt have enough mana to use mend he goes back to choosing spells
    if (priest["mana"] < spellMpCost):

        print("You dont have enough mana to cast that spell!")
        return("0")

    #Else he casts mend
    else:

        #Choose who to heal
        target = targetChoice(1)

        #If he chooses 0 he goes back to choosing the spells
        if (target == "0"):
            return ("0")

        #Displays the amount of healing on the screen
        print(colored("\n-----------------------------", "white"))

        #Reduces priest's mana by the spell cost
        priest["mana"] = priest["mana"] - spellMpCost

        #If after casting mend the amount of health he recovers doesnt break the max health threshold of the characters, 
        #he recovers that amount
        if (target["health"] + (d6 + priest["damage"]) < target["maxHealth"]):

            target["health"] = target["health"] + (d6 + priest["damage"])
            print("Priest healed " + str((priest["damage"] + d6)) + " life points to the " + target["name"] + "!")
            print( target["name"] + " now has " + str(target["health"]) + colored(" HP", "green"))


        #If after casting mend the amount of health he recovers breaks the max health threshold of the character, 
        #the character's health becomes his max health
        else:

            print("Priest healed " + str(target["maxHealth"] - target["health"]) + " life points to the " + target["name"] + "!")
            target["health"] = target["maxHealth"]
            print( target["name"] + " now has " + str(target["health"]) + colored(" HP", "green"))
            
        print(colored("-----------------------------\n", "white"))

    




#Warrior choosing a spell
def spellChooseWarrior():

    choice = ""
    
    #Loop so the player can only choose one of the 2 options displayed
    while(choice != "done"):

        #Display possible options
        print("Choose a spell, you have " + colored(str(warrior["mana"]), "blue") + " mana: ")
        print(" 1 - RushDown (" + colored(str(warrior["damage"] + 1), "red") + "-" + colored(str(warrior["damage"] + 4), "red") + ") Cost: " + colored("5", "blue") 
        +"\n\n0 - Go Back\n")
        
        #Get the player's input
        choice = input().translate({ord(c): None for c in string.whitespace}).lower()
        deleteInput()

        #Go to function rushDown if he chooses 1
        if (choice == "1" or choice == "rushdown"):

            if (rushDown() == "0"):
                clear()
            else:
                choice = "done"
        
        #Go back if he chooses 0
        elif (choice == "0"):

            choice = "done"
            return ("0")

        #Print this if its an invalid choice
        else:

            clear()
            print("\nYou need to choose a spell\n")


#Rogue choosing a spell
def spellChooseRogue():

    choice = ""

    #Loop so the player can only choose one of the 2 options displayed
    while(choice != "done"):

        #Display possible options
        print("Choose a spell, you have " + colored(str(rogue["mana"]), "blue") + " mana: ")
        print(" 1 - Arrow Rain (AOE " + colored(str(int((rogue["damage"] / 2)) + 1), "red") + "-" + colored(str(int((rogue["damage"] / 2)) + 5), "red") + ") Cost: " + colored("8", "blue"))
        print("\n 0 - Go Back\n\n")

        #Get the player's input
        choice = input().translate({ord(c): None for c in string.whitespace}).lower()
        deleteInput()

        #Go to function arrowRain if he chooses 1
        if (choice == "1" or choice == "arrowrain"):

            #If the rogue doesnt have enough mana to use arrow rain he goes back to choosing spells
            if (rogue["mana"] < 8):

                print("You dont have enough mana to cast that spell!")
            else:

                arrowRain()
                choice = "done"
        
        #Go back if he chooses 0
        elif (choice == "0"):

            choice = "done"
            return ("0")

        #Print this if its an invalid choice
        else:
            clear()
            print("\nYou need to choose a spell\n")



#Priest choosing a spell
def spellChoosePriest():

    choice = ""

    #Loop so the player can only choose one of the 3 options displayed
    while(choice != "done"):
        
        #Display possible options
        print("Choose a spell, you have " + colored(str(priest["mana"]), "blue") + " mana: ")
        print(" 1 - Exorcism (" + colored("2", "red") + "-" + colored("8", "red") + ") Cost: " + colored("5", "blue"))
        print(" 2 - Mend (" + colored(priest["damage"] + 1, "green") + "-" + colored(priest["damage"] + 6, "green") + ") Cost: " + colored("3", "blue"))
        print("\n 0 - Go Back\n\n")

        #Get the player's input
        choice = input().translate({ord(c): None for c in string.whitespace}).lower()
        deleteInput()

        #Go to function exorcism if he chooses 1
        if (choice == "1" or choice == "exorcism"):

            if (exorcism() == "0"):
                clear()
            else:
                choice = "done"

        #Go to function mend if he chooses 2
        elif (choice == "2" or choice == "mend"):

            if (mend() == "0"):
                clear()
            else:
                choice = "done"
        
        #Go back if he chooses 0
        elif (choice == "0"):

            choice = "done"
            return ("0")

        #Print this if its an invalid choice
        else:
            clear()
            print("\nYou need to choose a spell\n")


#Spell choosing for the goblin shaman
def spellChooseGS():
    
    #If he gets a 1 or 2 (66% chance) he chooses poison, if he gets a 3  (33% chance) he choose the damage buff spell
    d3 = random.randrange(1, 4)
    #If he has enough mana he casts the spell, else he rests
    if (goblinShaman["mana"] > 5):
        if (d3 == 1):

            poison()

        elif (d3 == 3 or d3 == 2):
            if (goblinShaman["mana"] > 7):

                damageBuff()

            else:

                rest()


    else:

        rest()
    

            




#Function that shows character's attack order on the terminal
def whoGoesFirst(characters):
    
    print("Turn order:\n")

    i = 0
    
    for x in characters:

        #Only displays alive characters on terminal
        if (x["alive"] == 1):
            
            i += 1

            print(str(i) + " - " + x["name"], end = "")

            for _ in range(0, (28 - len(x["name"]))):

                print(" ", end="")

            print("[ " + colored("HP: " , "green"), end="")
            if (x["health"] < 10):
                print("0", end="")
            print(str(x["health"]) + "/" + str(x["maxHealth"]), end = " |")
            print(colored(" Mana: ", "blue"), end="")
            if (x["mana"] < 10):
                print("0", end="")
            print(str(x["mana"]) + "/", end= "")
            if (x["maxMana"] < 10):
                print("0", end="")
            print(str(x["maxMana"]), end = " |")
            print(colored(" Armor: ", "grey") + str(x["armor"]), end = " |")
            print(colored(" Damage: ", "red") + str(x["damage"]), end = " |")
            print(colored(" Poisoned: ", "green" , attrs= ["bold"]) + str(x["poisoned"]), end = " |")
            if (x["damageBoost"] > 0):
                print(colored(" 2x Damage", "red", attrs= ["bold"] ) +  " ]")
            else:
                print(colored(" 2x Damage", "grey", attrs= ["bold"] ) +  " ]")



#Function to know who is using each spell
def spellPhase(character):

    #Each character has a differente spell phase
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


#Function for characters to attack
def attackPhase(character):

    #If the character is an ally he attacks here
    if (character["loyalty"] == "good"):

        target = targetChoice(0)

        if (target == "0"):
            return ("0")


        #Dealing the damage and displaying it on screen
        print(colored("\n-----------------------------", "white"))
        print(character["name"] + " attacks " + target["name"])
        
        #If the character has damage boost deals double damage
        if (character["damageBoost"] == 0):

            damage = (character["damage"] - target["armor"])

        else:

            damage = ((character["damage"] * 2) - target["armor"])

        #If the armor didnt nullify the damage deal damage, else deal no damage and display "target took no damage"
        if (damage > 0):

            target["health"] = target["health"] - damage
            print( target["name"] + " took " + colored(str(damage), "red", attrs = ["bold"]) + " damage!")
            print(target["name"] + " now has " + colored(str(target["health"]), "green", attrs = ["bold"]) + " health!")
        else:

            print (target["name"] + " took no damage!")

        print(colored("-----------------------------\n", "white"))
        
    #If the characters is an enemy he attacks here
    elif (character["loyalty"] == "evil"):

        print("\n" + character["name"] + " is deciding what to do...")
        time.sleep(5)

        target = 0

        #Choose a random character from the ally team to attack
        while(not target in [priest, warrior, rogue]):
            target = random.randrange(1, 4)
       
            if (target == 1 and priest["alive"] == 1):

                target = priest

            elif (target == 2 and warrior["alive"] == 1):

                target = warrior

            elif (target == 3 and rogue["alive"] == 1):

                target = rogue
        
        #Display who is attacking who
        print(colored("\n-----------------------------", "red"))
        print("" + character["name"] + " attacks " + target["name"])

        #If its any other enemy than damage * 1
        d2 = 2

        #If the enemy is a goblin he has 50% chance to deal double damage
        if (character["name"] == goblin["name"]):
#tempo goblin shaman
            #Damage * d2
            d2 = random.randrange(2, 5)
            
        #Doubles the character's damage if he has damage boost
        if (character["damageBoost"] == 0):
            
            damage = int(((character["damage"] * int(d2 /2)) - target["armor"]))
        else:

            character["damageBoost"] = 0
            damage = int(((character["damage"] * 2 * int(d2 /2)) - target["armor"]))

        #If the armor didnt nullify the damage deal damage, else deal no damage and display "target took no damage"
        if (damage > 0):
            target["health"] = target["health"] - damage
            print( target["name"] + " took " + colored(str(damage), "red", attrs = ["bold"]) + " damage!")
            print(target["name"] + " now has " + colored(str(target["health"]), "green", attrs = ["bold"]) + " health!")
        else:
            print (target["name"] + " took no damage!")
        print(colored("-----------------------------\n", "red"))




#The character rests and recovers 2/3 of its max mana, unless its the warrior
#which always recovers full mana since he has a low amount of mana
def rest(character):

    manaRecover = int(character["maxMana"] * (2/3))

    #If its the warrior recover full mana
    if(character["name"] == warrior["name"]):
        character["mana"] = character["maxMana"]
        print(colored("\n-----------------------------", "blue"))
        print(character["name"] + " restored " + colored(str((character["maxMana"]) - (character["mana"])), "blue") + " mana!")
        print(colored("-----------------------------\n", "blue"))
    
    else:
        #If after resting the amount of mana he recovers doesnt break the max mana threshold he recovers that amount
        if (character["mana"] + manaRecover < character["maxMana"]):   

            character["mana"] = character["mana"] + manaRecover
            print(colored("\n-----------------------------", "blue"))
            print(character["name"] + " rested and recovered " + str(manaRecover) + " mana! ")
            print(colored("-----------------------------\n", "blue"))


        #If after resting the amount of mana he recovers breaks the max mana threshold his mana becomes his max mana
        else:

            character["mana"] = character["maxMana"]
            print(colored("\n-----------------------------", "blue"))
            print(character["name"] + " restored " + colored(str((character["maxMana"]) - (character["mana"])), "blue") + " mana!")
            print(colored("-----------------------------\n", "blue"))



#Function to decide what action each character does and check if character is poisoned
def chooseAction(character):


    choiceNotChosen = True

    #If the character is poisoned and alive, he takes poison damage and reduces poison turns by 1
    if (character["poisoned"] > 0 and character["health"] > 0):

        character["poisoned"] = character["poisoned"] - 1
        print(colored("\n-----------------------------\n", "green") + character["name"] + " is poisoned he takes " + colored(poisonDamage, "green", attrs=["bold"]) + " damage!")
        character["health"] = character["health"] - poisonDamage
        print("Health is now " + str(character["health"]) + colored("\nPoisoned", "green", attrs=["bold"]) + " turns left: " + str(character["poisoned"]) + colored("\n-------------------------------\n", "green"))
        if(character["health"] <= 0):
            character["alive"] = 0

    #If character is alive he acts
    while(choiceNotChosen and character["alive"] == 1):
            
        #If its an ally character (loyalty = good) he chooses what to do 
        if (character["loyalty"] == "good"):

            print("\n\nYou are: " + character["name"])
            choice = input("Would you like to: \n 1 - Attack \n 2 - Use a spell \n 3 - Rest ( Recover "+ colored("Mana", "blue") +" )\n\n").translate({ord(c): None for c in string.whitespace}).lower()
            deleteInput()

        #If its an enemy character (loyalty = evil) his actions are randomly chosen
        else:

            #If the enemy is a goblinShaman he has a chance of using spells, since he's the only spell caster on the enemy side
            if (character["name"] == goblinShaman["name"]):
                
                d4 = random.randrange(1, 8)
                
                #15% chance of the Goblin Shaman attacking 
                if (d4 == 1):

                    choice = "1"

                #85% chance of the Goblin Shaman casting a spell
                else:

                    #If Goblin Shaman doesnt have enough mana to cast a spell he rests to recover mana
                    if (goblinShaman["mana"] < 6):

                        rest()

                    #If Goblin Shaman has enough mana he will cast a random spell
                    else:

                        choice = "2"

            #If it's an enemy other than the Goblin Shaman he always attacks
            else:

                choice = "1"
                

        #If character is attacking he goes into Attack Phase
        if (choice == "1"):

            if (attackPhase(character) != "0"):
                choiceNotChosen = False
            

        #If character is casting a spell he goes into Spell Phase
        elif (choice == "2"):

            if (spellPhase(character) != "0"):
                choiceNotChosen = False

        elif (choice == "3"):

            rest(character)
            choiceNotChosen = False

    


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

  
        
        #Check if the character is alive, and if he is he takes his turn
        if (character["alive"] == 1):

            chooseAction(character)

            #Check if any character died inbetween character turns, to make sure a dead character cannot act, and changes his alive value to 0
            for x in characters:

                if (x["health"] <= 0 and x["alive"] == 1):

                    print(colored("\n--------------------------", "red",  attrs=["bold"]))
                    print("     " + x["name"] + " is downed!")
                    print(colored("--------------------------\n", "red",  attrs=["bold"]))
                    x["alive"] = 0
                    x["health"] = 0
                    x["name"] = colored(x["name"], attrs= ["reverse"])

            #Give time for the player to see what happened in that turn
            time.sleep(6)

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
rogue = createCharacter(colored("Rogue", "white", attrs=["bold"]), 22, 10, 0, 6, 10, "good", 0, 0, 1)   
priest = createCharacter(colored("Priest", "white", attrs=["bold"]), 20, 25, 0, 2, 6, "good", 0, 0, 1)  
warrior = createCharacter(colored("Warrior", "white", attrs=["bold"]), 32, 5, 2, 5, 2, "good", 0, 0, 1)  
goblinShaman = createCharacter(colored("Goblin Shaman", "red", attrs=["bold"]), 20, 22, 0, 2, 12, "evil", 0, 0, 1)   
goblin = createCharacter(colored("Goblin", "red", attrs=["bold"]), 15, 0, 0, 8, 7, "evil", 0, 0, 1)
ogre = createCharacter(colored("Ogre", "red", attrs=["bold"]), 20, 0, 2, 5, 0, "evil", 0, 0, 1)

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