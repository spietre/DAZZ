import math
import numpy

class Distance:

    @staticmethod
    def euclid(A: list, B: list):
        """
        sqrt( sum( [xi - yi] ^ 2 ) ) \n
        sum all squared differences between items with same index 
        and get square root of their sum
        """        
        return math.sqrt(
            sum((A[i] - B[i]) ** 2 for i in range(len(A)))
        )
    
    @staticmethod
    def euclid2(A: list, B: list):
        """
        sum( [xi - yi] ^ 2 ) \n
        sum all squared differences between items with same index
        """
        return sum((A[i] - B[i]) ** 2 for i in range(len(A)))
    
    @staticmethod
    def manhattan(A: list, B: list):
        """
        sum( |xi - yi| ) \n
        sum all absolut differences between items with same index
        """
        return sum(abs(A[i] - B[i]) for i in range(len(A)))
    
    @staticmethod
    def tchebyshev(A: list, B: list):
        """
        max( |xi - yi| ) \n
        find maximum of absolute differences between items with same index
        """
        return max(abs(A[i] - B[i]) for i in range(len(A)))
    
    @staticmethod
    def minkowsky(A: list, B: list, p: int):
        """
        p-root( sum( |xi - yi| ^ p ) ) where p > 0
        """
        if p < 0:
            raise AttributeError
        
        return math.pow(
            sum(abs(A[i] - B[i]) ** p for i in range(len(A))), 
            1/p
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