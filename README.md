## Dungeons and Dragons - Introdução à computação.

### Autoria: 
##### Trabalho realizado por :

- Henrique Monteiro - a22202855
- António Rodrigo - a22202884

#### Partes abordadas por cada elemento:

O projeto teve início com ambos os membros do projeto a trabalhar na ideia e como iriamos começar a trabalhar no esqueleto do código.

Temas abordados e código realizado por **António**:

- Adicionou a função para criar personagens;
- Adicionou a ordem dos turnos dos personagens;
- Adicionou a função para mostrar a ordem de quem joga primeiro;
- Adicionou o "Users Interface";
- Adicionou a função para escolher a ação dos personagens;
- Adicionou a arte de "YOUWIN" e "YOULOSE";
- Adicionou novas personagens ( Goblin Shaman, Goblin, "Rougue")
- Adicionou cores ao texto exposto;
- Adicionou um timer entre as ações dos monstros inimigos;
- Adicionou comentário;
- Adicionou vários fixes a bugs;
- Adicionou os status dos personagens no output;


Temas abordados e código realizado por **Henrique**:


- Adicionou a ação de "Spells";
- Adicionou "Spells": ("Poison, Mend, Exorcism);
- Adicionou quem são os targets dos "Spells";
- Adicionou nova tentativa de spells para novas personagens( DamageBuff, Arrow Rain );
- Adicionou um novo spell ( Poison );
- Adicionou a opção de voltar atrás e melhorou os visuáis;
- Adicionou comentário;
- Adicionou opção de "rest" (descanso que aumenta mana);
- Adicionou a "SpellFase" do Goblin Shaman;
- Adicionou a versão final do "Spell" Poison;
- Adicionou um pequeno hot fix;


### Organização e explicação do código:

- No começo do trabalho pensamos que iria ser mais trabalhoso se não usasse mos um dicionário para definir as variáveis das personagens, então depois de alguma pesquisa e aprendizagem decidimos tratar das personagens com dicionários.

- Trabalhamos com o programa numa base maior com definições. No começo de cada ronda, e para começar a luta no jogo decidimos implementar um dado com um valor possível de 0 a 21 e adicionar ao já implementado valor de iniciativa de cada personagem.

- O personagem que obteve o maior valor será o que conseguirá passar á ação primeiro.

- Estes personagens podem ser um "Ogre", um "Goblin Shaman" e um "Goblin" que são os inimigos que o jogador e os seus personagens têm de abater.
As personagens do jogador são um "Priest", um "Warrior" e um "Rouge".

- Cada Personagem do jogador possui a opção de usar os seus spells especificos, atacar e descansar. Caso o jogador fizer uma personagem denscanbdar esta na sua ronda irás recuperare algum mana de volta.

- Para melhorar o projecto em termos estéticos importamos "termcolored" para dar uma maior cor e tornar mais fácil entender o que se está a passar e fazer a distinção de inimigo e aliado.

![](foto.png)

eveverv

