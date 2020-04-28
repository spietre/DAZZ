from enum import Enum
from Statistics import Statistics
from Statistics import Information
class Head(Enum):
    Tumor = 0
    History = 1
    Heredity = 2
    Age = 3
    Cancer = 4

data = [
    #Tumor            History          Heredity    Age         Cancer
    [[0.9, 0.1, 0.0], [1.0, 0.0, 0.0], [0.8, 0.2], [0.4, 0.6], [0.0, 0.8, 0.2]],
    [[0.8, 0.2, 0.0], [0.6, 0.4, 0.0], [0.0, 1.0], [0.0, 1.0], [0.6, 0.4, 0.0]],
    [[0.0, 0.7, 0.3], [0.8, 0.2, 0.0], [0.1, 0.9], [0.2, 0.8], [0.3, 0.6, 0.1]],
    [[0.2, 0.7, 0.1], [0.3, 0.7, 0.0], [0.2, 0.8], [0.3, 0.7], [0.9, 0.1, 0.0]],
    [[0.0, 0.1, 0.9], [0.7, 0.3, 0.0], [0.5, 0.5], [0.5, 0.5], [0.0, 0.0, 1.0]],
    [[0.0, 0.7, 0.3], [0.0, 0.3, 0.7], [0.7, 0.3], [0.4, 0.6], [0.2, 0.0, 0.8]],
    [[0.0, 0.3, 0.7], [0.0, 0.0, 1.0], [0.0, 1.0], [0.1, 0.9], [0.0, 0.0, 1.0]],
    [[0.0, 1.0, 0.0], [0.0, 0.2, 0.8], [0.2, 0.8], [0.0, 1.0], [0.7, 0.0, 0.3]],
    [[1.0, 0.0, 0.0], [1.0, 0.0, 0.0], [0.6, 0.4], [0.7, 0.3], [0.2, 0.8, 0.0]],
    [[0.9, 0.1, 0.0], [0.0, 0.3, 0.7], [0.0, 1.0], [0.9, 0.1], [0.0, 0.3, 0.7]],
    [[0.7, 0.3, 0.0], [1.0, 0.0, 0.0], [1.0, 0.0], [0.2, 0.8], [0.3, 0.7, 0.0]],
    [[0.2, 0.6, 0.2], [0.0, 1.0, 0.0], [0.3, 0.7], [0.3, 0.7], [0.7, 0.2, 0.1]],
    [[0.9, 0.1, 0.0], [0.2, 0.8, 0.0], [0.1, 0.9], [1.0, 0.0], [0.0, 0.0, 1.0]],
    [[0.0, 0.9, 0.1], [0.0, 0.9, 0.1], [0.1, 0.9], [0.7, 0.3], [0.0, 0.0, 1.0]],
    [[0.0, 0.0, 1.0], [0.0, 0.0, 1.0], [1.0, 0.0], [0.8, 0.2], [0.0, 0.0, 1.0]],
    [[1.0, 0.0, 0.0], [0.5, 0.5, 0.0], [0.0, 1.0], [0.0, 1.0], [0.5, 0.5, 0.0]]
]

sums = { i.value : dict() for i in Head }

for row in data:
    for col, col_list in enumerate(row):
        for cell, val in enumerate(col_list):
            try:
                sums[col][cell] += val
            except KeyError:
                try:
                    sums[col][cell] = val
                except KeyError:
                    sums[col] = dict()
                    sums[col][cell] = val
                    
print(sums)

print(Statistics.cardinality(data, Head))
print(Information.Personal.fuzzy(Head.History.value, 0, data, head=Head))
print(Information.Personal.fuzzy(Head.Cancer.value, 0, data, head=Head))
print(Information.Joint.fuzzy(Head.Cancer.value, 0, Head.History.value, 0, data, head=Head))
print(Information.Conditional.fuzzy(Head.Cancer.value, 0, Head.History.value, 0, data, head=Head))
print(Information.Mutual.fuzzy(Head.Cancer.value, 0, Head.History.value, 0, data, head=Head))