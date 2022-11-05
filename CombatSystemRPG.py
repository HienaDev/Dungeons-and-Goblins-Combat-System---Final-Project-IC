import random
import string


#Function to create a character
def createCharacter(name, health, mana, armor, damage, iniative):

    character = {
        "name" : name,
        "health" : health,
        "mana" : mana,
        "armor" : armor,
        "damage" : damage,
        "iniative" : iniative
    }

    return (character)


#Function to create an array of characters
def allCharacters(characters):

    return (characters)


#Function to roll iniative of each character
def rollInitiative(character):

    d20 = random.randrange(1, 20)
    print(character["name"] + " rolled a " + str(d20) + " his turn order is: " + str(d20 + character["iniative"]))
    return (d20 + character["iniative"])


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
    

#What rushdown spell does
def rushdown(characters):
    d4=random.randrange(1,4)
    spellmpcost = 5
    if (warrior["mana"] >= spellmpcost):
        pass
        
#What exorcism spell does
def exorcism():
    pass

def mend():
    pass
    

#Warrior choosing a spell
def spellchooseW(characters):
    print(" What spell will you choose: \n 1-RushDown \n 0-Back ")
    if input(1):
        rushdown()
    elif input(0):
        pass


#Priest choosing a spell
def spellChooseP(character):

    print("--------------------------")
    print("What spell will you choose: \n1 - Exorcism \n2 - Mend \n0 - Back ")
    if (input == "1"):
        exorcism()
    elif input("2"):
        mend()
    elif input(0):
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

    while(True):

        print("----------------------------------")
        print("You are: " + character["name"])
        choice = input("Would you like to: \n1 - Attack \n2 - Use a spell?\n").translate({ord(c): None for c in string.whitespace})

        if (choice == "1"):

            attackPhase(character)
            break

        elif (choice == "2"):

            spellPhase(character)
            break

        else:

            continue


#Function for every action in the action phase
def actionPhase(characters):

    for character in characters:

        chooseAction(character)

player = createCharacter("Player", 25, 10, 2, 5, 10)   
monster = createCharacter("Monster", 30, 20, 23, 5, 6)   
priest = createCharacter("Priest", 20, 25, 0, 2, 6)  
warrior = createCharacter("Warrior", 32, 5, 2, 5, 2)  
spider = createCharacter("Spider", 17, 5, 23, 5, 9) 

characters = allCharacters([player, monster, priest, warrior, spider])
for x in characters:
    print(str(x))
order = turnOrder(characters)
print(str(order))
order, characters = sortOrder(order, characters)
print(str(order))
print("----------------------------------------")
whoGoesFirst(characters)
actionPhase(characters)

#se escolher o spell e possior mp sufecientes
#spellefectvalue = -1 * (wd + d4)
#if input('rushdown') and (mpplayer >= SpellMPcost):
#   (player[2]) - 