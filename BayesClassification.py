
# class Dict:
#     Name: str
#     Vals: dict
    
#     @property
#     def Sum(self):
#         return sum(self.Vals.values())
    
#     def __init__(self, name):
#         self.Name = name
#         self.Vals = dict()        
    
#     def __getitem__(self, key):
#         return self.Vals[key]
    
#     def __setitem__(self, key, val):
#         self.Vals[key] = val
    
#     def __repr__(self):
#         return f'{self.Name}, {self.Sum}, {self.Vals}'


header = ['Tumor',  'History',    'Heredity',   'Age',    'Cancer']

data = [
    #Tumor  #History    #Heredity   #Age    #Cancer
    ['confirmed',	'high',	'yes',	'younger',	'high'],
    ['confirmed',	'high',	'yes',	'elder',	'high'],
    ['no',	'high',	'yes',	'younger',	'low'],
    ['non confirmed',	'medium',	'yes',	'younger',	'low'],
    ['non confirmed',	'low',	'no',	'younger',	'low'],
    ['non confirmed',	'low',	'no',	'elder',	'high'],
    ['no',	'low',	'no',	'elder',	'low'],
    ['confirmed',	'medium',	'yes',	'younger',	'high'],
    ['confirmed',	'low',	'no',	'younger',	'low'],
    ['non confirmed',	'medium',	'no',	'younger',	'low'],
    ['confirmed',	'medium',	'no',	'elder',	'low'],
    ['no',	'medium',	'yes',	'elder',	'low'],
    ['no',	'high',	'no',	'younger',	'low'],
    ['non confirmed',	'medium',	'yes',	'elder',	'high']
]

# number of attributes for each object
cols_num = len(data[0])
# list of dictionaries, each dictionary contains values of attribute
# ex.: [{'non confirmed', 'confirmed', 'no'}]
data_vals = [set() for i in range(cols_num)]

# index of attribute that we want to decide in the future
cancer_col_idx = cols_num - 1

for item in data:
    for i in range(cols_num):
        try:
            data_vals[i].add(item[i])
        except Exception:
            print(f"{item[i]} already in")

###############OUTPUT###############
print()
for i in range(cols_num):
    print(data_vals[i])
####################################

data_prep = {}

for i in header:
    data_prep[i] = dict()

for cur_col_idx in range(cols_num):
    if cur_col_idx != cancer_col_idx:
        for cancer_val in data_vals[cancer_col_idx]:
            data_prep[header[cur_col_idx]][cancer_val] = dict.fromkeys(data_vals[cur_col_idx], 0)
    else:
        for cancer_val in data_vals[cancer_col_idx]:
            data_prep[header[cancer_col_idx]][cancer_val] = 0
            
###############OUTPUT###############
print()
for i in header:
    print(data_prep[i])
####################################

for cur_row in data:
    for cur_col_idx in range(cols_num):
        if cur_col_idx != cancer_col_idx:
            data_prep[header[cur_col_idx]][cur_row[cancer_col_idx]][cur_row[cur_col_idx]] += 1
        else:
            data_prep[header[cancer_col_idx]][cur_row[cancer_col_idx]] += 1

###############OUTPUT###############
print()
for i in range(cols_num):
    print(f'{header[i]}: {data_prep[header[i]]}')
####################################

new_data = ['confirmed',	'low',	'yes',	'elder', None]

tmp_results = dict.fromkeys([i for i in data_vals[cancer_col_idx]], .0)

for cancer_val in data_vals[cancer_col_idx]:
    for cur_col_idx in range(cols_num):
        new_result = .0
        if new_data[cur_col_idx] is not None:
            #print(f'{header[cancer_col_idx]}:{cancer_val}|{header[cur_col_idx]}:{new_data[cur_col_idx]} = {data_prep[header[cur_col_idx]][cancer_val][new_data[cur_col_idx]] / sum([i for i in data_prep[header[cur_col_idx]][cancer_val].values()])}')
            new_result = data_prep[header[cur_col_idx]][cancer_val][new_data[cur_col_idx]] / sum([i for i in data_prep[header[cur_col_idx]][cancer_val].values()])
            tmp_results[cancer_val] = new_result if tmp_results[cancer_val] == .0 else tmp_results[cancer_val] * new_result
        else:
            #print(f'{header[cancer_col_idx]}:{cancer_val} = {data_prep[header[cancer_col_idx]][cancer_val] / sum([i for i in data_prep[header[cancer_col_idx]].values()])}')
            new_result = data_prep[header[cancer_col_idx]][cancer_val] / sum([i for i in data_prep[header[cancer_col_idx]].values()])
            tmp_results[cancer_val] = new_result if tmp_results[cancer_val] == .0 else tmp_results[cancer_val] * new_result

results = dict.fromkeys([i for i in data_vals[cancer_col_idx]], .0)

for key, val in tmp_results.items():
    results[key] = val / sum([i for i in tmp_results.values()])
    
###############OUTPUT###############
print()
tmp_sum = .0
for key, val in results.items():
    print(f'P({header[cancer_col_idx]}:{key}|atrs) = {val}')
    tmp_sum += val
print(f'sum = {tmp_sum}')
####################################