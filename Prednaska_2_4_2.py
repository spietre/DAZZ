# 2.4. Porovnávanie dát. Vyhľadávanie podobných objektov
# Pojem vzdialenosti [0; +∞]
# Vzdialenosť (x,y) = 1 – Podobnosť (x,y)
#            d(x,y) = 1 – s(x,y)
from tabulate import tabulate
from Statistics.Distance import Distance

# INPUT
teams = [[1,1],[2,1],[4,3],[4,5],[2,4]]

# OUTPUT
print("Euclidian distance")
print(tabulate([
    ['A', '-', Distance.euclid(teams[0],teams[1]), Distance.euclid(teams[0],teams[2]), Distance.euclid(teams[0],teams[3]), Distance.euclid(teams[0],teams[4])],
    ['B', '-', '-', Distance.euclid(teams[1],teams[2]), Distance.euclid(teams[1],teams[3]), Distance.euclid(teams[1],teams[4])],
    ['C', '-', '-', '-', Distance.euclid(teams[2],teams[3]), Distance.euclid(teams[2],teams[4])],
    ['D', '-', '-', '-', '-', Distance.euclid(teams[3],teams[4])],
    ['E', '-', '-', '-', '-', '-']
    ], headers=['A','B','C','D','E']))

print("Euclid ^ 2 distance")
print(tabulate([
    ['A', '-', Distance.euclid2(teams[0],teams[1]), Distance.euclid2(teams[0],teams[2]), Distance.euclid2(teams[0],teams[3]), Distance.euclid2(teams[0],teams[4])],
    ['B', '-', '-', Distance.euclid2(teams[1],teams[2]), Distance.euclid2(teams[1],teams[3]), Distance.euclid2(teams[1],teams[4])],
    ['C', '-', '-', '-', Distance.euclid2(teams[2],teams[3]), Distance.euclid2(teams[2],teams[4])],
    ['D', '-', '-', '-', '-', Distance.euclid2(teams[3],teams[4])],
    ['E', '-', '-', '-', '-', '-']
    ], headers=['A','B','C','D','E']))

print("Manhattanian distance")
print(tabulate([
    ['A', '-', Distance.manhattan(teams[0],teams[1]), Distance.manhattan(teams[0],teams[2]), Distance.manhattan(teams[0],teams[3]), Distance.manhattan(teams[0],teams[4])],
    ['B', '-', '-', Distance.manhattan(teams[1],teams[2]), Distance.manhattan(teams[1],teams[3]), Distance.manhattan(teams[1],teams[4])],
    ['C', '-', '-', '-', Distance.manhattan(teams[2],teams[3]), Distance.manhattan(teams[2],teams[4])],
    ['D', '-', '-', '-', '-', Distance.manhattan(teams[3],teams[4])],
    ['E', '-', '-', '-', '-', '-']
    ], headers=['A','B','C','D','E']))

print("Tchebyshev distance")
print(tabulate([
    ['A', '-', Distance.tchebyshev(teams[0],teams[1]), Distance.tchebyshev(teams[0],teams[2]), Distance.tchebyshev(teams[0],teams[3]), Distance.tchebyshev(teams[0],teams[4])],
    ['B', '-', '-', Distance.tchebyshev(teams[1],teams[2]), Distance.tchebyshev(teams[1],teams[3]), Distance.tchebyshev(teams[1],teams[4])],
    ['C', '-', '-', '-', Distance.tchebyshev(teams[2],teams[3]), Distance.tchebyshev(teams[2],teams[4])],
    ['D', '-', '-', '-', '-', Distance.tchebyshev(teams[3],teams[4])],
    ['E', '-', '-', '-', '-', '-']
    ], headers=['A','B','C','D','E']))

print("Minkowsky distance p=10")
print(tabulate([
    ['A', '-', Distance.minkowsky(teams[0],teams[1], 10), Distance.minkowsky(teams[0],teams[2], 10), Distance.minkowsky(teams[0],teams[3], 10), Distance.minkowsky(teams[0],teams[4], 10)],
    ['B', '-', '-', Distance.minkowsky(teams[1],teams[2], 10), Distance.minkowsky(teams[1],teams[3], 10), Distance.minkowsky(teams[1],teams[4], 10)],
    ['C', '-', '-', '-', Distance.minkowsky(teams[2],teams[3], 10), Distance.minkowsky(teams[2],teams[4], 10)],
    ['D', '-', '-', '-', '-', Distance.minkowsky(teams[3],teams[4], 10)],
    ['E', '-', '-', '-', '-', '-']
    ], headers=['A','B','C','D','E']))


print("Hamming distance for Karolin and Kathrin")
print(Distance.hamming(list("Karolin"), list("Kathrin")))

print("Hamming distance for Karolin and Kerstin")
print(Distance.hamming(list("Karolin"), list("Kerstin")))

print("Hamming distance for 1011101 and 1001001")
print(Distance.hamming(list("1011101"), list("1001001")))

print("Hamming distance for 2173896 and 2233796")
print(Distance.hamming(list("2173896"), list("2233796")))

print("Jaccard distance for x = { 0, 1, 2, 5, 6} and y = { 0, 2, 3, 5, 7, 9}")
x = { 0, 1, 2, 5, 6}
y = { 0, 2, 3, 5, 7, 9}
print(Distance.jaccard(x, y))
