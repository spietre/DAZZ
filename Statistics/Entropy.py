from Statistics.Cardinality import Cardinality
from Statistics.Probability import Probability
from Statistics.Information import Information

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
        def bayes(key_A, rows, val_A = None):
            """ H(A) = Sum{ P(A) * I(A) } """
            return Entropy.of(key_A, rows, val_A)
        
        @staticmethod
        def regular_helper(M, N):
            prob = Probability.of(M=M, N=N)
            
            return prob * Information.of(probability = prob)
        
        @staticmethod
        def fuzzy(A, rows: list):
            """ H(A) = Sum{ P(A) * I(A) } """
            entropy = .0
            for col in range(len(rows[0][A])):
                entropy += Cardinality.personal(A, rows, col) * Information.Personal.fuzzy(A, col, rows)
            
            return entropy

    class Joint:                    
        @staticmethod
        def bayes(key_A, key_B, rows, val_A = None, val_B = None):
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
            entropy = .0
            
            for a_key, dict_of_b in values.items():
                if val_A is None or val_A == a_key:
                    for b_key, occurrence in dict_of_b.items():
                        if val_B is None or val_B == b_key:
                            prob = Probability.of(M = occurrence, N = length)
                            entropy += prob * Information.of(probability = prob)
                
            return entropy

        @staticmethod
        def fuzzy(A, B, rows: list):
            """ H(A,B) = Sum{ Sum[ P(A,B) * I(A,B) ] } """
            entropy = .0
            for col_A in range(len(rows[0][A])):
                for col_B in range(len(rows[0][B])):
                    entropy += Cardinality.joint({ A : col_A, B : col_B }, rows) * Information.Joint.fuzzy(A, col_A, B, col_B, rows)

            return entropy
        
    class Conditional:
        @staticmethod
        def bayes(key_A, key_B, rows, val_A = None, val_B = None):
            """ 
            H(A|B) = H(A,B) – H(B) \n
            OR\n
            H(A|B) = Sum{ Sum[ P(A,B) * I(A|B) ] }
            """
            return Entropy.Joint.bayes(key_A, key_B, rows, val_A, val_B) - Entropy.Personal.bayes(key_B, rows, val_B)
    
        @staticmethod
        def fuzzy(A, B, rows: list, key_B = None):
            """ 
                H(A|B) = H(A,B) – H(B)\n
                OR\n
                H(A|B) = M(A,B) * I(A|B)
            """
            entropy = .0
            if key_B is not None:
                for col_A in range(len(rows[0][A])):
                    entropy += Cardinality.joint({ B : key_B, A : col_A }, rows) * Information.Conditional.fuzzy(A, col_A, B, key_B, rows)
            else:
                ######  this is one approach ########
                for col_B in range(len(rows[0][B])):
                    entropy += Entropy.Conditional.fuzzy(A, B, rows, col_B) # recursive call
                #####################################
            return entropy
        
        @staticmethod
        def _fuzzy(atr_col_pairs: dict, rows: list):
            entropy = .0
            atrs = list(atr_col_pairs.keys())
            last_atr = atrs[-1]
            first_atr = atrs[0]
            
            if atr_col_pairs[last_atr] is None:
                for col_B in range(len(rows[0][last_atr])):
                    atr_col_pairs[last_atr] = col_B
                    if atr_col_pairs[first_atr] is None:
                        for col_A in range(len(rows[0][first_atr])):
                            atr_col_pairs[first_atr] = col_A
                            entropy += Cardinality.joint(atr_col_pairs, rows) * Information.Conditional._fuzzy(atr_col_pairs, rows)
                        atr_col_pairs[first_atr] = None
                    else:
                        entropy += Cardinality.joint(atr_col_pairs, rows) * Information.Conditional._fuzzy(atr_col_pairs, rows)
                atr_col_pairs[last_atr] = None
            else:
                if atr_col_pairs[first_atr] is None:
                    for col_A in range(len(rows[0][first_atr])):
                        atr_col_pairs[first_atr] = col_A
                        entropy += Cardinality.joint(atr_col_pairs, rows) * Information.Conditional._fuzzy(atr_col_pairs, rows)
                    atr_col_pairs[first_atr] = None
                else:
                    entropy += Cardinality.joint(atr_col_pairs, rows) * Information.Conditional._fuzzy(atr_col_pairs, rows)

            return entropy
                
    
    class Mutual:
        @staticmethod
        def bayes(key_A, key_B, rows, val_A = None, val_B = None):
            """ 
            Stredné množstvo informácie o atribútu A v atribúte B\n
            I(A;B) = H(A) + H(B) - H(A,B) \n
            OR\n
            I(A;B) = H(A) - H(A|B) \n
            OR\n
            I(A;B) = Sum{ Sum[ P(A,B) * I(A;B) ] }
            """
            return Entropy.Personal.bayes(key_A, rows, val_A) + Entropy.Personal.bayes(key_B, rows, val_B) - Entropy.Joint.bayes(key_A, key_B, rows, val_A, val_B)

        @staticmethod
        def fuzzy(A, B, rows: list, key_B = None):
            """ 
                Stredné množstvo informácie o atribútu A v atribúte B \n
                I(A;B) = H(A) + H(B) - H(A,B)\n
                OR \n
                I(A;B) = H(A) - H(A|B) \n
                OR \n
                I(A;B) = Sum{ Sum[ P(A,B) * I(A;B) ] }
            """
            return Entropy.Personal.fuzzy(A, rows) - Entropy.Conditional.fuzzy(A, B, rows, key_B)
        
        @staticmethod
        def _fuzzy(atr_col_pairs: dict, rows: list):
            last_skipped = dict()
            i = -1
            for key, val in atr_col_pairs.items():
                i += 1
                if i < len(atr_col_pairs) - 1:
                    last_skipped[key] = val
            
            if len(last_skipped) > 1:
                entropy = Entropy.Conditional._fuzzy(last_skipped, rows) - Entropy.Conditional._fuzzy(atr_col_pairs, rows)
            else:
                entropy = Entropy.Mutual.fuzzy(list(atr_col_pairs.keys())[0], list(atr_col_pairs.keys())[1], rows, atr_col_pairs[list(atr_col_pairs.keys())[1]])
        
            return entropy
    @staticmethod
    def stability(key_A, key_B, rows, val_A = None, val_B = None):
        """
            Coefficient of atribute connection stability, it determines which atribute contributes         
        """
        return Entropy.Mutual.bayes(key_B, key_A, rows, val_A, val_B) / Entropy.Personal.bayes(key_A, rows, val_A)
    