from enum import Enum
from Statistics import Statistics
from Statistics import Information
from Statistics import Entropy
from Statistics import Cardinality

class Atrs:
    Tumor = 0
    History = 1
    Heredity = 2
    Age = 3
    Cancer = 4
    Count = 5
    alfa = .16
    beta = .75
    
    
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

sums = { atr : dict() for atr in range(Atrs.Count) }

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
                    
# print(sums)

# print(Cardinality.complete(data, Atr))
# print(Information.Personal.fuzzy(Atrs.History, 0, data))
# print(Information.Personal.fuzzy(Atrs.Cancer, 0, data))
# print(Information.Joint.fuzzy(Atrs.Cancer, 0, Atrs.History, 0, data))
# print(Information.Conditional.fuzzy(Atrs.Cancer, 0, Atrs.History, 0, data))
# print(Information.Mutual.fuzzy(Atrs.Cancer, 0, Atrs.History, 0, data))

# print(Entropy.Personal.fuzzy(Atrs.History, data))
# print(Cardinality.cartesian(Atrs.Cancer, 0, Atrs.History, 0, data))
# print(Entropy.Joint.fuzzy(Atrs.Cancer, Atrs.History, data))
# print(Entropy.Conditional.fuzzy(Atrs.Cancer, Atrs.History, data, 0))
# print(Entropy.Conditional.fuzzy(Atrs.Cancer, Atrs.History, data))

##### vypocitame vstupnu entropiu vystupneho atributu
print(f'H(B): {Entropy.Personal.fuzzy(Atrs.Cancer, data)}') # H(B): 24.684391263804933
print(f'B1= {Cardinality.personal(Atrs.Cancer, data, 0) / Cardinality.personal(Atrs.Cancer, data) * 100}%') # B1= 27.499999999999996%
print(f'B2= {Cardinality.personal(Atrs.Cancer, data, 1) / Cardinality.personal(Atrs.Cancer, data) * 100}%') # B2= 27.500000000000004%
print(f'B3= {Cardinality.personal(Atrs.Cancer, data, 2) / Cardinality.personal(Atrs.Cancer, data) * 100}%') # B3= 44.99999999999999%
print()
##### frekvencia je zatial 1 pretoze sme v koreni
# print(Cardinality.joint(Atrs.History, 0, Atrs.Tumor, 0, data))
# print(Cardinality.joint(Atrs.Cancer, 0, Atrs.History, 0, data) / Cardinality.personal(Atrs.History, data, 0)) 

##### vyberieme minimum z tychto podmienenych entropii
print(f'H(B|A1)= {Entropy.Conditional._fuzzy({ Atrs.Cancer: None, Atrs.Tumor: None }, data)}') # H(B|A1)= 21.6323512405259
print(f'H(B|A2)= {Entropy.Conditional._fuzzy({ Atrs.Cancer: None, Atrs.History: None }, data)} <--- min') # H(B|A2)= 20.932545536332213
print(f'H(B|A3)= {Entropy.Conditional._fuzzy({ Atrs.Cancer: None, Atrs.Heredity: None }, data)}') # H(B|A3)= 24.427719369546534
print(f'H(B|A4)= {Entropy.Conditional._fuzzy({ Atrs.Cancer: None, Atrs.Age: None }, data)}') # H(B|A4)= 23.282907573986932
print()
print()




##### ta entropia ktora vysla najmensia cuze History teraz rozbijeme na vetvy 
##### VETVA A21
print('\tbranch: B -> A21')
print('\t----------------------------------------------------------------------')
print(f'\tH(B|A21)= {Entropy.Conditional._fuzzy({ Atrs.Cancer: None, Atrs.History: 0 }, data)}') # H(B|A21)= 8.820320028015262
print(f'\tB1 = {Cardinality.joint({ Atrs.Cancer : 0, Atrs.History : 0 }, data) / Cardinality.personal(Atrs.History, data, 0) * 100}%') # B1 = 26.557377049180324%
print(f'\tB2 = {Cardinality.joint({ Atrs.Cancer : 1, Atrs.History : 0 }, data) / Cardinality.personal(Atrs.History, data, 0) * 100}%') # B2 = 54.0983606557377%
print(f'\tB3 = {Cardinality.joint({ Atrs.Cancer : 2, Atrs.History : 0 }, data) / Cardinality.personal(Atrs.History, data, 0) * 100}%') # B3 = 19.344262295081965%
print(f'\tf = {Cardinality.joint({Atrs.History : 0}, data) / Cardinality.personal(Atrs.History, data)}') # f = 0.38125000000000003
print()

