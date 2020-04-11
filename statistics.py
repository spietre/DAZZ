import math
import numpy

class Statistics:
    @staticmethod
    def covariance(X: list, Y: list):
        meanX = Statistics.mean(X)
        meanY = Statistics.mean(Y)
        
        return sum(
            [(X[i] - meanX) * (Y[i] - meanY) for i in range(len(X))] / (len(X) - 1)
        )
    
    @staticmethod
    def correlation(X: list, Y: list):
        return Statistics.covariance(X, Y) / Statistics.std_deviation(X) * Statistics.std_deviation(Y)
        
    @staticmethod
    def std_deviation(X: list):        
        mean = Statistics.mean(X)
        return math.sqrt(
            sum([(i - mean) ** 2 for i in X]) / (len(X) - 1)
        )
    
    @staticmethod
    def mean(X: list):
        return sum([i for i in X]) / len(X)

    # minimum of range, maximum of range
    # normalizes x_old at <0; 1> interval
    @staticmethod
    def normalize(x_old: float = None, x_min: float = None, x_max: float = None, X: list = None):
        # if one number is passed normalize it at <0; 1>
        if x_old is not None and x_max is not None and x_min is not None:
            x_new = (x_old - x_min) / (x_max - x_min)        
            return x_new
        
        # if whole list is passed, normalize all its numbers at <0; 1>
        if X is not None:
            x_min = min(X)
            x_max = max(X)
            
            for i in len(X):
                X[i] = (X[i] - x_min) / (x_max - x_min)
            return X
    
    # lower and upper are both inclusives <a, b>
    # normalizes x_old at <a; b> interval
    @staticmethod
    def normalize_at_ab(a: float, b: float, x_old: float = None, x_min: float = None, x_max: float = None, X: list = None):
        # if one number is passed normalize it at <a; b>
        if x_old is not None and x_max is not None and x_min is not None:
            return Statistics.normalize(x_old=x_old, x_min=x_min, x_max=x_max) * (b - a) + a

        # if whole list is passed, normalize all its numbers at <a; b>
        if X is not None:
            x_min = min(X)
            x_max = max(X)
            
            for i in len(X):
                X[i] = Statistics.normalize(x_old=X[i], x_min=x_min, x_max=x_max) * (b - a) + a
            return X