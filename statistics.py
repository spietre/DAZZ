import math
import numpy
from enum import Enum

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
    
class DB:
    @staticmethod
    def distinct(rows: list, header: Enum, withColNames: bool = False):
        # list of dictionaries, each dictionary contains values of attribute
        # ex.: [{'non confirmed', 'confirmed', 'no'}]
        data_vals = { col.value if not withColNames else col.name : set() for col in header }

        for row in rows:
            for col, val in enumerate(row):
                try:
                    if type(val) is str or type(val) is bool:
                        data_vals[col if not withColNames else header(col).name].add(val)
                    else: 
                        continue
                except Exception:
                    print(f"{val} already in")

        ###############OUTPUT###############
        #{
            # 'Tumor': {'non confirmed', 'confirmed', 'no'}, 
            # 'History': {'low', 'high', 'medium'}, 
            # 'Heredity': {'yes', 'no'}, 
            # 'Age': {'younger', 'elder'}, 
            # 'Cancer': {'low', 'high'}
        # }
        # or with keys as numbers
        ####################################
        
        return data_vals

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
        """
            M(A) = A1 + A2 + A3 + ... + AN  =>  WHERE  A1 = A11 + A12 + A13 + ... + AM\n
            OR\n
            M(B3) = B31 + B32 + B33 + ... + B3N\n
            function sums all values of atribute A in column or in specific column of A column if key_a is specified
        """
        cardinality = .0
        for row in rows:
            if key_A is not None:
                # add only vlaue at key_A in A column for all rows
                # row: [ A: [ x, y, key_A, ... ], B: [], ... ]
                cardinality += row[A][key_A]
            else:
                # add all values in A column
                # row: [ A: [ x, y, z, ... ], B: [], ... ]
                # x + y + z + ...
                cardinality += sum([val for val in row[A]])
        
        return cardinality

    # @staticmethod
    # def joint_separate(A, key_A, B, key_B, rows: list):
    #     return sum([row[A][key_A] * row[B][key_B] for row in rows])
    
    @staticmethod
    def joint(atr_col_pairs: dict, rows: list):
        """
            M(A2, B3, C1) = (A21 * B31 * C11) + (A22 * B32 * C12) + (A23 * B33 * C13) + ... + (A2N * B3N * C2N);\n
            { A : 2, B : 3, C : 1 } <=> { atribute key or order : inner column }\n
            atr_col_pairs is a dictionary of atributes and columns
        """
        ret_sum = .0
        for row in rows:
            row_multiple = 1.0
            for atr, col in atr_col_pairs.items():
                if col is not None:
                    row_multiple *= row[atr][col]
                else:
                    # if column is not specified compute personal value of whole atribute
                    row_multiple *= sum([val for val in row[atr]])
            ret_sum += row_multiple
        
        return ret_sum
    
    class Bayes:
        @staticmethod
        def conditional(col_val_pairs: dict, rows: list):
            ret_sum = 0 #{ col : { val : 1 } for col, val in enumerate(col_val_pairs) }
            
            for row in rows:
                condition_was_met = True
                for col, val in col_val_pairs.items():
                    if row[col] != val:
                        condition_was_met = False
                
                if condition_was_met:
                    ret_sum += 1
            
            return ret_sum

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
    def stability(key_A, key_B, rows, val_A = None, val_B = None):
        """
            Coefficient of atribute connection stability, it determines which atribute contributes         
        """
        return Entropy.Mutual.bayes(key_B, key_A, rows, val_A, val_B) / Entropy.Personal.bayes(key_A, rows, val_A)
    
