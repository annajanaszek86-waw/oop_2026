#klasa = Szblon, Przepis
class Czlowiek:
    #istota
    gatunek = "Homo Sapiens"
    def __init__(self):
        #konstruktor
        #akt istnienia
       print("Niech powstanie Człowiek")

#powstawanie obiektu
#gotowanie z przepisu
adam = Czlowiek()
# print(type(adam))
# print(dir(Czlowiek))
# print(dir(adam))
print(adam.gatunek)