#### dalej vyberieme ten atribut ktoreho entropia je najnizsia
print(f'\tH(B|A21,A1)= {Entropy.Conditional._fuzzy({ Atrs.Cancer: None, Atrs.History: 0, Atrs.Tumor: None}, data)} <--- min') # H(B|A21,A1)= 7.652739733918309
print(f'\tH(B|A21,A3)= {Entropy.Conditional._fuzzy({ Atrs.Cancer: None, Atrs.History: 0, Atrs.Heredity: None}, data)}') # H(B|A21,A3)= 8.601022207502698
print(f'\tH(B|A21,A4)= {Entropy.Conditional._fuzzy({ Atrs.Cancer: None, Atrs.History: 0, Atrs.Age: None}, data)}') # H(B|A21,A4)= 8.560939352368301
### alebo informacia najvyssia
print(f'\tI(B;A21,A1)= {Entropy.Mutual._fuzzy({ Atrs.Cancer: None, Atrs.History: 0, Atrs.Tumor: None}, data)} <--- max') # I(B;A21,A1)= 1.167580294096953
print(f'\tI(B;A21,A3)= {Entropy.Mutual._fuzzy({ Atrs.Cancer: None, Atrs.History: 0, Atrs.Heredity: None}, data)}') # I(B;A21,A3)= 0.21929782051256375
print(f'\tI(B;A21,A4)= {Entropy.Mutual._fuzzy({ Atrs.Cancer: None, Atrs.History: 0, Atrs.Age: None}, data)}') # I(B;A21,A4)= 0.25938067564696077
print()

print('\t\tbranch: B -> A21 -> A11')
print('\t\t----------------------------------------------------------------------')
print(f'\t\tH(B|A21, A11)= {Entropy.Conditional._fuzzy({ Atrs.Cancer: None, Atrs.History: 0, Atrs.Tumor: 0 }, data)}') # H(B|A21, A11)= 4.72475650959
print(f'\t\tB1 = {Cardinality.resulting({ Atrs.Cancer: 0, Atrs.History: 0, Atrs.Tumor: 0 }, data) * 100}%') # B1 = 26.2303664921466%
print(f'\t\tB2 = {Cardinality.resulting({ Atrs.Cancer: 1, Atrs.History: 0, Atrs.Tumor: 0 }, data) * 100}%') # B2 = 64.3455497382199%
print(f'\t\tB3 = {Cardinality.resulting({ Atrs.Cancer: 2, Atrs.History: 0, Atrs.Tumor: 0 }, data) * 100}%') # B3 = 9.42408376963351%
print(f'\t\tf = {Cardinality.joint({ Atrs.History : 0, Atrs.Tumor: 0 }, data) / Cardinality.personal(Atrs.History, data)}') # f = 0.23875
print()

print(f'\t\tH(B|A21,A11,A3)= {Entropy.Conditional._fuzzy({ Atrs.Cancer: None, Atrs.History: 0, Atrs.Tumor: 0, Atrs.Heredity: None}, data)}') # H(B|A21,A11,A3)= 4.541534976741148
print(f'\t\tH(B|A21,A11,A4)= {Entropy.Conditional._fuzzy({ Atrs.Cancer: None, Atrs.History: 0, Atrs.Tumor: 0, Atrs.Age: None}, data)} <--- min') # H(B|A21,A11,A4)= 4.505771043721003
print(f'\t\tI(B;A21,A11,A3)= {Entropy.Mutual._fuzzy({ Atrs.Cancer: None, Atrs.History: 0, Atrs.Tumor: 0, Atrs.Heredity: None}, data)}') # I(B;A21,A11,A3)= 0.1832215328488518
print(f'\t\tI(B;A21,A11,A4)= {Entropy.Mutual._fuzzy({ Atrs.Cancer: None, Atrs.History: 0, Atrs.Tumor: 0, Atrs.Age: None}, data)} <--- max') # I(B;A21,A11,A4)= 0.2189854658689967
print()

