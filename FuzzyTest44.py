from enum import Enum
from Statistics.Statistics import Statistics
from Statistics.Information import Information
from Statistics.Entropy import Entropy
from Statistics.Cardinality import Cardinality

class A:
    A1 = 0
    A2 = 1
    A3 = 2
    A4 = 3
    B = 4
    Alfa = .19
    Beta = .75

data=[
    #A1          A2               A3          A4          B
    [[0.9, 0.1], [0.2, 0.8, 0.0], [0.3, 0.7], [0.1, 0.9], [0.0, 0.6, 0.4]],
    [[0.7, 0.3], [0.2, 0.3, 0.5], [0.9, 0.1], [0.9, 0.1], [0.0, 0.8, 0.2]],
    [[0.9, 0.1], [1.0, 0.0, 0.0], [0.3, 0.7], [0.7, 0.3], [0.0, 0.7, 0.3]],
    [[1.0, 0.0], [0.1, 0.5, 0.4], [0.2, 0.8], [0.5, 0.5], [0.0, 0.1, 0.9]],
    [[0.0, 1.0], [0.1, 0.3, 0.6], [0.7, 0.3], [1.0, 0.0], [0.0, 0.9, 0.1]],
    [[0.9, 0.1], [0.0, 1.0, 0.0], [1.0, 0.0], [0.7, 0.3], [0.2, 0.0, 0.8]],
    [[1.0, 0.0], [0.9, 0.1, 0.0], [0.3, 0.7], [0.9, 0.1], [0.0, 0.6, 0.4]],
    [[0.2, 0.8], [0.2, 0.7, 0.1], [0.8, 0.2], [0.7, 0.3], [0.0, 0.0, 1.0]],
    [[0.1, 0.9], [0.3, 0.4, 0.3], [0.3, 0.7], [0.7, 0.3], [0.0, 0.8, 0.2]],
    [[0.9, 0.1], [0.7, 0.3, 0.0], [0.7, 0.3], [0.7, 0.3], [0.0, 1.0, 0.0]],
    [[0.7, 0.3], [0.9, 0.1, 0.0], [0.4, 0.6], [0.8, 0.2], [0.3, 0.7, 0.0]],
    [[0.2, 0.8], [0.1, 0.8, 0.1], [0.3, 0.7], [0.7, 0.3], [0.0, 0.7, 0.3]],
    [[0.0, 1.0], [0.0, 0.2, 0.8], [1.0, 0.0], [0.9, 0.1], [0.0, 0.9, 0.1]],
    [[0.0, 1.0], [0.9, 0.1, 0.0], [0.7, 0.3], [0.9, 0.1], [0.8, 0.1, 0.1]],
    [[0.9, 0.1], [0.0, 0.7, 0.3], [0.8, 0.2], [0.7, 0.3], [0.0, 0.7, 0.3]]
]

max = '<--- max'
min = '<--- min'
koniec = ' <--- koniec'
ltAlfa = f' < {A.Alfa} {koniec}'
gtBeta = f' > {A.Beta} {koniec}'

print(f'Alfa: {A.Alfa}')
print(f'Beta: {A.Beta}')
print()

##### vypocitame vstupnu entropiu vystupneho atributu
print(f'H(B) = {Entropy.Personal.fuzzy(A.B, data)}')
print(f'B1 = {Cardinality.joint({ A.B : 0 }, data) / Cardinality.personal(A.B, data)}')
print(f'B2 = {Cardinality.joint({ A.B : 1 }, data) / Cardinality.personal(A.B, data)}')
print(f'B3 = {Cardinality.joint({ A.B : 2 }, data) / Cardinality.personal(A.B, data)}')
print('#####')
print(f'I(B;A1) = {Entropy.Mutual._fuzzy({ A.B: None, A.A1: None}, data)}')
print(f'I(B;A2) = {Entropy.Mutual._fuzzy({ A.B: None, A.A2: None}, data)} {max}')
print(f'I(B;A3) = {Entropy.Mutual._fuzzy({ A.B: None, A.A3: None}, data)}')
print(f'I(B;A4) = {Entropy.Mutual._fuzzy({ A.B: None, A.A4: None}, data)}')
##### vyberieme minimum z tychto podmienenych entropii
print(f'H(B|A1) = {Entropy.Conditional._fuzzy({ A.B : None, A.A1 : None }, data)}')
print(f'H(B|A2) = {Entropy.Conditional._fuzzy({ A.B : None, A.A2 : None }, data)} {min}')
print(f'H(B|A3) = {Entropy.Conditional._fuzzy({ A.B : None, A.A3 : None }, data)}')
print(f'H(B|A4) = {Entropy.Conditional._fuzzy({ A.B : None, A.A4 : None }, data)}')
print()


