
from BayesClassification import BayesClassification

# TEST zadanie 1-9
header = ['Vek',	'Astigmatizmus',	'Zrak',	'Pohlavie',	'Šošovky']
data = [
    ['Dospelý',	'Áno',	'Normálny',	'Muž',	'Nie'],
    ['Starý',	'Nie',	'Zmenšeny',	'Muž',	'Soft'],
    ['Starý',	'Nie',	'Zmenšeny',	'Žena',	'Soft'],
    ['Dospelý',	'Nie',	'Normálny',	'Žena',	'Nie'],
    ['Mladý',	'Nie',	'Normálny',	'Muž',	'Nie'],
    ['Mladý',	'Nie',	'Zmenšeny',	'Muž',	'Soft'],
    ['Mladý',	'Nie',	'Zmenšeny',	'Žena',	'Nie'],
    ['Starý',	'Áno',	'Zmenšeny',	'Muž',	'Hard'],
    ['Starý',	'Áno',	'Zmenšeny',	'Žena',	'Soft'],
    ['Dospelý',	'Áno',	'Zmenšeny',	'Muž',	'Soft'],
    ['Mladý',	'Áno',	'Normálny',	'Muž',	'Soft'],
    ['Dospelý',	'Nie',	'Zmenšeny',	'Žena',	'Hard'],
    ['Dospelý',	'Áno',	'Normálny',	'Žena',	'Soft'],
    ['Mladý',	'Áno',	'Normálny',	'Muž',	'Hard'],
    ['Starý',	'Áno',	'Normálny',	'Žena',	'Hard'],   
]
new_data1 =  ['Dospelý',	'Nie',	'Normálny',	'Muž', None]
new_data2 =  ['Starý',	'Áno',	'Zmenšeny',	'Žena',	None]

BayesClassification(data, header, new_data1)
BayesClassification(data, header, new_data2)

data = [
    [  41,	'Áno',	'Normálny',	'Muž',	'Nie'],
    [   55,	'Nie',	'Zmenšeny',	'Muž',	'Soft'],
    [   65,	'Nie',	'Zmenšeny',	'Žena',	'Soft'],
    [  33,	'Nie',	'Normálny',	'Žena',	'Nie'],
    [ 14,	'Nie',	'Normálny',	'Muž',	'Nie'],
    [ 18,	'Nie',	'Zmenšeny',	'Muž',	'Soft'],
    [ 10,	'Nie',	'Zmenšeny',	'Žena',	'Nie'],
    [   72,	'Áno',	'Zmenšeny',	'Muž',	'Hard'],
    [   64,	'Áno',	'Zmenšeny',	'Žena',	'Soft'],
    [  44,	'Áno',	'Zmenšeny',	'Muž',	'Soft'],
    [ 19,	'Áno',	'Normálny',	'Muž',	'Soft'],
    [  40,	'Nie',	'Zmenšeny',	'Žena',	'Hard'],
    [  38,	'Áno',	'Normálny',	'Žena',	'Soft'],
    [ 25,	'Áno',	'Normálny',	'Muž',	'Hard'],
    [   62,	'Áno',	'Normálny',	'Žena',	'Hard']
]
new_data1 =  [44,	'Nie',	'Normálny',	'Muž', None]
new_data2 =  [50,	'Áno',	'Zmenšeny',	'Žena',	None]

BayesClassification(data, header, new_data1)
BayesClassification(data, header, new_data2)
################################################################




# TEST zadanie minuly rok
header = ['Vek',	'Pohlavie',	'Astigmatizmus',	'Zrak',	'Sosovky']
data = [
    [18,	'muz',	False,	'Good',	'soft'],
    [19,	'muz',	True,	'Bad',	'soft'],
    [14,	'muz',	False,	'Bad',	'nie'],
    [10,	'zena',	True,	'Bad',	'nie'],
    [25,	'zena',	True,	'Bad',	'hard'],
    [44,	'muz',	True,	'Good',	'soft'],
    [41,	'muz',	True,	'Good',	'nie'],
    [33,	'zena',	False,	'Bad',	'nie'],
    [35,	'zena',	False,	'Good',	'soft'],
    [38,	'zena',	True,	'Good',	'soft'],
    [70,	'muz',	True,	'Good',	'hard'],
    [65,	'muz',	True,	'Good',	'hard'],
    [64,	'zena',	True,	'Good',	'hard'],
    [61,	'zena',	False,	'Bad',	'hard'],
    [55,	'muz',	False,	'Good',	'soft']
]
new_data1 = [44,	'muz',	False,	'Bad',	    None]
new_data2 = [50,	'zena',	True,	'Good',	None]

BayesClassification(data, header, new_data1)
BayesClassification(data, header, new_data2)
################################################################




# TEST zadanie minuly rok
header = ['Tumor',  'History',    'Heredity',   'Age',    'Cancer']
data = [
    #Tumor  #History    #Heredity   #Age    #Cancer
    ['confirmed',	'high',	'yes',	'younger',	'high'],
    ['confirmed',	'high',	'yes',	'elder',	'high'],
    ['no',	'high',	'yes',	'younger',	'low'],
    ['non confirmed',	'medium',	'yes',	'younger',	'low'],
    ['non confirmed',	'low',	'no',	'younger',	'low'],
    ['non confirmed',	'low',	'no',	'elder',	'high'],
    ['no',	'low',	'no',	'elder',	'low'],
    ['confirmed',	'medium',	'yes',	'younger',	'high'],
    ['confirmed',	'low',	'no',	'younger',	'low'],
    ['non confirmed',	'medium',	'no',	'younger',	'low'],
    ['confirmed',	'medium',	'no',	'elder',	'low'],
    ['no',	'medium',	'yes',	'elder',	'low'],
    ['no',	'high',	'no',	'younger',	'low'],
    ['non confirmed',	'medium',	'yes',	'elder',	'high']
]

new_data1 = ['confirmed',	'low',	'yes',	'elder', None]
BayesClassification(data, header, new_data1)

data = [
    #Tumor  #History    #Heredity   #Age    #Cancer
    ['confirmed',	85,	'yes',	'younger',	'high'],
    ['confirmed',	80,	'yes',	'elder',	'high'],
    ['no',	83,	'yes',	'younger',	'low'],
    ['non confirmed',	70,	'yes',	'younger',	'low'],
    ['non confirmed',	68,	'no',	'younger',	'low'],
    ['non confirmed',	65,	'no',	'elder',	'high'],
    ['no',	64,	'no',	'elder',	'low'],
    ['confirmed',	72,	'yes',	'younger',	'high'],
    ['confirmed',	69,	'no',	'younger',	'low'],
    ['non confirmed',	75,	'no',	'younger',	'low'],
    ['confirmed',	75,	'no',	'elder',	'low'],
    ['no',	72,	'yes',	'elder',	'low'],
    ['no',	81,	'no',	'younger',	'low'],
    ['non confirmed',	71,	'yes',	'elder',	'high']
]

new_data2 = ['confirmed',	80,	'yes',	'elder', None]
BayesClassification(data, header, new_data2)