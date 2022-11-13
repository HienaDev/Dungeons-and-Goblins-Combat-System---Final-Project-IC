# **Dungeons and Dragons - Introdução à computação.**

## Authorship: 

##### Work done by:

- Henrique Monteiro - a22202855
- António Rodrigo - a22202884

##### Functions addressed by each element:
\
 **António**:

- Added createCharacter function;
- Added sorting functions;
- Added function to print turn order on screen;
- Added the game's UI;
- Added function to choose the action of each character;
- Added "YOU WIN/YOU LOSE" text;
- Added new characters ( Goblin Shaman, Goblin, Rogue);
- Added colors to the printed text;
- Added timer inbetween actions;
- Added most of the commentary;
- Added characters stats to output;


**Henrique**:


- Added function to choose spells;
- Added spells: (Poison, Mend, Exorcism, DamageBuff, Rushdown, DamageBuff, Arrow Rain);
- Added spell targetting;
- Added the option to backtrack on menus and improved text clarity on the output;
- Added comments;
- Added the rest action;
- Added goblin shaman spell phase;



### Solution Description:

The project was carefully planned and separated in parts so it would be easier to understand and create. For that we started by work in the :

- Characters:  To create the characters and link them automatically to their respective status, we decided to invest in the dictionary option in python. So every time we needed to call a variable of a certain character it would be easier.

- Turn Order: After creating the characters and their status, we created the order which they were going to attack. For that we created a dice between 1 and 20, and when used, the number that the dice decides is added to the number of the character initiative. After adding the two values, the one that has the biggest combination is the first one to play and keeps on going until all the characters play in that round.

- Choose Action: After the order is showend, the characters can choose what action is available for them to do. The characters the player controls can use three actions:

 - Rest - (rest()): The character rests the round not being able to attack or use spells but recovers mana;
 
  - Attack - (attackPhase): The character inflicts damage up on the opponent; 
  
  - Spells - (spellPhase): The character chooses a spell to cast. Some characters have spells in the area, others can use the spells to heal.

![](foto.png)







#### Complicated algorithms implemented:

- createCharacter(name, health, mana, armor, damage, initiative, loyalty, poisoned, damageBoost, alive):
    -   This function takes 10 arguments, string "name", integer "health", integer "mana", integer "armor", integer "damage", integer "initiative", string "loyalty", integer "poisoned", integer "damageBoost" and integer "alive";
    -   It then creates a dictionary "character" with those exact stats.
    
- rollIniative(character):
    - This function takes 1 argument, dictionary "character";
    - It then gets a random number from 1 to 20;
    - After that it checks if the character is alive;
    - If the character is alive it adds that random number with the "iniative" stat of the dictionary "character" and returns that addition.
    
- turnOrder(characters):
    - This function takes 1 argument, list "characters";
    - It then creates a list "order", and adds the rollIniative(character) of every character to that list;
    - It then returns "order".

- sortOrder(order, characters):
    - This function takes 2 arguments, list "order" and list "characters";
    - The list "order" has the iniative roll of each character sorted the same way as the list "characters". This means that the index 1 of the list "order" is, for example, the roll of the priest, and the index 1 of the list "characters" is the character priest;
    - Than the function starts sorting the list "order" and everytime it makes a swap in the list "order", it makes the exact same swap in the list "characters". Once the sorting ends we end up with the character list sorted by the iniative order;
    - This function runs through  a loop "len(order)"" times to make sure it sorts through every possible swap.
 
- targetChoice(friendship):
    - This function takes 1 argument, integer "friendship";
    - If friendship is 0 you get every enemy as an option to target on the output. If friendship is 1 you get every ally as an option to target on the ouput;
    - The function then asks the user for input on who to target and returns that choice;
    - If the input is not a valid choice it asks the user again for input.

- damageBuff():
    - This function takes no arguments;
    - This function reduces the goblin shaman's mana by 8;
    - Then it gets a random number from 1 to 7. If its 7 this function prints that the goblin shaman failed to use a spell;
    - If its anything other than 1 the goblin shaman "uses" the spell and adds 1 to the "damageBoost" stat of every character with loyalty "evil".
    
