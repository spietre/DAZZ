
from BayesClassification import Bayes

# TEST zadanie 1-9
from Data.BayesData import Sight

Bayes.Classify(Sight.LinguisticDataSet, Sight.Header, Sight.LinguisticNew1)
Bayes.Classify(Sight.LinguisticDataSet, Sight.Header, Sight.LinguisticNew2)

Bayes.Classify(Sight.NumericDataSet, Sight.Header, Sight.NumericNew1)
Bayes.Classify(Sight.NumericDataSet, Sight.Header, Sight.NumericNew2)
################################################################


# TEST zadanie minuly rok
from Data.BayesData import Sight_old

Bayes.Classify(Sight_old.Data, Sight_old.Header, Sight_old.new_data1)
Bayes.Classify(Sight_old.Data, Sight_old.Header, Sight_old.new_data2)
################################################################


# TEST zadanie minuly rok
from Data.BayesData import Cancer

Bayes.Classify(Cancer.LinguisticDataSet, Cancer.Header, Cancer.LinguisticNew)
Bayes.Classify(Cancer.NumericDataSet, Cancer.Header, Cancer.NumericNew)
