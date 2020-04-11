# 2.4. Porovnávanie dát. Vyhľadávanie podobných objektov
# Naivná podobnosť premenných rôznych typov [0; 1]
from enum import Enum

class Item:
    def __init__(self, cena: float, vzdialenost: int, hasDom: bool, noIzieb: str):
        self.cena = cena  # euro
        self.vzdialenost = vzdialenost  # minuty
        self.hasDom = hasDom
        self.noIzieb = noIzieb

# INPUT
variants = {
    'goal': Item(100, 5, 0, 'tri'), # this is what customer wants
    'A': Item(180, 30, 0, 'dve'), # the rest are possible variants and we can try to find the closest one to what he wants
    'B': Item(210, 15, 1, 'tri'),
    'C': Item(140, 45, 0, 'jedna')
}

# vzdialenost medzi variantami a 'goal'-om zakaznika, pozri vypis nizsie
def CalculateDistance(item1: Item, item2: Item):
    return (CalcPriceDiff(item1.cena, item2.cena) + 
            CalcDistDiff(item1.vzdialenost, item2.vzdialenost) + 
            int(item1.hasDom == item2.hasDom) + 
            int(item1.noIzieb == item2.noIzieb)) / len(variants)

# vzdialentost medzi cenou 
def CalcPriceDiff(a: float, b: float):
    maxPriceKey = max(variants, key=lambda k: variants[k].cena)
    minPriceKey = min(variants, key=lambda k: variants[k].cena)
    return 1 - abs(a - b) / (variants[maxPriceKey].cena - variants[minPriceKey].cena)

# vzdialenost medzi vzdialenostou v minutach
def CalcDistDiff(a: float, b: float):
    maxDistKey = max(variants, key=lambda k: variants[k].vzdialenost)
    minDistKey = min(variants, key=lambda k: variants[k].vzdialenost)
    return 1 - abs(a - b) / (variants[maxDistKey].vzdialenost - variants[minDistKey].vzdialenost)

# OUTPUT
first = True

# variant ktory ma najvacsie cislo je najblizsie k tomu co chceme 
# podobnost patri do intervalu <0,1> kde: 
#       0 - znamena ze prvky nie su podobne; 
#       1 - znamena ze prvky su zhodne vo vsetkych bodoch
for key, val in variants.items():
    if first:
        first = False
        continue
    
    print(f'variant {key}: {CalculateDistance(val, variants["goal"])}')