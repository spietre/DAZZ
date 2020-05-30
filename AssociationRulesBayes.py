from Data.BayesData import Cancer
from Data.BayesData import ECancer
from Statistics.Cardinality import Cardinality
from Statistics.Statistics import DB



# result = Cardinality.conditional({Tumor.History : 'low', Tumor.Heredity : 'no'}, Tumor.LinguisticDataSet)

# print(result)

# result = Cardinality.conditional({Tumor.Heredity : 'no'}, Tumor.LinguisticDataSet)

# print(result)

# Bayes.distinctColVals(Cancer.LinguisticDataSet, True)

# print(
cols = DB.distinct(Cancer.LinguisticDataSet, ECancer)
associationRules = set()

for i in ECancer:    
    for j in ECancer:
        if i == j: continue
        for k in ECancer:
            if j == k or i == k: continue
            
            for icol in cols[i.value]:
                for jcol in cols[j.value]:
                    for kcol in cols[k.value]:
                        
                        allTrue = Cardinality.Bayes.conditional({
                                i.value : icol,
                                j.value : jcol,
                                k.value : kcol
                            }, Cancer.LinguisticDataSet)
                        if (allTrue > 1):
                            # 001
                            ooi = Cardinality.Bayes.conditional({
                                    i.value : icol,
                                    j.value : jcol
                                }, Cancer.LinguisticDataSet)
                            if(ooi != 0 and allTrue / ooi == 1):
                                string = f'IF {i.name}={icol} and {j.name}={jcol} THEN {k.name}={kcol}\t support: {allTrue}, confidence: {allTrue / ooi * 100}%'
                                # print(f'\t001 {string}')
                                associationRules.add(string)
                            
                            # 010
                            oio = Cardinality.Bayes.conditional({
                                    i.value : icol,
                                    k.value : kcol
                                }, Cancer.LinguisticDataSet)
                            if(oio != 0 and allTrue / oio == 1):
                                string = f'IF {i.name}={icol} and {k.name}={kcol} THEN {j.name}={jcol}\t support: {allTrue}, confidence: {allTrue / oio * 100}%'
                                # print(f'\t010 {string}')
                                associationRules.add(string)
                                
                            # 011
                            oii = Cardinality.Bayes.conditional({
                                    i.value : icol
                                }, Cancer.LinguisticDataSet)
                            if(oii != 0 and allTrue / oii == 1):
                                string = f'IF {i.name}={icol} THEN {k.name}={kcol} and {j.name}={jcol}\t support: {allTrue}, confidence: {allTrue / oii * 100}%'
                                # print(f'\t011 {string}')
                                associationRules.add(string)
                            
                            # 100
                            ioo = Cardinality.Bayes.conditional({
                                    j.value : jcol,
                                    k.value : kcol
                                }, Cancer.LinguisticDataSet)
                            if(ioo != 0 and allTrue / ioo == 1):
                                string = f'IF {k.name}={kcol} and {j.name}={jcol} THEN {i.name}={icol}\t support: {allTrue}, confidence: {allTrue / ioo * 100}%'
                                # print(f'\t100 {string}')
                                associationRules.add(string)
                            
                            # 101
                            ioi = Cardinality.Bayes.conditional({                            
                                    j.value : jcol
                                }, Cancer.LinguisticDataSet)
                            if(ioi != 0 and allTrue /ioi == 1):
                                string = f'IF {j.name}={jcol} THEN {i.name}={icol} and {k.name}={kcol}\t support: {allTrue}, confidence: {allTrue / ioi * 100}%'
                                # print(f'\t101 {string}')
                                associationRules.add(string)
                                
                            # 110
                            iio = Cardinality.Bayes.conditional({                            
                                    k.value : kcol
                                }, Cancer.LinguisticDataSet)
                            if(iio != 0 and allTrue / iio == 1):
                                string = f'IF {k.name}={kcol} THEN {j.name}={jcol} and {i.name}={icol}\t support: {allTrue}, confidence: {allTrue / iio * 100}%'
                                # print(f'\t110 {string}')
                                associationRules.add(string)
                                
                            # # 111
                            # if(allTrue/Cardinality.Bayes.conditional({                            
                            #     k.value : kcol
                            # }, Cancer.LinguisticDataSet) == 1):
                            #     print(f'IF {k.name}={kcol} THEN {j.name}={jcol} and {i.name}={icol}')
                                    
for i, string in enumerate(associationRules):
    print(f'{i} {string}') 
                        
# true means that item is in result    
# def compute(i: bool, j: bool, k: bool):
#     if not i and not j and not k:
#         raise Exception('all arguments false!')
    
    
        
    