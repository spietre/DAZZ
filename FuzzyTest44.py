from enum import Enum
from Statistics import Statistics
from Statistics import Information
from Statistics import Entropy
from Statistics import Cardinality

class A:
    A1 = 0
    A2 = 1
    A3 = 2
    A4 = 3
    B = 4

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

##### vypocitame vstupnu entropiu vystupneho atributu
print(f'H(B) = {Entropy.Personal.fuzzy(A.B, data)}')
print(f'B1 = {Cardinality.personal(A.B, data, 0) / Cardinality.personal(A.B, data)}')
print(f'B2 = {Cardinality.personal(A.B, data, 1) / Cardinality.personal(A.B, data)}')
print(f'B3 = {Cardinality.personal(A.B, data, 2) / Cardinality.personal(A.B, data)}')
print()

#####
print(f'I(B;A1)/cost(A1) = {Entropy.Mutual.fuzzy(A.B, A.A1, data)/1}')
print(f'I(B;A2)/cost(A2) = {Entropy.Mutual.fuzzy(A.B, A.A2, data)/1}')
print(f'I(B;A3)/cost(A3) = {Entropy.Mutual.fuzzy(A.B, A.A3, data)/1}')
print(f'I(B;A4)/cost(A4) = {Entropy.Mutual.fuzzy(A.B, A.A4, data)/1}')
print()

##### vyberieme minimum z tychto podmienenych entropii
print(f'H(B|A1) = {Entropy.Conditional.fuzzy(A.B, A.A1, data)}')
print(f'H(B|A2) = {Entropy.Conditional.fuzzy(A.B, A.A2, data)}')
print(f'H(B|A3) = {Entropy.Conditional.fuzzy(A.B, A.A3, data)}')
print(f'H(B|A4) = {Entropy.Conditional.fuzzy(A.B, A.A4, data)}')
print()

#### najlepsie vyslo A2 
#### pocitame vetvu A21
print(f'H(B|A21) = {Entropy.Conditional.fuzzy(A.B, A.A2, data, 0)}')
print(f'B1 = {Cardinality.joint(A.B, 0, A.A2, 0, data) / Cardinality.personal(A.A2, data, 0)}')
print(f'B2 = {Cardinality.joint(A.B, 1, A.A2, 0, data) / Cardinality.personal(A.A2, data, 0)}')
print(f'B3 = {Cardinality.joint(A.B, 2, A.A2, 0, data) / Cardinality.personal(A.A2, data, 0)}')
print(f'f = {Cardinality.personal(A.A2, data, 0) / Cardinality.personal(A.A2, data)}')
print()

#### pocitame vetvu A22
print(f'H(B|A22) = {Entropy.Conditional.fuzzy(A.B, A.A2, data, 1)}')
print(f'B1 = {Cardinality.joint(A.B, 0, A.A2, 1, data) / Cardinality.personal(A.A2, data, 1)}')
print(f'B2 = {Cardinality.joint(A.B, 1, A.A2, 1, data) / Cardinality.personal(A.A2, data, 1)}')
print(f'B3 = {Cardinality.joint(A.B, 2, A.A2, 1, data) / Cardinality.personal(A.A2, data, 1)}')
print(f'f = {Cardinality.personal(A.A2, data, 1) / Cardinality.personal(A.A2, data)}')
print()

#### pocitame vetvu A23
print(f'H(B|A23) = {Entropy.Conditional.fuzzy(A.B, A.A2, data, 2)}')
print(f'B1 = {Cardinality.joint(A.B, 0, A.A2, 2, data) / Cardinality.personal(A.A2, data, 2)}')
print(f'B2 = {Cardinality.joint(A.B, 1, A.A2, 2, data) / Cardinality.personal(A.A2, data, 2)}')
print(f'B3 = {Cardinality.joint(A.B, 2, A.A2, 2, data) / Cardinality.personal(A.A2, data, 2)}')
print(f'f = {Cardinality.personal(A.A2, data, 2) / Cardinality.personal(A.A2, data)}')
print()