print('\t\t\tbranch: B -> A21 -> A11 -> A41')
print('\t\t\t----------------------------------------------------------------------')
print(f'\t\t\tH(B|A21, A11)= {Entropy.Conditional._fuzzy({ Atrs.Cancer: None, Atrs.History: 0, Atrs.Tumor: 0, Atrs.Age: 0 }, data)}')
print(f'\t\t\tB1 = {Cardinality.resulting({ Atrs.Cancer: 0, Atrs.History: 0, Atrs.Tumor: 0, Atrs.Age: 0 }, data) * 100}%')
print(f'\t\t\tB2 = {Cardinality.resulting({ Atrs.Cancer: 1, Atrs.History: 0, Atrs.Tumor: 0, Atrs.Age: 0 }, data) * 100}%')
print(f'\t\t\tB3 = {Cardinality.resulting({ Atrs.Cancer: 2, Atrs.History: 0, Atrs.Tumor: 0, Atrs.Age: 0 }, data) * 100}%')
print(f'\t\t\tf = {Cardinality.joint({ Atrs.History : 0, Atrs.Tumor: 0, Atrs.Age: 0 }, data) / Cardinality.personal(Atrs.History, data)} < {Atrs.alfa} <--- uz dalej nejdeme')
print('\t\t\txxx')
print()

print('\t\t\tbranch: B -> A21 -> A11 -> A42')
print('\t\t\t----------------------------------------------------------------------')
print(f'\t\t\tH(B|A21, A11)= {Entropy.Conditional._fuzzy({ Atrs.Cancer: None, Atrs.History: 0, Atrs.Tumor: 0, Atrs.Age: 1 }, data)}')
print(f'\t\t\tB1 = {Cardinality.resulting({ Atrs.Cancer: 0, Atrs.History: 0, Atrs.Tumor: 0, Atrs.Age: 1 }, data) * 100}%')
print(f'\t\t\tB2 = {Cardinality.resulting({ Atrs.Cancer: 1, Atrs.History: 0, Atrs.Tumor: 0, Atrs.Age: 1 }, data) * 100}%')
print(f'\t\t\tB3 = {Cardinality.resulting({ Atrs.Cancer: 2, Atrs.History: 0, Atrs.Tumor: 0, Atrs.Age: 1 }, data) * 100}%')
print(f'\t\t\tf = {Cardinality.joint({ Atrs.History : 0, Atrs.Tumor: 0, Atrs.Age: 1 }, data) / Cardinality.personal(Atrs.History, data)} < {Atrs.alfa} <--- uz dalej nejdeme')
print('\t\t\txxx')
print()
print()

print('\t\tbranch: B -> A21 -> A12')
print('\t\t----------------------------------------------------------------------')
print(f'\t\tH(B|A21, A12)= {Entropy.Conditional._fuzzy({ Atrs.Cancer: None, Atrs.History: 0, Atrs.Tumor: 1 }, data)}') # H(B|A21, A12)= 1.9271963161875494
print(f'\t\tB1 = {Cardinality.resulting({ Atrs.Cancer: 0, Atrs.History: 0, Atrs.Tumor: 1 }, data) * 100}%') # B1 = 37.60869565217392%
print(f'\t\tB2 = {Cardinality.resulting({ Atrs.Cancer: 1, Atrs.History: 0, Atrs.Tumor: 1 }, data) * 100}%') # B2 = 50.36231884057971%
print(f'\t\tB3 = {Cardinality.resulting({ Atrs.Cancer: 2, Atrs.History: 0, Atrs.Tumor: 1 }, data) * 100}%') # B3 = 12.02898550724638%
print(f'\t\tf = {Cardinality.joint({ Atrs.History: 0, Atrs.Tumor: 1 }, data) / Cardinality.personal(Atrs.History, data)} < {Atrs.alfa} <--- uz dalej nejdeme') # f = 0.08625
print('\t\txxx')
print()

