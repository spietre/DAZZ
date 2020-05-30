class Probability:
    @staticmethod        
    def of(A = None, key = None, rows = None, M = None, N = None):
        """ Calculates probability of an 'A' being inside 'rows' list. """
        probability = .0
        if rows is None or A is None or key is None:
            probability = M / N
        else:
            probability = sum([row[key] == A for row in rows]) / len(rows)
        
        return probability
    
    @staticmethod
    def personal(A = None, key = None, rows = None, M = None, N = None):
        """ Calculates same thing as 'of' method. """
        return Probability.of(A, key, rows)
    
    @staticmethod
    def conjoint(A, B, key_A, key_B, rows):
        """
        Calculates probability of 'A' and 'B' being inside 'rows' stored at indices 'key_A' and 'key_B'.\n
        P(A,B) = P(A and B) \n
        OR\n
        P(A,B) = P(A x B)
        """
        return sum([A == row[key_A] and B == row[key_B] for row in rows]) / len(rows)
        
    @staticmethod
    def conditional(A, B, key_A, key_B, rows):
        """ 
        Calculates conditional probablity of 'A' if we consider 'B' have already happend. \n
        P(A|B) = P(A,B) / P(B)
        """
        return Probability.conjoint(A, B, key_A, key_B, rows) / Probability.personal(B, key_B, rows)