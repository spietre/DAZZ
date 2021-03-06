
from Statistics.Statistics import Statistics as stat
from statistics import NormalDist

class Bayes:
    
    @staticmethod
    def distinctColVals(rows: list, verbose = False):
        # number of attributes for each object
        cols_num = len(rows[0])
        # list of dictionaries, each dictionary contains values of attribute
        # ex.: [{'non confirmed', 'confirmed', 'no'}]
        data_vals = [set() for i in range(cols_num)]        

        for row in rows:
            for col, val in enumerate(row):
                try:
                    if type(val) is str or type(val) is bool:
                        data_vals[col].add(val)
                    else: 
                        continue
                except Exception:
                    print(f"{val} already in")

        ###############OUTPUT###############
        if verbose:
            print()
            for i in range(cols_num):
                print(data_vals[i])
                
            # {'no', 'non confirmed', 'confirmed'}
            # {'high', 'medium', 'low'}  <-- or -->  set()
            # {'yes', 'no'}
            # {'younger', 'elder'}
            # {'high', 'low'}
        ####################################
        
        return data_vals
    
    @staticmethod
    def Classify(rows: list, header: list, new_data: list):
        # number of attributes for each object
        cols_num = len(rows[0])
        # index of attribute that we want to decide in the future
        cancer_col_idx = cols_num - 1
        
        data_vals = Bayes.distinctColVals(rows, True)

        data_prep = {}

        for i in header:
            data_prep[i] = dict()

        for cur_col_idx in range(cols_num):
            if cur_col_idx != cancer_col_idx:
                ## regular column handling (not the resulting one) ##
                for cancer_val in data_vals[cancer_col_idx]:
                    if len(data_vals[cur_col_idx]) != 0:
                        ## string columns value handling ##
                        data_prep[header[cur_col_idx]][cancer_val] = dict.fromkeys(data_vals[cur_col_idx], 0)
                    else:
                        ## numeric columns value handling ##
                        data_prep[header[cur_col_idx]][cancer_val] = list()
            else:
                ## resulting 'cancer' column handling ##
                for cancer_val in data_vals[cancer_col_idx]:
                    data_prep[header[cancer_col_idx]][cancer_val] = 0
                    
        ###############OUTPUT###############
        print()
        for i in header:
            print(data_prep[i])
            
        # {'high': {'no': 0, 'non confirmed': 0, 'confirmed': 0}, 'low': {'no': 0, 'non confirmed': 0, 'confirmed': 0}}      
        # {'high': {'high': 0, 'medium': 0, 'low': 0}, 'low': {'high': 0, 'medium': 0, 'low': 0}}  <-- or -->  {'high': [], 'low': []}
        # {'high': {'yes': 0, 'no': 0}, 'low': {'yes': 0, 'no': 0}}
        # {'high': {'younger': 0, 'elder': 0}, 'low': {'younger': 0, 'elder': 0}}
        # {'high': 0, 'low': 0}
        ####################################

        for row in rows:
            for col_idx, val in enumerate(row):
                if col_idx != cancer_col_idx:
                    ## regular column handling (not the resulting one) ##
                    if type(val) is str or type(val) is bool:
                        ## string columns value handling ##
                        data_prep[header[col_idx]][row[cancer_col_idx]][val] += 1
                    else:
                        ## numeric columns value handling ##
                        data_prep[header[col_idx]][row[cancer_col_idx]].append(val)
                else:
                    ## resulting 'cancer' column handling ##
                    data_prep[header[cancer_col_idx]][row[cancer_col_idx]] += 1

        ###############OUTPUT###############
        print()
        for i in range(cols_num):
            print(f'{header[i]}: {data_prep[header[i]]}')

        # Tumor: {'high': {'no': 0, 'non confirmed': 2, 'confirmed': 3}, 'low': {'no': 4, 'non confirmed': 3, 'confirmed': 2}}
        # History: {'high': {'high': 2, 'medium': 2, 'low': 1}, 'low': {'high': 2, 'medium': 4, 'low': 3}}  <-- or -->  History: {'high': [85, 80, 65, 72, 71], 'low': [83, 70, 68, 64, 69, 75, 75, 72, 81]}
        # Heredity: {'high': {'yes': 4, 'no': 1}, 'low': {'yes': 3, 'no': 6}}
        # Age: {'high': {'younger': 2, 'elder': 3}, 'low': {'younger': 6, 'elder': 3}}
        # Cancer: {'high': 5, 'low': 9}
        ####################################

    

        tmp_results = dict.fromkeys([i for i in data_vals[cancer_col_idx]], 1.0)

        for cancer_val in data_vals[cancer_col_idx]:
            for ccol_idxol, val in enumerate(new_data):
                new_result = .0
                if val is not None:
                    ## regular column handling (not the resulting one) ##
                    if type(val) is str or type(val) is bool:
                        ## string columns value handling ##
                        #print(f'{header[cancer_col_idx]}:{cancer_val}|{header[cur_col_idx]}:{new_data[cur_col_idx]} = {data_prep[header[cur_col_idx]][cancer_val][new_data[cur_col_idx]] / sum([i for i in data_prep[header[cur_col_idx]][cancer_val].values()])}')
                        new_result = data_prep[header[ccol_idxol]][cancer_val][val] / sum([i for i in data_prep[header[ccol_idxol]][cancer_val].values()])
                        tmp_results[cancer_val] = tmp_results[cancer_val] * new_result
                    else:
                        ## numeric columns value handling ##
                        new_result = NormalDist(mu=stat.mean(data_prep[header[ccol_idxol]][cancer_val]), sigma=stat.std_deviation(data_prep[header[ccol_idxol]][cancer_val])).pdf(val)
                        tmp_results[cancer_val] = tmp_results[cancer_val] * new_result
                else:
                    ## resulting 'cancer' column handling ##
                    #print(f'{header[cancer_col_idx]}:{cancer_val} = {data_prep[header[cancer_col_idx]][cancer_val] / sum([i for i in data_prep[header[cancer_col_idx]].values()])}')
                    new_result = data_prep[header[cancer_col_idx]][cancer_val] / sum([i for i in data_prep[header[cancer_col_idx]].values()])
                    tmp_results[cancer_val] = tmp_results[cancer_val] * new_result

        results = dict.fromkeys([i for i in data_vals[cancer_col_idx]], .0)

        for key, val in tmp_results.items():
            results[key] = val / sum([i for i in tmp_results.values()])
            
        ###############OUTPUT###############
        print()
        tmp_sum = .0
        for key, val in results.items():
            print(f'P({header[cancer_col_idx]}:{key}|atrs) = {val}')
            tmp_sum += val
        print(f'checksum = {tmp_sum}')

        # P(Cancer:high|atrs) = 0.795417348608838
        # P(Cancer:low|atrs) = 0.20458265139116202
        # sum = 1.0
        ####################################