print('\t\tbranch: B -> A21 -> A13')
print('\t\t----------------------------------------------------------------------')
print(f'\t\tH(B|A21, A13)= {Entropy.Conditional._fuzzy({ Atrs.Cancer: None, Atrs.History: 0, Atrs.Tumor: 2 }, data)}') # H(B|A21, A13)= 1.0007869081407605
print(f'\t\tB1 = {Cardinality.resulting({ Atrs.Cancer: 0, Atrs.History: 0, Atrs.Tumor: 2 }, data) * 100}%') # B1 = 11.0%
print(f'\t\tB2 = {Cardinality.resulting({ Atrs.Cancer: 1, Atrs.History: 0, Atrs.Tumor: 2 }, data) * 100}%') # B2 = 16.333333333333332%
print(f'\t\tB3 = {Cardinality.resulting({ Atrs.Cancer: 2, Atrs.History: 0, Atrs.Tumor: 2 }, data) * 100}%') # B3 = 72.66666666666667%
print(f'\t\tf = {Cardinality.joint({ Atrs.History: 0, Atrs.Tumor: 2 }, data) / Cardinality.personal(Atrs.History, data)} < {Atrs.alfa} <--- uz dalej nejdeme') # f = 0.05625
print('\t\txxx')
print()

print()
print()
print()



##### VETVA A22
print('\tbranch: B -> A22')
print('\t----------------------------------------------------------------------')
print(f'\tH(B|A22)= {Entropy.Conditional._fuzzy({ Atrs.Cancer: None, Atrs.History: 1}, data)}') # H(B|A22)= 8.201310585759494
print(f'\tB1 = {Cardinality.resulting({ Atrs.Cancer : 0, Atrs.History : 1 }, data) * 100}%') # B1 = 37.14285714285714%
print(f'\tB2 = {Cardinality.resulting({ Atrs.Cancer : 1, Atrs.History : 1 }, data) * 100}%') # B2 = 15.892857142857144%
print(f'\tB3 = {Cardinality.resulting({ Atrs.Cancer : 2, Atrs.History : 1 }, data) * 100}%') # B3 = 46.96428571428571%
print(f'\tf = {Cardinality.joint({Atrs.History : 1}, data) / Cardinality.personal(Atrs.History, data)}') # f = 0.35000000000000003
print()

print(f'\tH(B|A22,A1)= {Entropy.Conditional._fuzzy({ Atrs.Cancer: None, Atrs.History: 1, Atrs.Tumor : None}, data)}') # H(B|A22,A1)= 8.055675659587857
print(f'\tH(B|A22,A3)= {Entropy.Conditional._fuzzy({ Atrs.Cancer: None, Atrs.History: 1, Atrs.Heredity : None}, data)}') # H(B|A22,A3)= 8.157170811492158
print(f'\tH(B|A22,A4)= {Entropy.Conditional._fuzzy({ Atrs.Cancer: None, Atrs.History: 1, Atrs.Age : None}, data)} <--- min') # H(B|A22,A4)= 7.081243709953053
print(f'\tI(B;A22,A1)= {Entropy.Mutual._fuzzy({ Atrs.Cancer: None, Atrs.History: 1, Atrs.Tumor: None}, data)}') # I(B;A22,A1)= 0.14563492617163654
print(f'\tI(B;A22,A3)= {Entropy.Mutual._fuzzy({ Atrs.Cancer: None, Atrs.History: 1, Atrs.Heredity: None}, data)}') # I(B;A22,A3)= 0.04413977426733595
print(f'\tI(B;A22,A4)= {Entropy.Mutual._fuzzy({ Atrs.Cancer: None, Atrs.History: 1, Atrs.Age: None}, data)} <--- max') # I(B;A22,A4)= 1.1200668758064403
print()

print('\t\tbranch: B -> A22 -> A41')
print('\t\t----------------------------------------------------------------------')
print(f'\t\tH(B|A22, A41)= {Entropy.Conditional._fuzzy({ Atrs.Cancer: None, Atrs.History: 1, Atrs.Age: 0 }, data)}') # H(B|A22, A41)= 2.5769465884057525
print(f'\t\tB1 = {Cardinality.resulting({ Atrs.Cancer: 0, Atrs.History: 1, Atrs.Age: 0 }, data) * 100}%') # B1 = 17.261904761904763%
print(f'\t\tB2 = {Cardinality.resulting({ Atrs.Cancer: 1, Atrs.History: 1, Atrs.Age: 0 }, data) * 100}%') # B2 = 7.380952380952381%
print(f'\t\tB3 = {Cardinality.resulting({ Atrs.Cancer: 2, Atrs.History: 1, Atrs.Age: 0 }, data) * 100}%') # B3 = 75.35714285714286%
print(f'\t\tf = {Cardinality.joint({ Atrs.History: 1, Atrs.Age: 0 }, data) / Cardinality.personal(Atrs.History, data)} < {Atrs.alfa} <--- uz dalej nejdeme') # f = 0.1575
print('\t\txxx')
print()

