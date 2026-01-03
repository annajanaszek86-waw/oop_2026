#klasa = Szblon, Przepis
class Czlowiek:
    #istota
    gatunek = "Homo Sapiens"
    def __init__(self, imie):
        #konstruktor
        #akt istnienia
       print(f"Niech powstanie Człowiek o imieniu {imie}")
       self.imie = imie
        # adam.imie = "Adam"
        # ewa.imie = "Ewa"

#powstawanie obiektu
#gotowanie z przepisu
adam = Czlowiek("Adam")
ewa = Czlowiek("Ewa")
# print(type(adam))
# print(dir(Czlowiek))
# print(dir(adam))
print(adam.gatunek)
print(ewa.gatunek)
print(adam.imie)
print(ewa.imie)