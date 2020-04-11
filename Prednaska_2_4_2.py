# 2.4. Porovnávanie dát. Vyhľadávanie podobných objektov
# Pojem vzdialenosti [0; +∞]
# Vzdialenosť (x,y) = 1 – Podobnosť (x,y)
#            d(x,y) = 1 – s(x,y)
from tabulate import tabulate
import math
import numpy

class Distance:
        
    @staticmethod
    def Euclid(A: list, B: list):
        return math.sqrt(   # and get square root of inner sum
            sum(  # sum all squared differences between items with same index
                [(A[i] - B[i]) ** 2 for i in range(len(A))]
            )
        )
    
    @staticmethod
    def Euclid2(A: list, B: list):
        return sum( # sum all squared differences between items with same index
            [(A[i] - B[i]) ** 2 for i in range(len(A))]
        )
    
    @staticmethod
    def Manhattan(A: list, B: list):
        return sum( # sum all absolut differences between items with same index
            [abs(A[i] - B[i]) for i in range(len(A))]
        )
    
    @staticmethod
    def Tchebyshev(A: list, B: list):
        return max( # find max in absolute differences between items with same index
            [abs(A[i] - B[i]) for i in range(len(A))]
        )
    
    @staticmethod
    def Minkowsky(A: list, B: list, p: int):
        if p < 0:
            raise AttributeError
        
        return math.pow(
            sum(
                [abs(A[i] - B[i]) ** p for i in range(len(A))]
            ), 1/p
        )
    
    @staticmethod
    def Weighted():
        raise NotImplementedError
    
    @staticmethod
    def Hamming(A: list, B: list):
        # returns number of differencies
        return sum([A[i] != B[i] for i in range(len(A))])
    
    @staticmethod
    def Jaccard(A: set, B: set):
        return 1 - len(A.intersection(B)) / len(A.union(B))

# INPUT
teams = [[1,1],[2,1],[4,3],[4,5],[2,4]]

# OUTPUT
print("Euclidian distance")
print(tabulate([
    ['A', '-', Distance.Euclid(teams[0],teams[1]), Distance.Euclid(teams[0],teams[2]), Distance.Euclid(teams[0],teams[3]), Distance.Euclid(teams[0],teams[4])],
    ['B', '-', '-', Distance.Euclid(teams[1],teams[2]), Distance.Euclid(teams[1],teams[3]), Distance.Euclid(teams[1],teams[4])],
    ['C', '-', '-', '-', Distance.Euclid(teams[2],teams[3]), Distance.Euclid(teams[2],teams[4])],
    ['D', '-', '-', '-', '-', Distance.Euclid(teams[3],teams[4])],
    ['E', '-', '-', '-', '-', '-']
    ], headers=['A','B','C','D','E']))

print("Euclid ^ 2 distance")
print(tabulate([
    ['A', '-', Distance.Euclid2(teams[0],teams[1]), Distance.Euclid2(teams[0],teams[2]), Distance.Euclid2(teams[0],teams[3]), Distance.Euclid2(teams[0],teams[4])],
    ['B', '-', '-', Distance.Euclid2(teams[1],teams[2]), Distance.Euclid2(teams[1],teams[3]), Distance.Euclid2(teams[1],teams[4])],
    ['C', '-', '-', '-', Distance.Euclid2(teams[2],teams[3]), Distance.Euclid2(teams[2],teams[4])],
    ['D', '-', '-', '-', '-', Distance.Euclid2(teams[3],teams[4])],
    ['E', '-', '-', '-', '-', '-']
    ], headers=['A','B','C','D','E']))

print("Manhattanian distance")
print(tabulate([
    ['A', '-', Distance.Manhattan(teams[0],teams[1]), Distance.Manhattan(teams[0],teams[2]), Distance.Manhattan(teams[0],teams[3]), Distance.Manhattan(teams[0],teams[4])],
    ['B', '-', '-', Distance.Manhattan(teams[1],teams[2]), Distance.Manhattan(teams[1],teams[3]), Distance.Manhattan(teams[1],teams[4])],
    ['C', '-', '-', '-', Distance.Manhattan(teams[2],teams[3]), Distance.Manhattan(teams[2],teams[4])],
    ['D', '-', '-', '-', '-', Distance.Manhattan(teams[3],teams[4])],
    ['E', '-', '-', '-', '-', '-']
    ], headers=['A','B','C','D','E']))

print("Tchebyshev distance")
print(tabulate([
    ['A', '-', Distance.Tchebyshev(teams[0],teams[1]), Distance.Tchebyshev(teams[0],teams[2]), Distance.Tchebyshev(teams[0],teams[3]), Distance.Tchebyshev(teams[0],teams[4])],
    ['B', '-', '-', Distance.Tchebyshev(teams[1],teams[2]), Distance.Tchebyshev(teams[1],teams[3]), Distance.Tchebyshev(teams[1],teams[4])],
    ['C', '-', '-', '-', Distance.Tchebyshev(teams[2],teams[3]), Distance.Tchebyshev(teams[2],teams[4])],
    ['D', '-', '-', '-', '-', Distance.Tchebyshev(teams[3],teams[4])],
    ['E', '-', '-', '-', '-', '-']
    ], headers=['A','B','C','D','E']))

print("Minkowsky distance p=10")
print(tabulate([
    ['A', '-', Distance.Minkowsky(teams[0],teams[1], 10), Distance.Minkowsky(teams[0],teams[2], 10), Distance.Minkowsky(teams[0],teams[3], 10), Distance.Minkowsky(teams[0],teams[4], 10)],
    ['B', '-', '-', Distance.Minkowsky(teams[1],teams[2], 10), Distance.Minkowsky(teams[1],teams[3], 10), Distance.Minkowsky(teams[1],teams[4], 10)],
    ['C', '-', '-', '-', Distance.Minkowsky(teams[2],teams[3], 10), Distance.Minkowsky(teams[2],teams[4], 10)],
    ['D', '-', '-', '-', '-', Distance.Minkowsky(teams[3],teams[4], 10)],
    ['E', '-', '-', '-', '-', '-']
    ], headers=['A','B','C','D','E']))


print("Hamming distance for Karolin and Kathrin")
print(Distance.Hamming(list("Karolin"), list("Kathrin")))

print("Hamming distance for Karolin and Kerstin")
print(Distance.Hamming(list("Karolin"), list("Kerstin")))

print("Hamming distance for 1011101 and 1001001")
print(Distance.Hamming(list("1011101"), list("1001001")))

print("Hamming distance for 2173896 and 2233796")
print(Distance.Hamming(list("2173896"), list("2233796")))

print("Jaccard distance for x = { 0, 1, 2, 5, 6} and y = { 0, 2, 3, 5, 7, 9}")
x = { 0, 1, 2, 5, 6}
y = { 0, 2, 3, 5, 7, 9}
print(Distance.Jaccard(x, y))