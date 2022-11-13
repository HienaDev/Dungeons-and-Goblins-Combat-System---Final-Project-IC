Henriqueta = []

Futebol = ["Messi", "Ronaldo", "Pele", "Nuno Gomes", "Maradona"]
Videojogos = ["Persona 5", "Apex", "LoL", "osu", "AC"]


for n in range(5):
    Henriqueta.append(Futebol)
    print(Henriqueta)

for i in Henriqueta:
    Henriqueta.append(Videojogos)
    print(Henriqueta) 


print("Futebol: " + Futebol)
print("Videojogos: " + Videojogos)
print("")
print("Henriqueta: " + Henriqueta)