#### najlepsie vyslo A2 
#### pocitame vetvu A21
print('\tVetva: B -> A21 ------------------')
print(f'\tH(B|A21) = {Entropy.Conditional._fuzzy({ A.B : None, A.A2 : 0 }, data)}')
print(f'\tB1 = {Cardinality.resulting({ A.B : 0, A.A2 : 0 }, data)}')
print(f'\tB2 = {Cardinality.resulting({ A.B : 1, A.A2 : 0 }, data)}')
print(f'\tB3 = {Cardinality.resulting({ A.B : 2, A.A2 : 0 }, data)}')
print(f'\tf = {Cardinality.joint({ A.A2 : 0 }, data) / Cardinality.personal(A.A2, data)}')
print('\t#####')
print(f'\tI(B;A21,A1) = {Entropy.Mutual._fuzzy({ A.B: None, A.A2 : 0, A.A1: None}, data)} {max}')
print(f'\tI(B;A21,A3) = {Entropy.Mutual._fuzzy({ A.B: None, A.A2 : 0, A.A3: None}, data)}')
print(f'\tI(B;A21,A4) = {Entropy.Mutual._fuzzy({ A.B: None, A.A2 : 0, A.A4: None}, data)}')
print(f'\tH(B|A21,A1) = {Entropy.Conditional._fuzzy({ A.B : None, A.A2 : 0, A.A1 : None }, data)} {min}')
print(f'\tH(B|A21,A3) = {Entropy.Conditional._fuzzy({ A.B : None, A.A2 : 0, A.A3 : None }, data)}')
print(f'\tH(B|A21,A4) = {Entropy.Conditional._fuzzy({ A.B : None, A.A2 : 0, A.A4 : None }, data)}')
print()

## najlepsie vyslo A1
#### pocitame vetvu A21 -> A11
print('\t\tVetva: B -> A21 -> A11------------------')
print(f'\t\tH(B|A21,A11) = {Entropy.Conditional._fuzzy({ A.B : None, A.A2 : 0, A.A1 : 0 }, data)}')
print(f'\t\tB1 = {Cardinality.resulting({ A.B : 0, A.A2 : 0, A.A1 : 0 }, data)}')
print(f'\t\tB2 = {Cardinality.resulting({ A.B : 1, A.A2 : 0, A.A1 : 0 }, data)}')
print(f'\t\tB3 = {Cardinality.resulting({ A.B : 2, A.A2 : 0, A.A1 : 0 }, data)}')
print(f'\t\tf = {Cardinality.joint({ A.A2 : 0, A.A1 : 0}, data) / Cardinality.personal(A.A2, data)}')
print('\t\t#####')
print(f'\t\tI(B;A21,A11,A3) = {Entropy.Mutual._fuzzy({ A.B: None, A.A2 : 0, A.A1 : 0, A.A3: None}, data)} {max}')
print(f'\t\tI(B;A21,A11,A4) = {Entropy.Mutual._fuzzy({ A.B: None, A.A2 : 0, A.A1 : 0, A.A4: None}, data)}')
print(f'\t\tH(B|A21,A11,A3) = {Entropy.Conditional._fuzzy({ A.B : None, A.A2 : 0, A.A1 : 0, A.A3 : None }, data)} {min}')
print(f'\t\tH(B|A21,A11,A4) = {Entropy.Conditional._fuzzy({ A.B : None, A.A2 : 0, A.A1 : 0, A.A4 : None }, data)}')
print()

