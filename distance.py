import math
import numpy

class Distance:

    @staticmethod
    def euclid(A: list, B: list):
        return math.sqrt(   # and get square root of inner sum
            sum(  # sum all squared differences between items with same index
                [(A[i] - B[i]) ** 2 for i in range(len(A))]
            )
        )
    
    @staticmethod
    def euclid2(A: list, B: list):
        return sum( # sum all squared differences between items with same index
            [(A[i] - B[i]) ** 2 for i in range(len(A))]
        )
    
    @staticmethod
    def manhattan(A: list, B: list):
        return sum( # sum all absolut differences between items with same index
            [abs(A[i] - B[i]) for i in range(len(A))]
        )
    
    @staticmethod
    def tchebyshev(A: list, B: list):
        return max( # find max in absolute differences between items with same index
            [abs(A[i] - B[i]) for i in range(len(A))]
        )
    
    @staticmethod
    def minkowsky(A: list, B: list, p: int):
        if p < 0:
            raise AttributeError
        
        return math.pow(
            sum(
                [abs(A[i] - B[i]) ** p for i in range(len(A))]
            ), 1/p
        )
    
    @staticmethod
    def weighted():
        raise NotImplementedError
    
    @staticmethod
    def hamming(A: list, B: list):
        # returns number of differencies
        return sum([A[i] != B[i] for i in range(len(A))])
    
    @staticmethod
    def jaccard(A: set, B: set):
        return 1 - len(A.intersection(B)) / len(A.union(B))