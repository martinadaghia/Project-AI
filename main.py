import os
import json

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import svm_model
import lr_model
import seaborn as sns
import load_dataset
from sklearn.feature_selection  import mutual_info_classif

DIR_NAME = 'src/Audio/'


def init_models(data_list, labels_list, randomness, test_size):
    lr_model.train_and_test(data_list, labels_list, randomness, test_size)
    svm_model.train_and_test(data_list, labels_list, randomness, test_size)


#load_dataset.load_data(DIR_NAME)
with open('./data.json', 'r') as f:
    dataset = json.load(f)
data = []
labels = []
for element in dataset:
    array = np.array(list(element['audio_features'].values()))
    data.append(array)
    labels.append(element['covid'])
print('Each element has ' + str(len(dataset[0]['audio_features'])) + ' features\n')
init_models(data_list=data, labels_list=labels, randomness=10, test_size=0.2)

importances = mutual_info_classif(data, labels)
feat_imp = pd.Series(importances, pd.DataFrame(data).columns[0:len(pd.DataFrame(data))-1])
feat_imp.plot(kind='barh')

#plt.yticks(pd.DataFrame(data).columns, dataset[0]['audio_features'].keys(), rotation='horizontal')
#plt.show()

#!=0 per togliere solo quelle inutili
feat_imp = feat_imp[feat_imp > 0.1]
plot_labels_new = []
plot_labels_new.append(list(dataset[0]['audio_features'].keys()))
labels_new=np.array(plot_labels_new)
important_features_indexes = feat_imp.index.tolist()
labels_new = labels_new[0][important_features_indexes]
feat_imp.plot(kind='barh')
plt.yticks(range(len(labels_new)), labels_new, rotation='horizontal')

plt.show()

reduced_data = []
for lista in data:
    nuova_lista = [lista[indice] for indice in important_features_indexes]
    reduced_data.append(nuova_lista)

print("reduced data results")
init_models(data_list=reduced_data, labels_list=labels, randomness=0, test_size=0.2)


