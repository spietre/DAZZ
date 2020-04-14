
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
from Statistics import Statistics as stat
from statistics import NormalDist

header = ['Tumor',  'History',    'Heredity',   'Age',    'Cancer']

# data = [
#     #Tumor  #History    #Heredity   #Age    #Cancer
#     ['confirmed',	'high',	'yes',	'younger',	'high'],
#     ['confirmed',	'high',	'yes',	'elder',	'high'],
#     ['no',	'high',	'yes',	'younger',	'low'],
#     ['non confirmed',	'medium',	'yes',	'younger',	'low'],
#     ['non confirmed',	'low',	'no',	'younger',	'low'],
#     ['non confirmed',	'low',	'no',	'elder',	'high'],
#     ['no',	'low',	'no',	'elder',	'low'],
#     ['confirmed',	'medium',	'yes',	'younger',	'high'],
#     ['confirmed',	'low',	'no',	'younger',	'low'],
#     ['non confirmed',	'medium',	'no',	'younger',	'low'],
#     ['confirmed',	'medium',	'no',	'elder',	'low'],
#     ['no',	'medium',	'yes',	'elder',	'low'],
#     ['no',	'high',	'no',	'younger',	'low'],
#     ['non confirmed',	'medium',	'yes',	'elder',	'high']
# ]

data = [
    #Tumor  #History    #Heredity   #Age    #Cancer
    ['confirmed',	85,	'yes',	'younger',	'high'],
    ['confirmed',	80,	'yes',	'elder',	'high'],
    ['no',	83,	'yes',	'younger',	'low'],
    ['non confirmed',	70,	'yes',	'younger',	'low'],
    ['non confirmed',	68,	'no',	'younger',	'low'],
    ['non confirmed',	65,	'no',	'elder',	'high'],
    ['no',	64,	'no',	'elder',	'low'],
    ['confirmed',	72,	'yes',	'younger',	'high'],
    ['confirmed',	69,	'no',	'younger',	'low'],
    ['non confirmed',	75,	'no',	'younger',	'low'],
    ['confirmed',	75,	'no',	'elder',	'low'],
    ['no',	72,	'yes',	'elder',	'low'],
    ['no',	81,	'no',	'younger',	'low'],
    ['non confirmed',	71,	'yes',	'elder',	'high']
]

# number of attributes for each object
cols_num = len(data[0])
# list of dictionaries, each dictionary contains values of attribute
# ex.: [{'non confirmed', 'confirmed', 'no'}]
data_vals = [set() for i in range(cols_num)]

# index of attribute that we want to decide in the future
cancer_col_idx = cols_num - 1

for cur_row in data:
    for cur_col_idx in range(cols_num):
        try:
            if type(cur_row[cur_col_idx]) is not str:
                continue
            data_vals[cur_col_idx].add(cur_row[cur_col_idx])
        except Exception:
            print(f"{cur_row[cur_col_idx]} already in")

###############OUTPUT###############
print()
for i in range(cols_num):
    print(data_vals[i])
    
# {'no', 'non confirmed', 'confirmed'}
# {'high', 'medium', 'low'}  or  set()
# {'yes', 'no'}
# {'younger', 'elder'}
# {'high', 'low'}
####################################

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
# {'high': {'high': 0, 'medium': 0, 'low': 0}, 'low': {'high': 0, 'medium': 0, 'low': 0}}  or  {'high': [], 'low': []}
# {'high': {'yes': 0, 'no': 0}, 'low': {'yes': 0, 'no': 0}}
# {'high': {'younger': 0, 'elder': 0}, 'low': {'younger': 0, 'elder': 0}}
# {'high': 0, 'low': 0}
####################################

for cur_row in data:
    for cur_col_idx in range(cols_num):
        if cur_col_idx != cancer_col_idx:
            ## regular column handling (not the resulting one) ##
            if type(cur_row[cur_col_idx]) is str:
                ## string columns value handling ##
                data_prep[header[cur_col_idx]][cur_row[cancer_col_idx]][cur_row[cur_col_idx]] += 1
            else:
                ## numeric columns value handling ##
                data_prep[header[cur_col_idx]][cur_row[cancer_col_idx]].append(cur_row[cur_col_idx])
        else:
            ## resulting 'cancer' column handling ##
            data_prep[header[cancer_col_idx]][cur_row[cancer_col_idx]] += 1

###############OUTPUT###############
print()
for i in range(cols_num):
    print(f'{header[i]}: {data_prep[header[i]]}')

# Tumor: {'high': {'no': 0, 'non confirmed': 2, 'confirmed': 3}, 'low': {'no': 4, 'non confirmed': 3, 'confirmed': 2}}
# History: {'high': {'high': 2, 'medium': 2, 'low': 1}, 'low': {'high': 2, 'medium': 4, 'low': 3}}  or  History: {'high': [85, 80, 65, 72, 71], 'low': [83, 70, 68, 64, 69, 75, 75, 72, 81]}
# Heredity: {'high': {'yes': 4, 'no': 1}, 'low': {'yes': 3, 'no': 6}}
# Age: {'high': {'younger': 2, 'elder': 3}, 'low': {'younger': 6, 'elder': 3}}
# Cancer: {'high': 5, 'low': 9}
####################################

#new_data = ['confirmed',	'low',	'yes',	'elder', None]
new_data = ['confirmed',	80,	'yes',	'elder', None]

tmp_results = dict.fromkeys([i for i in data_vals[cancer_col_idx]], .0)

for cancer_val in data_vals[cancer_col_idx]:
    for cur_col_idx in range(cols_num):
        new_result = .0
        if new_data[cur_col_idx] is not None:
            ## regular column handling (not the resulting one) ##
            if type(new_data[cur_col_idx]) is str:
                ## string columns value handling ##
                #print(f'{header[cancer_col_idx]}:{cancer_val}|{header[cur_col_idx]}:{new_data[cur_col_idx]} = {data_prep[header[cur_col_idx]][cancer_val][new_data[cur_col_idx]] / sum([i for i in data_prep[header[cur_col_idx]][cancer_val].values()])}')
                new_result = data_prep[header[cur_col_idx]][cancer_val][new_data[cur_col_idx]] / sum([i for i in data_prep[header[cur_col_idx]][cancer_val].values()])
                tmp_results[cancer_val] = new_result if tmp_results[cancer_val] == .0 else tmp_results[cancer_val] * new_result
            else:
                ## numeric columns value handling ##
                new_result = NormalDist(mu=stat.mean(data_prep[header[cur_col_idx]][cancer_val]), sigma=stat.std_deviation(data_prep[header[cur_col_idx]][cancer_val])).pdf(new_data[cur_col_idx])
                tmp_results[cancer_val] = new_result if tmp_results[cancer_val] == .0 else tmp_results[cancer_val] * new_result
        else:
            ## resulting 'cancer' column handling ##
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
print(f'checksum = {tmp_sum}')

# P(Cancer:high|atrs) = 0.795417348608838
# P(Cancer:low|atrs) = 0.20458265139116202
# sum = 1.0
####################################