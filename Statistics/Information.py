import math
from Statistics.Probability import Probability
from Statistics.Cardinality import Cardinality

class Information:    
    @staticmethod
    def of(A = None, key_A = None, rows = None, probability: float = None):
        """ 
        Calculates how much infromation does 'A' provides. \n
        I(A) = -log2( P(A) )
        """
        if probability is None:
            probability = Probability.of(A, key_A, rows)
        
        return -math.log2(probability) if probability > 0 else 0
    
    class Personal:
        @staticmethod
        def bayes(A = None, key_A = None, rows = None, probability: float = None):
            """ 
            Calculates same thing as 'of' method. The personal information of 'A' describes uncertainty of this value. \n
            I(A) = -log2( P(A) )
            """
            return Information.of(A=A, key_A=key_A, rows=rows, probability=probability)
        
        @staticmethod
        def fuzzy(A, key_A, rows: list):
            """ 
                I(A1) = log2( M(A) ) -log2( M(A1) )
            """
            return math.log2(Cardinality.personal(A, rows)) - math.log2(Cardinality.personal(A, rows, key_A))
    
    class Joint:
        @staticmethod
        def bayes(A = None, B = None, rows = None, key_A = None, key_B = None, probability: float = None):
            """ 
            Conjoint information of 'A' and 'B' describes common uncertainty of these two values. \n
            I(A,B) = -log2( P(A,B) )
            """
            if probability is None:
                probability = Probability.conjoint(A, B, key_A, key_B, rows)
            
            return -math.log2(probability) if probability > 0 else 0
    
        @staticmethod
        def fuzzy(A, key_A, B, key_B, rows: list):
            """ 
                I(A,B) = log2( M(A) = M(B) ) -log2( M(A,B) )                 
            """
            n = Cardinality.personal(A, rows)
            joint = Cardinality.joint({ A : key_A, B : key_B }, rows)
            if joint > 0:
                return math.log2(n) - math.log2(joint)
            else:
                return math.log2(n)
        
        @staticmethod
        def _fuzzy(atr_col_pairs: dict, rows: list): # A, key_A, B, key_B,
            """            
                I(A1,B3,C2) = log2( M(A) = M(B) = M(C) ) - log2( M(A1,B3,C2) )\n
                { A : 2, B : 3, C : 1 } <=> { atribute key : inner column }\n
                atr_col_pairs is a dictionary of atributes and columns
            """
            # next(iter(dict)) returns the first key of ordered dictionary
            n = Cardinality.personal(list(atr_col_pairs.keys())[0], rows) # (A, rows)
            joint = Cardinality.joint(atr_col_pairs, rows)
            if joint > 0:
                return math.log2(n) - math.log2(joint)
            else:
                return math.log2(n)
        
    class Conditional:
        @staticmethod
        def bayes(A, B, key_A, key_B, rows):
            """ 
            Calculates and describes uncertainty of 'A' value if 'B' value is considered to be known.\n
            I(A|B) = I(A,B) - I(B)
            """
            return Information.Joint.bayes(A, B, key_A, key_B, rows) - Information.Personal.bayes(A)

        @staticmethod
        def fuzzy(A, key_A, B, key_B, rows: list):
            """ I(A|B) = I(A,B) - I(B) """
            return Information.Joint.fuzzy(B, key_B, A, key_A, rows) - Information.Personal.fuzzy(B, key_B, rows)
        
        @staticmethod
        def _fuzzy(atr_col_pairs: dict, rows: list):
            """ I(A|B1,C4) = I(A,B1,C4) - I(B1,C4) \n
                { A : 2, B : 3, C : 1 } <=> { atribute key : inner column }\n
                atr_col_pairs is a dictionary of atributes and columns            
            """
            #skip first item that is A
            first_skipped = iter(atr_col_pairs.items())
            next(first_skipped) # first item is skipped here (output atribute)
            
            return Information.Joint._fuzzy(atr_col_pairs, rows) - Information.Joint._fuzzy(dict(first_skipped), rows)
    
    class Mutual:
        @staticmethod
        def bayes(A, B, key_A, key_B, rows):
            """ Calculates information between 'A' and 'B' and describes dependency of 'A' on value of 'B' and vice versa. \n
            I(A;B) = I(A) - I(A|B) \n
            OR\n
            I(A;B) = I(A) + I(B) - I(A,B) """
            inf1 = Information.Personal.bayes(A, key_A, rows) - Information.Conditional.bayes(B, A, key_B, key_A, rows)
            inf2 = Information.Personal.bayes(A, key_A, rows) + Information.Personal.bayes(B, key_B, rows) - Information.Joint.bayes(A, B, key_A, key_B, rows)
            
            if (inf1 != inf2):
                raise AssertionError
            
            return inf1   
        
        @staticmethod
        def fuzzy(A, key_A, B, key_B, rows: list):
            """ 
                I(A;B) = I(A) - I(A|B)\n
                OR\n
                I(A;B) = I(A) + I(B) - I(A,B)
             """
            return Information.Personal.fuzzy(A, key_A, rows) - Information.Conditional.fuzzy(A, key_A, B, key_B, rows)