print('\t\tbranch: B -> A22 -> A42')
print('\t\t----------------------------------------------------------------------')
print(f'\t\tH(B|A22, A42)= {Entropy.Conditional._fuzzy({ Atrs.Cancer: None, Atrs.History: 1, Atrs.Age: 1 }, data)}') # H(B|A22, A42)= 4.5042971215473
print(f'\t\tB1 = {Cardinality.resulting({ Atrs.Cancer: 0, Atrs.History: 1, Atrs.Age: 1 }, data) * 100}%') # B1 = 53.40909090909091%
print(f'\t\tB2 = {Cardinality.resulting({ Atrs.Cancer: 1, Atrs.History: 1, Atrs.Age: 1 }, data) * 100}%') # B2 = 22.857142857142858%
print(f'\t\tB3 = {Cardinality.resulting({ Atrs.Cancer: 2, Atrs.History: 1, Atrs.Age: 1 }, data) * 100}%') # B3 = 23.73376623376624%
print(f'\t\tf = {Cardinality.joint({ Atrs.History: 1, Atrs.Age: 1 }, data) / Cardinality.personal(Atrs.History, data)}') # f = 0.19249999999999998
print()

print(f'\t\tH(B|A22,A42,A1)= {Entropy.Conditional._fuzzy({ Atrs.Cancer: None, Atrs.History: 1, Atrs.Age: 1, Atrs.Tumor : None}, data)} <--- min') # H(B|A22,A42,A1)= 4.034641092862546
print(f'\t\tH(B|A22,A42,A3)= {Entropy.Conditional._fuzzy({ Atrs.Cancer: None, Atrs.History: 1, Atrs.Age: 1, Atrs.Heredity : None}, data)}') # H(B|A22,A42,A3)= 4.40748413555121
print(f'\t\tI(B;A22,A42,A1)= {Entropy.Mutual._fuzzy({ Atrs.Cancer: None, Atrs.History: 1, Atrs.Age: 1, Atrs.Tumor: None}, data)} <--- max') # I(B;A22,A42,A1)= 0.46965602868475465
print(f'\t\tI(B;A22,A42,A3)= {Entropy.Mutual._fuzzy({ Atrs.Cancer: None, Atrs.History: 1, Atrs.Age: 1, Atrs.Heredity: None}, data)}') # I(B;A22,A42,A3)= 0.09681298599609
print()

print('\t\t\tbranch: B -> A22 -> A42 -> A11')
print('\t\t\t----------------------------------------------------------------------')
print(f'\t\t\tH(B|A22, A42)= {Entropy.Conditional._fuzzy({ Atrs.Cancer: None, Atrs.History: 1, Atrs.Age: 1, Atrs.Tumor: 0 }, data)}') # H(B|A22, A42)= 1.2359679867187277
print(f'\t\t\tB1 = {Cardinality.resulting({ Atrs.Cancer: 0, Atrs.History: 1, Atrs.Age: 1, Atrs.Tumor: 0 }, data) * 100}%') # B1 = 57.89861751152073%
print(f'\t\t\tB2 = {Cardinality.resulting({ Atrs.Cancer: 1, Atrs.History: 1, Atrs.Age: 1, Atrs.Tumor: 0 }, data) * 100}%') # B2 = 39.06912442396314%
print(f'\t\t\tB3 = {Cardinality.resulting({ Atrs.Cancer: 2, Atrs.History: 1, Atrs.Age: 1, Atrs.Tumor: 0 }, data) * 100}%') # B3 = 3.032258064516129%
print(f'\t\t\tf = {Cardinality.joint({ Atrs.History: 1, Atrs.Age: 1, Atrs.Tumor: 0 }, data) / Cardinality.personal(Atrs.History, data)} < {Atrs.alfa} <--- uz dalej nejdeme') # f = 0.0678125
print('\t\t\txxx')
print()

