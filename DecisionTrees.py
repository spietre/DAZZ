from Statistics import Entropy

header = ['Tumor',  'History',    'Heredity',   'Age',    'Cancer']
# data = [
#     #Tumor  #History    #Heredity   #Age    #Cancer
#     ['confirmed',	85,	'yes',	'younger',	'high'],
#     ['confirmed',	80,	'yes',	'elder',	'high'],
#     ['no',	83,	'yes',	'younger',	'low'],
#     ['non confirmed',	70,	'yes',	'younger',	'low'],
#     ['non confirmed',	68,	'no',	'younger',	'low'],
#     ['non confirmed',	65,	'no',	'elder',	'high'],
#     ['no',	64,	'no',	'elder',	'low'],
#     ['confirmed',	72,	'yes',	'younger',	'high'],
#     ['confirmed',	69,	'no',	'younger',	'low'],
#     ['non confirmed',	75,	'no',	'younger',	'low'],
#     ['confirmed',	75,	'no',	'elder',	'low'],
#     ['no',	72,	'yes',	'elder',	'low'],
#     ['no',	81,	'no',	'younger',	'low'],
#     ['non confirmed',	71,	'yes',	'elder',	'high']
# ]

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

forms = '{:15s}{:10s}{:10s}{:10s}{:10s}{:10s}{:10s}'

print(forms.format('Atribute A_i', 'H(Cancer)', 'H(A_i)', 'H(B,A_i)', 'I(B;A_i)', 'H(B|A_i)', 's(A_i,|B)'))

cancer_idx = len(header) - 1
# entropy of cancer
cancEnt = Entropy.Personal.regular(cancer_idx, data)

for col_idx in range(cancer_idx):
    # what = ()
    formf = "{:15s}{:1.4f}{:10.4f}{:10.4f}{:10.4f}{:10.4f}{:10.4f}"
    print(formf.format(
        header[col_idx],
        cancEnt,
        Entropy.Personal.regular(col_idx, data),
        Entropy.Joint.regular(cancer_idx, col_idx, data),
        Entropy.mutual(cancer_idx, col_idx, data),
        Entropy.conditional(cancer_idx, col_idx, data),
        Entropy.stability(col_idx, cancer_idx, data))
    )
    # print(formf % what)
    

print(forms.format('Atribute A_i', 'H(B|confirmed)', 'H(A_i|confirmed)', 'H(B,A_i,confirmed)', 'I(B;A_i|confirmed)', 'H(B|A_i)', 's(A_i,|B)'))    
cancIfTumorConfirmed = Entropy.conditional(cancer_idx, 0, data, val_B='confirmed')

for col_idx in range(1, cancer_idx):
    # what = ()
    formf = "{:15s}{:1.4f}{:10.4f}{:10.4f}{:10.4f}{:10.4f}{:10.4f}"
    print(formf.format(
        header[col_idx],
        cancIfTumorConfirmed,
        Entropy.Joint.regular(col_idx, 0, data, val_B='confirmed'),
        Entropy.Joint.regular(cancer_idx, col_idx, data, ),
        Entropy.mutual(cancer_idx, col_idx, data),
        Entropy.conditional(cancer_idx, col_idx, data),
        Entropy.stability(col_idx, cancer_idx, data))
    )
    # print(formf % what)
    