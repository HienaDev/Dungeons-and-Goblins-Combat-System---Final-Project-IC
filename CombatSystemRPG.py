import random


#Function to create a character
def createCharacter(name, health, mana, armor, damage, iniative):

    character = (name, health, mana, armor, damage, iniative)
    return (character)


#Function to create an array of characters
def allCharacters(characters):

    return (characters)


#Function to roll iniative of each character
def rollInitiative(character):

    d20 = random.randrange(1, 20)
    print(character[0] + " rolled a " + str(d20) + " his turn order is: " + str(d20 + character[5]))
    return (d20 + character[5])


#Function that creates a tuple with the iniative roll of each character
def turnOrder(characters):

    order = []

    for character in characters:

        order.append(rollInitiative(character))
    
    return(order)


#Function to sort the character list by iniative order
def sortOrder(order, characters):

    auxTurn = 0
    auxCharacter = "Hello"

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
    

#What exorcism spell does
def rushdown(characters):
    d4=random.randrange(1,4)
    spellmpcost = 5
    if (warrior[2] >= spellmpcost):
        SpellEffectValue = -1 * (WP + d4)
        

def exorcism():
    pass

def mend():
    pass
    

#Warrior choosing the spell
def spellchooseW(characters):
    print(" What spell will you choose: \n 1-RushDown \n 0-Back ")
    if input(1):
        rushdown()
    elif input(0):
        pass


#Wizzard choosing the spells
def spellchooseP(characters):
    print(" What spell will you choose: \n 1-Exorcism \n 2-Mend \n 0-Back ")
    if input(1):
        exorcism()
    elif input(2):
        mend()
    elif input(0):
        pass



    
#def magicspells():
#    spells = ['rushdown', 'exorcism', 'mend']
#    if input ('rushdown')

def whoGoesFirst(characters):
    
    print("Turn order:\n")
    i = 0
    
    for x in characters:
        i += 1
        print(str(i) + " - " + x[0])



player = createCharacter("PLAYER", 25, 10, 2, 5, 10)   
monster = createCharacter("MONSTER", 30, 20, 23, 5, 6)   
priest = createCharacter("PRIEST", 20, 25, 0, 2, 6)  
warrior = createCharacter("WARRIOR", 32, 5, 2, 5, 2)  
spider = createCharacter("SPIDER", 17, 5, 23, 5, 9)  
characters = allCharacters([player, monster, priest, warrior, spider])
for x in characters:
    print(str(x))
order = turnOrder(characters)
print(str(order))
order, characters = sortOrder(order, characters)
print(str(order))
print("----------------------------------------")
whoGoesFirst(characters)

#se escolher o spell e possior mp sufecientes
#spellefectvalue = -1 * (wd + d4)
#if input('rushdown') and (mpplayer >= SpellMPcost):
#   (player[2]) - 