print('\t\t\tbranch: B -> A22 -> A42 -> A12')
print('\t\t\t----------------------------------------------------------------------')
print(f'\t\t\tH(B|A22, A42)= {Entropy.Conditional._fuzzy({ Atrs.Cancer: None, Atrs.History: 1, Atrs.Age: 1, Atrs.Tumor: 1 }, data)}') # H(B|A22, A42)= 2.153204326753506
print(f'\t\t\tB1 = {Cardinality.resulting({ Atrs.Cancer: 0, Atrs.History: 1, Atrs.Age: 1, Atrs.Tumor: 1 }, data) * 100}%') # B1 = 55.09079118028532%
print(f'\t\t\tB2 = {Cardinality.resulting({ Atrs.Cancer: 1, Atrs.History: 1, Atrs.Age: 1, Atrs.Tumor: 1 }, data) * 100}%') # B2 = 14.163424124513618%
print(f'\t\t\tB3 = {Cardinality.resulting({ Atrs.Cancer: 2, Atrs.History: 1, Atrs.Age: 1, Atrs.Tumor: 1 }, data) * 100}%') # B3 = 30.745784695201035%
print(f'\t\t\tf = {Cardinality.joint({ Atrs.History: 1, Atrs.Age: 1, Atrs.Tumor: 1 }, data) / Cardinality.personal(Atrs.History, data)} < {Atrs.alfa} <--- uz dalej nejdeme') # f = 0.096375
print('\t\t\txxx')
print()

print('\t\t\tbranch: B -> A22 -> A42 -> A13')
print('\t\t\t----------------------------------------------------------------------')
print(f'\t\t\tH(B|A22, A42)= {Entropy.Conditional._fuzzy({ Atrs.Cancer: None, Atrs.History: 1, Atrs.Age: 1, Atrs.Tumor: 2 }, data)}') # H(B|A22, A42)= 0.645468779390312
print(f'\t\t\tB1 = {Cardinality.resulting({ Atrs.Cancer: 0, Atrs.History: 1, Atrs.Age: 1, Atrs.Tumor: 2 }, data) * 100}%') # B1 = 36.93156732891832%
print(f'\t\t\tB2 = {Cardinality.resulting({ Atrs.Cancer: 1, Atrs.History: 1, Atrs.Age: 1, Atrs.Tumor: 2 }, data) * 100}%') # B2 = 13.620309050772624%
print(f'\t\t\tB3 = {Cardinality.resulting({ Atrs.Cancer: 2, Atrs.History: 1, Atrs.Age: 1, Atrs.Tumor: 2 }, data) * 100}%') # B3 = 49.44812362030904%
print(f'\t\t\tf = {Cardinality.joint({ Atrs.History: 1, Atrs.Age: 1, Atrs.Tumor: 2 }, data) / Cardinality.personal(Atrs.History, data)} < {Atrs.alfa} <--- uz dalej nejdeme') # f = 0.028312500000000004
print('\t\t\txxx')
print()
print()



##### VETVA A23
print('\tbranch: B -> A23')
print('\t----------------------------------------------------------------------')
print(f'\tH(B|A23)= {Entropy.Conditional._fuzzy({ Atrs.Cancer: None, Atrs.History: 2}, data)}') # H(B|A23)= 3.910914922557456
print(f'\tB1 = {Cardinality.joint({ Atrs.Cancer : 0, Atrs.History : 2 }, data) / Cardinality.personal(Atrs.History, data, 2) * 100}%') # B1 = 16.279069767441857%
print(f'\tB2 = {Cardinality.joint({ Atrs.Cancer : 1, Atrs.History : 2 }, data) / Cardinality.personal(Atrs.History, data, 2) * 100}%') # B2 = 4.883720930232557%
print(f'\tB3 = {Cardinality.joint({ Atrs.Cancer : 2, Atrs.History : 2 }, data) / Cardinality.personal(Atrs.History, data, 2) * 100}% > {Atrs.beta * 100}% <--- uz dalej nejdeme') # B3 = 78.83720930232558%
print(f'\tf = {Cardinality.joint({Atrs.History : 2}, data) / Cardinality.personal(Atrs.History, data)}') # f = 0.26875000000000004
print('\txxx')
print()

