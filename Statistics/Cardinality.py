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
    
    @staticmethod
    def resulting(atr_col_pairs: dict, rows: list):
        #skip first item that is A
        first_skipped = iter(atr_col_pairs.items())
        next(first_skipped) # first item is skipped here (output atribute)
        
        return Cardinality.joint(atr_col_pairs, rows) / Cardinality.joint(dict(first_skipped), rows)
    
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