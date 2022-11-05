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

#Function that creates a tuple with the order of each character
def turnOrder(characters):

    order = []

    for character in characters:

        order.append(rollInitiative(character))
    
    return(order)


def sortOrder(order):

    aux = 0

    for i in range(len(order)):
        for index in range(len(order)):
            if (index < len(order) - 2):
                if (order[index] > order[index + 1]):
                    aux = order[index]
                    order[index] = order[index + 1]
                    order[index + 1] = aux
        print(str(i))
    return(order)


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

#def sortOrder(characters, order):

    
#def magicspells():
#    spells = ['rushdown', 'exorcism', 'mend']
#    if input ('rushdown')


#ola sou o henrique
#def magicspells():
#    spells = ['rushdown', 'exorcism', 'mend']
#    if input ('rushdown')


#ola sou o henrique


player = createCharacter("PLAYER", 25, 10, 2, 5, 10)   
monster = createCharacter("MONSTER", 30, 20, 23, 5, 6)   
priest = createCharacter("Priest", 20, 25, 0, 2, 6)
warrior = createCharacter("Warrior", 32, 5, 2, 5, 2)


characters = allCharacters((player, monster, priest, warrior))


print(str(characters[0]) + "\n" + str(characters[1]))
print(str(turnOrder(characters)))
print("----------------------------------------")
print(str(sortOrder([5, 2, 9, 31, 23, 4, 69, 12])))

#se escolher o spell e possior mp sufecientes
#spellefectvalue = -1 * (wd + d4)
#if input('rushdown') and (mpplayer >= SpellMPcost):
#   (player[2]) - 