## najlepsie vyslo A3
#### pocitame vetvu A21 -> A11 -> A31
print('\t\t\tVetva: B -> A21 -> A11 -> A31------------------')
print(f'\t\t\tH(B|A21,A11,A31) = {Entropy.Conditional._fuzzy({ A.B : None, A.A2 : 0, A.A1 : 0, A.A3 : 0 }, data)}')
print(f'\t\t\tB1 = {Cardinality.resulting({ A.B : 0, A.A2 : 0, A.A1 : 0, A.A3 : 0 }, data)}')
print(f'\t\t\tB2 = {Cardinality.resulting({ A.B : 1, A.A2 : 0, A.A1 : 0, A.A3 : 0 }, data)} {gtBeta}')
print(f'\t\t\tB3 = {Cardinality.resulting({ A.B : 2, A.A2 : 0, A.A1 : 0, A.A3 : 0 }, data)}')
print(f'\t\t\tf = {Cardinality.joint({ A.A2 : 0, A.A1 : 0, A.A3 : 0 }, data) / Cardinality.personal(A.A2, data)} {ltAlfa}')
#### xxx
print()

#### pocitame vetvu A21 -> A11 -> A32
print('\t\t\tVetva: B -> A21 -> A11 -> A32------------------')
print(f'\t\t\tH(B|A21,A11,A32) = {Entropy.Conditional._fuzzy({ A.B : None, A.A2 : 0, A.A1 : 0, A.A3 : 1 }, data)}')
print(f'\t\t\tB1 = {Cardinality.resulting({ A.B : 0, A.A2 : 0, A.A1 : 0, A.A3 : 1 }, data)}')
print(f'\t\t\tB2 = {Cardinality.resulting({ A.B : 1, A.A2 : 0, A.A1 : 0, A.A3 : 1 }, data)}')
print(f'\t\t\tB3 = {Cardinality.resulting({ A.B : 2, A.A2 : 0, A.A1 : 0, A.A3 : 1 }, data)}')
print(f'\t\t\tf = {Cardinality.joint({ A.A2 : 0, A.A1 : 0, A.A3 : 1 }, data) / Cardinality.personal(A.A2, data)} {ltAlfa}')
#### xxx
print()




#### pocitame vetvu A21 -> A12
print('\t\tVetva: B -> A21 -> A12------------------')
print(f'\t\tH(B|A21,A12) = {Entropy.Conditional._fuzzy({ A.B : None, A.A2 : 0, A.A1 : 1 }, data)}')
print(f'\t\tB1 = {Cardinality.resulting({ A.B : 0, A.A2 : 0, A.A1 : 1 }, data)}')
print(f'\t\tB2 = {Cardinality.resulting({ A.B : 1, A.A2 : 0, A.A1 : 1 }, data)}')
print(f'\t\tB3 = {Cardinality.resulting({ A.B : 2, A.A2 : 0, A.A1 : 1 }, data)}')
print(f'\t\tf = {Cardinality.joint({ A.A2 : 0, A.A1 : 1 }, data) / Cardinality.personal(A.A2, data)} {ltAlfa}')
#### xxx
print()







#### pocitame vetvu A22
print('\tVetva: B -> A22 ------------------')
print(f'\tH(B|A22) = {Entropy.Conditional.fuzzy(A.B, A.A2, data, 1)}')
print(f'\tH(B|A22). = {Entropy.Conditional._fuzzy({ A.B : None, A.A2 : 1 }, data)}')
print(f'\tB1 = {Cardinality.resulting({ A.B : 0, A.A2 : 1 }, data)}')
print(f'\tB2 = {Cardinality.resulting({ A.B : 1, A.A2 : 1 }, data)}')
print(f'\tB3 = {Cardinality.resulting({ A.B : 2, A.A2 : 1 }, data)}')
print(f'\tf = {Cardinality.joint({ A.A2 : 1 }, data) / Cardinality.personal(A.A2, data)}')
print('\t#####')
print(f'\tI(B;A22,A1) = {Entropy.Mutual._fuzzy({ A.B: None, A.A2 : 1, A.A1: None}, data)}')
print(f'\tI(B;A22,A3) = {Entropy.Mutual._fuzzy({ A.B: None, A.A2 : 1, A.A3: None}, data)} {max}')
print(f'\tI(B;A22,A4) = {Entropy.Mutual._fuzzy({ A.B: None, A.A2 : 1, A.A4: None}, data)}')
print(f'\tH(B|A22,A1) = {Entropy.Conditional._fuzzy({ A.B : None, A.A2 : 1, A.A1 : None }, data)}')
print(f'\tH(B|A22,A3) = {Entropy.Conditional._fuzzy({ A.B : None, A.A2 : 1, A.A3 : None }, data)} {min}')
print(f'\tH(B|A22,A4) = {Entropy.Conditional._fuzzy({ A.B : None, A.A2 : 1, A.A4 : None }, data)}')
print()

