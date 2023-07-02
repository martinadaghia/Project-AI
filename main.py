import os
import json

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import svm_model
import lr_model
import seaborn as sns
import load_dataset
from sklearn.feature_selection import mutual_info_classif, SelectPercentile

DIR_NAME = 'src/Audio/'

# IS COVID PROBABILITY THRESHOLD
THRESHOLD = 0.30
# NUMBER OF TOP FEATURES TO SELECT
NUM_FEATURES = 350

PERCENT = 25


def init_models(data_list, labels_list, randomness, test_size, threshold):
    lr_model.train_and_test(data_list, labels_list, randomness, test_size, threshold)
    svm_model.train_and_test(data_list, labels_list, randomness, test_size, threshold)


# load_dataset.load_data(DIR_NAME)
with open('./data.json', 'r') as f:
    dataset = json.load(f)
data = []
labels = []
for element in dataset:
    array = np.array(list(element['audio_features'].values()))
    data.append(array)
    labels.append(element['covid'])


data = np.array(data)  # Converti la lista di array in un array bidimensionale


print('Each of ' + str(len(data)) + ' element has ' + str(len(dataset[0]['audio_features'])) + ' features\n')
# init_models(data_list=data, labels_list=labels, randomness=10, test_size=0.2, threshold=THRESHOLD)

importance = mutual_info_classif(data, labels)
feat_imp = pd.Series(importance, pd.DataFrame(data).columns)

# Calcola la percentuale di elementi con valore zero
# num_zeros = np.count_nonzero(feat_imp == 0)
# percentage_zeros = (num_zeros / feat_imp.size) * 100
# print("Numero di zeri:", num_zeros)
# print("Percentuale di zeri:", percentage_zeros, "%")

# feat_imp.plot(kind='barh')

# plt.yticks(pd.DataFrame(data).columns, dataset[0]['audio_features'].keys(), rotation='horizontal')
# plt.show()
# selector = SelectPercentile(percentile=PERCENT)
# Adattamento e trasformazione dei dati
# selected_features = selector.fit_transform(data, labels)
# top_indices = selector.get_support(indices=True)
# print("Selezionate " + str(len(top_indices)) + " features")


# Ottieni gli indici degli elementi in ordine decrescente di importanza
indices = np.argsort(feat_imp)[::-1]

# Seleziona i primi n indici

top_indices = indices[:NUM_FEATURES]

# !=0 per togliere solo quelle inutili
# feat_imp = feat_imp[feat_imp >= 0.03]

# Aggiornamento delle features con quelle selezionate migliori
feat_imp = feat_imp[top_indices]
print("Valore minimo importanza feature:", feat_imp.min())
# Plot delle features migliori
plot_labels_new = [list(dataset[0]['audio_features'].keys())]
labels_new = np.array(plot_labels_new)
important_features_indexes = feat_imp.index.tolist()
labels_new = labels_new[0][important_features_indexes]
feat_imp.plot(kind='barh')
plt.yticks(range(len(labels_new)), labels_new, rotation='horizontal')
plt.show()

reduced_data = []
for element_features in data:
    element_new_features = [element_features[index] for index in important_features_indexes]
    reduced_data.append(element_new_features)

print("Reduced data results")
init_models(data_list=reduced_data, labels_list=labels, randomness=0, test_size=0.2, threshold=THRESHOLD)


