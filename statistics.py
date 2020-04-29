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

    @staticmethod
    def normalize(x_old: float = None, x_min: float = None, x_max: float = None, X: list = None):
        """
        minimum of range, maximum of range
        normalizes x_old at <0; 1> interval
        """
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
    
    @staticmethod
    def normalize_at_ab(a: float, b: float, x_old: float = None, x_min: float = None, x_max: float = None, X: list = None):
        """ 
        lower and upper are both inclusives <a, b>
        normalizes x_old at <a; b> interval
        """
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
    
class Cardinality:
    @staticmethod
    def complete(rows: list, head):
        sums_row = { i.value : dict() for i in head }
        
        for row in rows:
            for col, col_list in enumerate(row):
                for cell, val in enumerate(col_list):
                    try:
                        sums_row[col][cell] += val
                    except KeyError:
                        try:
                            sums_row[col][cell] = val
                        except KeyError:
                            sums_row[col] = dict()
                            sums_row[col][cell] = val
        return sums_row

    @staticmethod
    def personal(A, rows: list, key_A = None):            
        ret_sum = .0
        for row in rows:
            # for col in row[A]:
            if key_A is not None:
                ret_sum += row[A][key_A]
            else:
                ret_sum += sum([val for val in row[A]])
        
        return ret_sum

    @staticmethod
    def cartesian(A, key_A, B, key_B, rows: list):
        return sum([row[A][key_A] * row[B][key_B] for row in rows])

class Probability:
    @staticmethod        
    def of(A = None, key = None, rows = None, M = None, N = None):
        """ Calculates probability of an 'A' being inside 'rows' list. """
        result = .0
        if rows is None or A is None or key is None:
            result = M / N
        else:
            result = sum([row[key] == A for row in rows]) / len(rows)
        
        return result
    
    @staticmethod
    def personal(A = None, key = None, rows = None, M = None, N = None):
        """ Calculates same thing as 'of' method. """
        return Probability.of(A, key, rows)
    
    @staticmethod
    def conjoint(A, B, key_A, key_B, rows):
        """
        Calculates probability of 'A' and 'B' being inside 'rows' stored at indices 'key_A' and 'key_B'.
        P(A,B) = P(A and B) 
        OR
        P(A,B) = P(A x B)
        """
        return sum([A == row[key_A] and B == row[key_B] for row in rows]) / len(rows)
        
    @staticmethod
    def conditional(A, B, key_A, key_B, rows):
        """ 
        Calculates conditional probablity of 'A' if we consider 'B' have already happend. 
        P(A|B) = P(A,B) / P(B)
        """
        return Probability.conjoint(A, B, key_A, key_B, rows) / Probability.personal(B, key_B, rows)
    
    
class Information:    
    @staticmethod
    def of(A = None, key_A = None, rows = None, probability: float = None):
        """ 
        Calculates how much infromation does 'A' provides. 
        I(A) = -log2( P(A) )
        """
        if probability is None:
            probability = Probability.of(A, key_A, rows)
        
        return -math.log2(probability) if probability > 0 else 0
    
    class Personal:
        @staticmethod
        def regular(A = None, key_A = None, rows = None, probability: float = None):
            """ 
            Calculates same thing as 'of' method. The personal information of 'A' describes uncertainty of this value. 
            I(A) = -log2( P(A) )
            """
            return Information.of(A=A, key_A=key_A, rows=rows, probability=probability)
        
        @staticmethod
        def fuzzy(A, key_A, rows: list, head = None, n = None):
            if n is None:
                if head is None:
                    raise AttributeError
                sums = Cardinality.complete(rows, head)
                n = sum([i for i in sums[A].values()])
            
            # return math.log2(n) - math.log2(sum([row[A][key_A] for row in rows]))
            return math.log2(n) - math.log2(Cardinality.personal(A, rows, key_A))
    
    class Joint:
        @staticmethod
        def regular(A = None, B = None, rows = None, key_A = None, key_B = None, probability: float = None):
            """ 
            Conjoint information of 'A' and 'B' describes common uncertainty of these two values. 
            I(A,B) = -log2( P(A,B) )
            """
            if probability is None:
                probability = Probability.conjoint(A, B, key_A, key_B, rows)
            
            return -math.log2(probability) if probability > 0 else 0
    
        @staticmethod
        def fuzzy(A, key_A, B, key_B, rows: list, head = None, n = None):
            if n is None:
                if head is None:
                    raise AttributeError
                sums = Cardinality.complete(rows, head)
                n = sum([i for i in sums[A].values()])
            
            # return math.log2(n) - math.log2(sum([row[A][key_A] * row[B][key_B] for row in rows]))
            return math.log2(n) - math.log2(Cardinality.cartesian(A, key_A, B, key_B, rows))
        
    class Conditional:
        @staticmethod
        def regular(A, B, key_A, key_B, rows):
            """ 
            Calculates and describes uncertainty of 'A' value if 'B' value is considered to be known.
            I(A|B) = I(A,B) - I(B)
            """
            return Information.Joint.regular(A, B, key_A, key_B, rows) - Information.Personal.regular(A)

        @staticmethod
        def fuzzy(A, key_A, B, key_B, rows: list, head = None, n = None):
            if n is None:
                if head is None:
                    raise AttributeError
                # sums = Cardinality.complete(rows, head)
                # n = sum([i for i in sums[A].values()])
                n = Cardinality.personal(A, rows)
            
            return Information.Joint.fuzzy(B, key_B, A, key_A, rows, n=n) - Information.Personal.fuzzy(B, key_B, rows, n=n)
    
    class Mutual:
        @staticmethod
        def regular(A, B, key_A, key_B, rows):
            """ Calculates information between 'A' and 'B' and describes dependency of 'A' on value of 'B' and vice versa. 
            I(A;B) = I(A) - I(A|B) 
            OR
            I(A;B) = I(A) + I(B) - I(A,B) """
            var1 = Information.Personal.regular(A, key_A, rows) - Information.Conditional.regular(B, A, key_B, key_A, rows)
            var2 = Information.Personal.regular(A, key_A, rows) + Information.Personal.regular(B, key_B, rows) - Information.Joint.regular(A, B, key_A, key_B, rows)
            
            if (var1 != var2):
                raise AssertionError
            
            return var1   
        
        @staticmethod
        def fuzzy(A, key_A, B, key_B, rows: list, head = None, n = None):
            if n is None:
                if head is None:
                    raise AttributeError
                # sums = Cardinality.complete(rows, head)
                # n = sum([i for i in sums[A].values()])
                n = Cardinality.personal(A, rows)
            
            return Information.Personal.fuzzy(A, key_A, rows, n=n) - Information.Conditional.fuzzy(A, key_A, B, key_B, rows, n=n)
            
    
