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

#def sortOrder(characters, order):

    


player = createCharacter("PLAYER", 25, 10, 2, 5, 10)   
monster = createCharacter("MONSTER", 30, 20, 23, 5, 6)   
characters = allCharacters((player, monster))
print(str(characters[0]) + "\n" + str(characters[1]))
print(str(turnOrder(characters)))
print("----------------------------------------")
print(str(sortOrder([5, 2, 9, 31, 23, 4, 69, 12])))