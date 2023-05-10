import os
import json
import numpy as np

from sklearn import svm
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

import matplotlib.pyplot as plt

import load_dataset

DIR_NAME = 'src/Test/'

load_dataset.load_data(DIR_NAME)

with open('./data.json', 'r') as f:
    dataset = json.load(f)
print(dataset)
features = []
labels = []
for element in dataset:
    array = np.array(list(element['audio_features'].values()))
    features.append(array)
    labels.append(element['covid'])
print('\nEnd.')
print('Each element has ' + str(len(dataset[0])) + ' features ')

# Divisione dei dati in set di addestramento e di test
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2)

# Training SVM
clf = svm.SVC()
clf.fit(X_train, y_train)

# Effettua le previsioni sul set di test
y_pred = clf.predict(X_test)

# Valuta le prestazioni del modello
accuracy_svm = accuracy_score(y_test, y_pred)
print('SVM Accuracy:', accuracy_svm)

# Crea e addestra il modello di regressione logistica
model = LogisticRegression(max_iter=1000000)
model.fit(X_train, y_train)

# Effettua le previsioni sul set di test
y_pred = model.predict(X_test)

# Valuta le prestazioni del modello
accuracy_lr = accuracy_score(y_test, y_pred)
print('LR Accuracy:', accuracy_lr)
