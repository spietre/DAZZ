from Statistics.Cardinality import Cardinality
from Statistics.Statistics import DB
from Data.BreastCancerData import ECancer, data




cols = DB.distinct(data, ECancer)
associationRules = set()

# i = ECancer.a3
# j = ECancer.a8
# k = ECancer.a9

# icol = 'ge40'
# jcol = 'right'
# kcol = 'left_low'

min_accuracy = 1
min_support = 30

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
                            }, data)
                        if (allTrue >= min_support):
                            # 001
                            ooi = Cardinality.Bayes.conditional({
                                    i.value : icol,
                                    j.value : jcol
                                }, data)
                            if(ooi != 0 and allTrue / ooi >= min_accuracy):
                                string = f'IF {i.name}={icol} and {j.name}={jcol} THEN {k.name}={kcol}\t support: {allTrue}, confidence: {allTrue / ooi * 100}%'
                                associationRules.add(string)

                            # 010
                            oio = Cardinality.Bayes.conditional({
                                    i.value : icol,
                                    k.value : kcol
                                }, data)
                            if(oio != 0 and allTrue / oio >= min_accuracy):
                                string = f'IF {i.name}={icol} and {k.name}={kcol} THEN {j.name}={jcol}\t support: {allTrue}, confidence: {allTrue / oio * 100}%'
                                associationRules.add(string)
                                
                            # 011
                            oii = Cardinality.Bayes.conditional({
                                    i.value : icol
                                }, data)
                            if(oii != 0 and allTrue / oii >= min_accuracy):
                                string = f'IF {i.name}={icol} THEN {k.name}={kcol} and {j.name}={jcol}\t support: {allTrue}, confidence: {allTrue / oii * 100}%'
                                associationRules.add(string)

                            # 100
                            ioo = Cardinality.Bayes.conditional({
                                    j.value : jcol,
                                    k.value : kcol
                                }, data)
                            if(ioo != 0 and allTrue / ioo >= min_accuracy):
                                string = f'IF {k.name}={kcol} and {j.name}={jcol} THEN {i.name}={icol}\t support: {allTrue}, confidence: {allTrue / ioo * 100}%'
                                associationRules.add(string)

                            # 101
                            ioi = Cardinality.Bayes.conditional({                            
                                    j.value : jcol
                                }, data)
                            if(ioi != 0 and allTrue /ioi >= min_accuracy):
                                string = f'IF {j.name}={jcol} THEN {i.name}={icol} and {k.name}={kcol}\t support: {allTrue}, confidence: {allTrue / ioi * 100}%'
                                associationRules.add(string)
                                
                            # 110
                            iio = Cardinality.Bayes.conditional({                            
                                    k.value : kcol
                                }, data)
                            if(iio != 0 and allTrue / iio >= min_accuracy):
                                string = f'IF {k.name}={kcol} THEN {j.name}={jcol} and {i.name}={icol}\t support: {allTrue}, confidence: {allTrue / iio * 100}%'
                                associationRules.add(string)
                                
                            # 111
                            if(allTrue/len(data) > min_accuracy):
                                string = f'IF true THEN {i.name}={icol} and {j.name}={jcol} and {k.name}={kcol}\t support: {allTrue}, confidence: {allTrue / len(data) * 100}%'
                                associationRules.add(string)
    
    
with open('breastCancer.txt', 'w') as f:
    for i, string in enumerate(associationRules):
        f.write(f'{string}\n')
    
        # print(f'{i} {string}') 