import tkinter as tk

top = tk.Tk()
drawingBoard = tk.Canvas(top, width = 600, height = 400, bg = "black")
# Code to add widgets will go here...
top.attributes("-topmost", 1)
top.geometry(f"266x400+300+200")
top.configure(bg='black')

def createCharacter(name, health, mana, armor, damage, iniative, loyalty):

    character = {
        "name" : name,
        "health" : health,
        "mana" : mana,
        "armor" : armor,
        "damage" : damage,
        "iniative" : iniative,
        "loyalty" : loyalty
    }

    return (character)

def displayOnScreen(message, x, y):

    drawingBoard.create_text(x, y, anchor = "center", text = message, fill = "white",  font = ("Minion Pro SmBd", "15"))


drawingBoard.create_rectangle(7, 8, 127, 84, outline = "white", width = 3)
drawingBoard.create_rectangle(4, 5, 130, 87, outline = "gray", width = 3)
drawingBoard.create_rectangle(138, 8, 258, 84, outline = "white", width = 3)
drawingBoard.create_rectangle(135, 5, 261, 87, outline = "gray", width = 3)

monster = createCharacter("Monster", 30, 20, 23, 5, 6)   
priest = createCharacter("Priest", 20, 25, 0, 2, 6)  
warrior = createCharacter("Warrior", 32, 5, 2, 5, 2) 

displayOnScreen((warrior["name"]), 70, 25)
displayOnScreen(("Health: " + str(warrior["health"])), 70, 45)
displayOnScreen(("Damage: " + str(warrior["damage"])), 70, 65)

displayOnScreen((priest["name"]), 200, 25)
displayOnScreen(("Health: " + str(priest["health"])), 200, 45)
displayOnScreen(("Damage: " + str(priest["damage"])), 200, 65)

drawingBoard.pack()

top.bind('<Escape>', lambda e: top.destroy())
top.mainloop()



#warrior = {
#    "name" : "Warrior",
#    "damage" : 5,
#    "health" : 32
#}
#
#print(warrior["name"])
#print(warrior["health"])
#warrior["health"] = warrior["health"] - 7
#print(warrior["health"])