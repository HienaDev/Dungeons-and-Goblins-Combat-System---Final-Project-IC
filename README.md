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



### Organização e explicação do código:

- No começo do trabalho pensamos que iria ser mais trabalhoso se não usasse mos um dicionário para definir as variáveis das personagens, então depois de alguma pesquisa e aprendizagem decidimos tratar das personagens com dicionários.

- Trabalhamos com o programa numa base maior com definições. No começo de cada ronda, e para começar a luta no jogo decidimos implementar um dado com um valor possível de 0 a 21 e adicionar ao já implementado valor de iniciativa de cada personagem.

- O personagem que obteve o maior valor será o que conseguirá passar á ação primeiro.

- Estes personagens podem ser um "Ogre", um "Goblin Shaman" e um "Goblin" que são os inimigos que o jogador e os seus personagens têm de abater.
As personagens do jogador são um "Priest", um "Warrior" e um "Rouge".

- Cada Personagem do jogador possui a opção de usar os seus spells especificos, atacar e descansar. Caso o jogador fizer uma personagem denscanbdar esta na sua ronda irás recuperare algum mana de volta.

- Para melhorar o projecto em termos estéticos importamos "termcolored" para dar uma maior cor e tornar mais fácil entender o que se está a passar e fazer a distinção de inimigo e aliado.

![](foto.png)




##### Referencias:

Durante tempos livres e de pesquisa, ideias foram trocadas com vários colegas, tal como ajuda fornecida pleos mesmos.

Alguns dos colegas:

- Ricardo Almeida - a21807601
- Paulo Silva
- Mariana Marques - 
- João Silva -



#### Links:


- https://stackoverflow.com/questions/10829650/delete-the-last-input-row-in-python

- https://stackoverflow.com/questions/517970/how-to-clear-the-interpreter-console

- https://www.w3schools.com/python/python_dictionaries.asp


