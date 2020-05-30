# 2.4. Porovnávanie dát. Vyhľadávanie podobných objektov
# Podobnosť dvojstavových premenných [0; 1]
from enum import Enum
from Statistics.Coincidence import Coincidence

class Item:
	def __init__(self, name: str, isTycinka: bool, isDezert: bool, isKolac: bool):
		self.name = name
		self.isTycinka = isTycinka
		self.isDezert = isDezert
		self.isKolac = isKolac
		
class Dezert(Enum):
	Tycinka = 1
	Dezert = 2
	Kolac = 3

table = [
	Item('Cokolada', 1, 0, 1),
	Item('Maslo', 0, 0, 1),
	Item('Tekutina', 0, 1, 0),
	Item('Ovocna Esencia', 0, 0, 1),
	Item('Kovovy obal', 0, 1, 1),
	Item('Mini-balenie', 1, 1, 0),
	Item('Cukor', 1, 1, 1),
	Item('Ryza', 1, 0, 1),
	Item('Umele sladidlo', 0, 0, 1),
	Item('Farbivo', 0, 0, 1)
]

resuts = {
	'tycinkaAndDezert' : sum(1 for i in table if i.isTycinka and i.isDezert),
	'tycinkaAndKolac' : sum(1 for i in table if i.isTycinka and i.isKolac),
	'dezertAndKolac' : sum(1 for i in table if not i.isDezert and i.isKolac),

	'notTycinkaAndNotDezert' : sum(
		1 for i in table if not i.isTycinka and not i.isDezert),
	'notTycinkaAndNotKolac' : sum(
		1 for i in table if not i.isTycinka and not i.isKolac),
	'notDezertAndNotKolac' : sum(
		1 for i in table if not i.isDezert and not i.isKolac),

	'tycinkaAndNotDezert' : sum(1 for i in table if i.isTycinka and not i.isDezert),
	'tycinkaAndNotKolac' : sum(1 for i in table if i.isTycinka and not i.isKolac),
	'notTycinkaAndKolac' : sum(1 for i in table if not i.isTycinka and i.isKolac),
	'notTycinkaAndDezert' : sum(1 for i in table if not i.isTycinka and i.isDezert),

	'dezertAndNotKolac' : sum(1 for i in table if not i.isDezert and not i.isKolac),
	'notDezertAndKolac' : sum(1 for i in table if not not i.isDezert and i.isKolac)
}

def PrintResults():
	for key, value in resuts.items():
		print(key + ': ' + str(value))

	print(f'Podobnost({Dezert.Tycinka}, {Dezert.Dezert})')
	print(f'Russel: {Coincidence.russel(resuts["tycinkaAndDezert"], len(table))}')
	print(f'Sokal: {Coincidence.sokal(resuts["tycinkaAndDezert"], resuts["notTycinkaAndNotDezert"], len(table))}')
	print(f'Jaccard: {Coincidence.jaccard(resuts["tycinkaAndDezert"], resuts["notTycinkaAndNotDezert"], len(table))}')

# ULOHY
# 1. Mame 2 objekty A a B, ktoré popísane 20 dvojstavovými atribútmi
ATrueIdxs = [1,2,3,4,8,9,11,14,16,17,20]
BTrueIdxs = [2,3,5,8,10,11,14,15,16,18,19,20]

def PrintResults1():
	A = [False for i in range(21)]
	B = [False for i in range(21)]

	for i in ATrueIdxs:
		A[i] = True

	for i in BTrueIdxs:
		B[i] = True

	possitive_coin = 0
	negative_coin = 0

	for i in range(21):
		if A[i] == B[i] and A[i] is True:
			possitive_coin += 1
		elif A[i] == B[i] and A[i] is False:
			negative_coin += 1
   
	print(f'Jaccard: {Coincidence.jaccard(possitive_coin, negative_coin, len(A))}')
	print(f'Russel: {Coincidence.russel(possitive_coin, len(A))}')
	print(f'Sokal: {Coincidence.sokal(possitive_coin, negative_coin, len(A))}')
 
PrintResults1()