## najlepsie vyslo A3
#### pocitame vetvu A22 -> A31
print('\t\tVetva: B -> A22 -> A31------------------')
print(f'\t\tH(B|A22,A31) = {Entropy.Conditional._fuzzy({ A.B : None, A.A2 : 1, A.A3 : 0 }, data)}')
print(f'\t\tB1 = {Cardinality.resulting({ A.B : 0, A.A2 : 1, A.A3 : 0 }, data)}')
print(f'\t\tB2 = {Cardinality.resulting({ A.B : 1, A.A2 : 1, A.A3 : 0 }, data)}')
print(f'\t\tB3 = {Cardinality.resulting({ A.B : 2, A.A2 : 1, A.A3 : 0 }, data)}')
print(f'\t\tf = {Cardinality.joint({ A.A2 : 1, A.A3 : 0 }, data) / Cardinality.personal(A.A2, data)}')
print('\t\t#####')
print(f'\t\tI(B;A22,A31,A1) = {Entropy.Mutual._fuzzy({ A.B: None, A.A2 : 1, A.A3 : 0, A.A1: None}, data)} {max}')
print(f'\t\tI(B;A22,A31,A4) = {Entropy.Mutual._fuzzy({ A.B: None, A.A2 : 1, A.A3 : 0, A.A4: None}, data)}')
print(f'\t\tH(B|A22,A31,A1) = {Entropy.Conditional._fuzzy({ A.B : None, A.A2 : 1, A.A3 : 0, A.A1 : None }, data)} {min}')
print(f'\t\tH(B|A22,A31,A4) = {Entropy.Conditional._fuzzy({ A.B : None, A.A2 : 1, A.A3 : 0, A.A4 : None }, data)}')
print()

## najlepsie vyslo A1
#### pocitame vetvu A22 -> A31 -> A11
print('\t\t\tVetva: B -> A22 -> A31 -> A11------------------')
print(f'\t\t\tH(B|A22,A31,A11) = {Entropy.Conditional._fuzzy({ A.B : None, A.A2 : 1, A.A3 : 0, A.A1 : 0 }, data)}')
print(f'\t\t\tB1 = {Cardinality.resulting({ A.B : 0, A.A2 : 1, A.A3 : 0, A.A1 : 0 }, data)}')
print(f'\t\t\tB2 = {Cardinality.resulting({ A.B : 1, A.A2 : 1, A.A3 : 0, A.A1 : 0 }, data)}')
print(f'\t\t\tB3 = {Cardinality.resulting({ A.B : 2, A.A2 : 1, A.A3 : 0, A.A1 : 0 }, data)}')
print(f'\t\t\tf = {Cardinality.joint({ A.A2 : 1, A.A3 : 0, A.A1 : 0 }, data) / Cardinality.personal(A.A2, data)} {ltAlfa}')
#### xxx
print()

#### pocitame vetvu A22 -> A31 -> A12
print('\t\t\tVetva: B -> A22 -> A31 -> A12------------------')
print(f'\t\t\tH(B|A22,A31,A12) = {Entropy.Conditional._fuzzy({ A.B : None, A.A2 : 1, A.A3 : 0, A.A1 : 1 }, data)}')
print(f'\t\t\tB1 = {Cardinality.resulting({ A.B : 0, A.A2 : 1, A.A3 : 0, A.A1 : 1 }, data)}')
print(f'\t\t\tB2 = {Cardinality.resulting({ A.B : 1, A.A2 : 1, A.A3 : 0, A.A1 : 1 }, data)}')
print(f'\t\t\tB3 = {Cardinality.resulting({ A.B : 2, A.A2 : 1, A.A3 : 0, A.A1 : 1 }, data)}')
print(f'\t\t\tf = {Cardinality.joint({ A.A2 : 1, A.A3 : 0, A.A1 : 1 }, data) / Cardinality.personal(A.A2, data)} {ltAlfa}')
#### xxx
print()