class Entropy:
    @staticmethod
    def of(key_A, rows, val_A = None):
        """ H(A) = Sum( P(A) * I(A) ) """
        values = dict()
        length = len(rows)
        
        # compute occurences of each attribute value
        for row in rows:
            try:
                values[row[key_A]] += 1
            except KeyError:
                values[row[key_A]] = 1            
            
        if val_A is None:
            entropy = sum([Entropy.Personal.regular_helper(val, length) for key, val in values.items()])
        else:
            entropy = sum([Entropy.Personal.regular_helper(val, length) if val_A == key else 0 for key, val in values.items()])
            
        return entropy
    
    class Personal:
        @staticmethod
        def regular(key_A, rows, val_A = None):
            """ H(A) = Sum{ P(A) * I(A) } """
            return Entropy.of(key_A, rows, val_A)
        
        @staticmethod
        def regular_helper(M, N):
            prob = Probability.of(M=M, N=N)
            
            return prob * Information.of(probability = prob)
        
        @staticmethod
        def fuzzy(A, rows: list, head):
            sums_row = Cardinality.complete(rows, head)
            ret_val = .0
            
            for key, val in sums_row[A].items():
                ret_val += val * Information.Personal.fuzzy(A, key, rows, head=head)
            
            return ret_val    

    class Joint:                    
        @staticmethod
        def regular(key_A, key_B, rows, val_A = None, val_B = None):
            """ H(A,B) = Sum{ Sum[ P(A,B) * I(A,B) ] } """
            values = dict() #{ key_A : { key_B : dict() } }
            length = len(rows)
            
            for row in rows:
                try:
                    values[row[key_A]][row[key_B]] += 1
                except KeyError:
                    try:
                        values[row[key_A]][row[key_B]] = 1
                    except KeyError:
                        values[row[key_A]] = dict()
                        values[row[key_A]][row[key_B]] = 1

            tmp_sum = .0
            
            for a_key, dict_of_b in values.items():
                if val_A is None or val_A == a_key:
                    for b_key, occurrence in dict_of_b.items():
                        if val_B is None or val_B == b_key:
                            prob = Probability.of(M = occurrence, N = length)
                            tmp_sum += prob * Information.of(probability = prob)
                
            return tmp_sum

        @staticmethod
        def fuzzy(A, key_A, B, key_B, rows: list, head = None, n = None):
           for row in rows:
               ret_sum += Cardinality.cartesian(A, key_A, B, key_B, rows) * Information.Joint.fuzzy(A, key_A, B, key_B, rows, head, n)
        
    @staticmethod
    def conditional(key_A, key_B, rows, val_A = None, val_B = None):
        """ 
        H(A|B) = H(A,B) – H(B) 
        OR
        H(A|B) = Sum{ Sum[ P(A,B) * I(A|B) ] }
        """
        return Entropy.Joint.regular(key_A, key_B, rows, val_A, val_B) - Entropy.Personal.regular(key_B, rows, val_B)
    
    @staticmethod
    def mutual(key_A, key_B, rows, val_A = None, val_B = None):
        """ 
        Stredné množstvo informácie o atribútu A v atribúte B
        I(A;B) = H(A) + H(B) - H(A,B) 
        OR
        I(A;B) = H(A) - H(A|B) 
        OR
        I(A;B) = Sum{ Sum[ P(A,B) * I(A;B) ] }
        """
        return Entropy.Personal.regular(key_A, rows, val_A) + Entropy.Personal.regular(key_B, rows, val_B) - Entropy.Joint.regular(key_A, key_B, rows, val_A, val_B)
    
    @staticmethod
    def stability(key_A, key_B, rows, val_A = None, val_B = None):
        """
        Coefficient of atribute connection stability, it determines which atribute contributes 
        
        """
        return Entropy.mutual(key_B, key_A, rows, val_A, val_B) / Entropy.Personal.regular(key_A, rows, val_A)
    