- arrowRain():
    - This function takes no arguments;
    - This function gets a random number from 1 to 8;
    - Then it reduces the rogue's mana by 8;
    - After that it reduces every character with "evil" loyalty by: (rogue's damage stat / 2 + the randomly generated number value) - "evil" character armor stat.
    
- poison():
    - This function takes no arguments;
    - This function reduces the goblin shaman's mana by 6;
    - Then it gets a random number from 1 to 3 to randomly choose a character to attack;
    - Then it gets a random number from 2 to 5 and adds that amount to the "poisoned" stat of the target.
    
- rushDown():
    - This function takes no arguments;
    - This function gets a random number from 1 to 4;
    - After that it checks if the warrior's mana stat is above rushdown's mana cost if it isn't it returns 0;
    - Then the function calls for the function targetChoice() to choose who to target with the spell;
    - Then it reduces the warrior's mana by 5;
    - Finally it reduces the target's "health" stat by (warrior "damage" stat + the randomly generated number).
    
- exorcism():
    - This function takes no arguments;
    - This function gets a random number from 1 to 4;
    - After that it checks if the priest's mana stat is above exorcism's mana cost if it isn't it returns 0;
    - Then the function calls for the function targetChoice() to choose who to target with the spell;
    - Then it reduces the priest's mana by 5;
    - Finally it reduces the target's "health" stat by (the randomly generated number * 2).
    
- mend():
    - This function takes no arguments;
    - This function gets a random number from 1 to 6;
    - After that it checks if the priest's mana stat is above mend's mana cost if it isn't it returns 0;
    - Then the function calls for the function targetChoice() to choose who to target with the spell;
    - Then it reduces the priest's mana by 3;
    - Finally it increases the target's "health" stat by (the randomly generated number + the priest's "damage" stat).

- spellChooseWarrior():
    - This function takes no arguments;
    - This function first asks for the user's input;
    - If the user enters 1 or rushdown this function calls for the function rushDown();
    - If the user enters 0 this functions returns 0;
    - If the user enter any other input the function asks for input again.
    
- spellChooseRogue():
    - This function takes no arguments;
    - This function first asks for the user's input;
    - If the user enters 1 or arrowrain, the function checks if the rogue's "mana" stat is smaller than arrow rain's spell cost. If it is it asks for the user's input again. If not this function calls for the function arrowRain();
    - If the user enters 0 this functions returns 0;
    - If the user enter any other input the function asks for input again.

- spellChoosePriest():
    - This function takes no arguments;
    - This function first asks for the user's input;
    - If the user enters 1 or exorcism this function calls for the function exorcism();
    - If the user enters 2 or mend this function calls for the function mend();
    - If the user enters 0 this functions returns 0;
    - If the user enter any other input the function asks for input again.
    
- spellChooseGS():
    - This function takes no arguments;
    - This function gets a randomly generated number between 1 and 2;
    - Then it checks if the goblinShaman character's "mana" stat is above 5;
    - If it is it then checks if the randomly generated number is 1:
        - If it is, it calls for the function poison().
    - If the randomly generated number is 2 it checks if the goblinShaman's "mana" stat is above 7:
        - If it is it calls for the function damageBuff();
        - If it isn't it calls for the rest(goblinShaman) function.
    - If the goblinShaman character's "mana" stat is under 5, the function calls for the rest(goblinShaman) function.
    
- spellPhase(character):
    - This function takes 1 argument, dictionary "character";
    - It then checks if the character's "name" stat is either rogue's "name" stat, priest's "name" stat, warrior's "name" stat or the goblinShaman's "name" stat;
    - It then calls for the functions spellChooseRogue(), spellChoosePriest(), spellChooseWarrior() or spellChooseGS() respectively.
    
- attackPhase(character):
    - This function takes 1 argument, dictionary "character";
    - The function first checks the character's "loyalty" stat. If it's "good", the function presents the user with targets to choose from to attack. If it's "evil", the function randomly chooses a target to attack;
    - After the target has been chosen by the player this function calculates the damage with the character's "damage" stat and the possible modifiers. Than it updates the target's health stat depending on how much damage he has been dealt.
    
- rest(character):
    - This function takes 1 argument, dictionary "character";
    - The function then increases the character's "mana" stat by (character's "maxMana" stat * ( 2 / 3 ) ), unless the character's "name" stat is the warrior's name, which increases the warrior's "mana" stat to warrior's "maxMana" stat.

- chooseAction(character):
    - This function takes 1 argument, dictionary "character";
    - The function then checks if the character is alive by checking his "alive" stat, if it's 0 it doesn't act, if it's 1 he acts;
    - Then it checks the character's "loyalty" stat. If it's "good", the function presents the user with actions to choose from. If it's "evil", the function randomly choose an action depending on who the character is.

- actionPhase(characters):
    - This function takes 1 argument, list "characters";
    - This function first checks if any of the parties combined "health" stat is equal or under 0;
    - It then deals poison damage to the character if his "poison" stat is higher then 0;
    - After that if the character is still alive the function calls the function chooseAction(character).

##### Referencias:

In our reaserch and free time, we traded ideas and fixes with some of our class collegues. Some of them were: 

- Ricardo Almeida - a21807601
- Paulo Silva
- Mariana Marques - 
- João Silva -



#### Links:


- https://stackoverflow.com/questions/10829650/delete-the-last-input-row-in-python

- https://stackoverflow.com/questions/517970/how-to-clear-the-interpreter-console

- https://www.w3schools.com/python/python_dictionaries.asp