#### pocitame vetvu A22 -> A32
print('\t\tVetva: B -> A22 -> A32------------------')
print(f'\t\tH(B|A22,A32) = {Entropy.Conditional._fuzzy({ A.B : None, A.A2 : 1, A.A3 : 1 }, data)}')
print(f'\t\tB1 = {Cardinality.resulting({ A.B : 0, A.A2 : 1, A.A3 : 1 }, data)}')
print(f'\t\tB2 = {Cardinality.resulting({ A.B : 1, A.A2 : 1, A.A3 : 1 }, data)}')
print(f'\t\tB3 = {Cardinality.resulting({ A.B : 2, A.A2 : 1, A.A3 : 1 }, data)}')
print(f'\t\tf = {Cardinality.joint({ A.A2 : 1, A.A3 : 1 }, data) / Cardinality.personal(A.A2, data)} {ltAlfa}')
#### xxx
print()










#### pocitame vetvu A23
print('\tVetva: B -> A23 ------------------')
print(f'\tH(B|A23) = {Entropy.Conditional.fuzzy(A.B, A.A2, data, 2)}')
print(f'\tH(B|A23). = {Entropy.Conditional._fuzzy({ A.B : None, A.A2 : 2 }, data)}')
print(f'\tB1 = {Cardinality.resulting({ A.B : 0, A.A2 : 2 }, data)}')
print(f'\tB2 = {Cardinality.resulting({ A.B : 1, A.A2 : 2 }, data)}')
print(f'\tB3 = {Cardinality.resulting({ A.B : 2, A.A2 : 2 }, data)}')
print(f'\tf = {Cardinality.joint({ A.A2 : 2 }, data) / Cardinality.personal(A.A2, data)}')
print('\t#####')
print(f'\tI(B;A23,A1) = {Entropy.Mutual._fuzzy({ A.B: None, A.A2 : 2, A.A1: None}, data)} {max}')
print(f'\tI(B;A23,A3) = {Entropy.Mutual._fuzzy({ A.B: None, A.A2 : 2, A.A3: None}, data)}')
print(f'\tI(B;A23,A4) = {Entropy.Mutual._fuzzy({ A.B: None, A.A2 : 2, A.A4: None}, data)}')
print(f'\tH(B|A23,A1) = {Entropy.Conditional._fuzzy({ A.B : None, A.A2 : 2, A.A1 : None }, data)} {min}')
print(f'\tH(B|A23,A3) = {Entropy.Conditional._fuzzy({ A.B : None, A.A2 : 2, A.A3 : None }, data)}')
print(f'\tH(B|A23,A4) = {Entropy.Conditional._fuzzy({ A.B : None, A.A2 : 2, A.A4 : None }, data)}')
print()

## najlepsie vyslo A1
#### pocitame vetvu A23 -> A11
print('\t\tVetva: B -> A23 -> A11------------------')
print(f'\t\tH(B|A23,A11) = {Entropy.Conditional._fuzzy({ A.B : None, A.A2 : 2, A.A1 : 0 }, data)}')
print(f'\t\tB1 = {Cardinality.resulting({ A.B : 0, A.A2 : 2, A.A1 : 0 }, data)}')
print(f'\t\tB2 = {Cardinality.resulting({ A.B : 1, A.A2 : 2, A.A1 : 0 }, data)}')
print(f'\t\tB3 = {Cardinality.resulting({ A.B : 2, A.A2 : 2, A.A1 : 0 }, data)}')
print(f'\t\tf = {Cardinality.joint({ A.A2 : 2, A.A1 : 0 }, data) / Cardinality.personal(A.A2, data)} {ltAlfa}')
#### xxx
print()




#### pocitame vetvu A23 -> A12
print('\t\tVetva: B -> A23 -> A12------------------')
print(f'\t\tH(B|A23,A12) = {Entropy.Conditional._fuzzy({ A.B : None, A.A2 : 2, A.A1 : 1 }, data)}')
print(f'\t\tB1 = {Cardinality.resulting({ A.B : 0, A.A2 : 2, A.A1 : 1 }, data)}')
print(f'\t\tB2 = {Cardinality.resulting({ A.B : 1, A.A2 : 2, A.A1 : 1 }, data)} {gtBeta}')
print(f'\t\tB3 = {Cardinality.resulting({ A.B : 2, A.A2 : 2, A.A1 : 1 }, data)}')
print(f'\t\tf = {Cardinality.joint({ A.A2 : 2, A.A1 : 1 }, data) / Cardinality.personal(A.A2, data)} {ltAlfa}')
#### xxx
print()