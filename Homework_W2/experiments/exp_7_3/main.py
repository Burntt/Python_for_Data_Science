import pandas as pd
import numpy as np
import pickle
from experiments.exp_7_3.transformer import Transformer_7_3
from experiments.base.classifier import LogisticCustomClassifier

X_train, X_test, y_train, y_test = pickle.load(open('split.pickle', 'rb'))

features = 'text'
target = 'Bin_High_Retweet_Count'

classifier = LogisticCustomClassifier('experiments/exp_7_3/config.yaml', Transformer_7_3, 'experiments/exp_7_3/result/')
classifier.fit(X_train, y_train[target])
y_pred = classifier.predict(X_test)
classifier.generate_results(y_pred, y_test[target])