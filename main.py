import json

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.feature_selection import mutual_info_classif

import lr_model
import svm_model

DIR_NAME = 'src/Audio/'

# IS COVID PROBABILITY THRESHOLD
THRESHOLD = 0.10
# NUMBER OF TOP FEATURES TO SELECT
NUM_FEATURES = 600
# NUMBER OF TESTS TO RUN
NUM_TESTS = 50
# SEED FOR SPLITTING
SEED = 592

PERCENT = 25

def print_report(report, model):
    print(model + '\n' + report)

def init_models(data_list, labels_list, randomness, test_size, threshold, seed):
    sns.set(rc={'figure.figsize': (11.7, 8.27)})
    print("start " + str(int(THRESHOLD % 0.1)+1))
    # aumenta il threshold di 0.10 per ogni ciclo di for
    for i in range(0, 3):
        actual_threshold = threshold + ((i-1)*0.1)
        print("Trying with " + str(actual_threshold) + " tolerance")
        lr_report, lr_mtx = lr_model.train_and_test(data_list, labels_list, randomness, test_size, actual_threshold, seed, False)
        svm_report, svm_mtx = svm_model.train_and_test(data_list, labels_list, randomness, test_size, actual_threshold, seed, False)

        print_report(lr_report, 'LR')
        print_report(svm_report, 'SVM')

        lr_confusion_df = pd.DataFrame(lr_mtx, index=['Actual 0', 'Actual 1'], columns=['Predicted 0', 'Predicted 1'])
        # Creazione della heatmap della matrice di confusione
        plt.figure(figsize=(8, 6))
        sns.heatmap(lr_confusion_df, annot=True, fmt='d', cmap='Blues')
        plt.title('Matrice di Confusione LR threshold ' + str(int(actual_threshold*100)) + '%')
        plt.xlabel('Valore Predetto')
        plt.ylabel('Valore Effettivo')

        svm_confusion_df = pd.DataFrame(svm_mtx, index=['Actual 0', 'Actual 1'], columns=['Predicted 0', 'Predicted 1'])
        # Creazione della heatmap della matrice di confusione
        plt.figure(figsize=(8, 6))
        sns.heatmap(svm_confusion_df, annot=True, fmt='d', cmap='Blues')
        plt.title('Matrice di Confusione SVM threshold ' + str(actual_threshold))
        plt.xlabel('Valore Predetto')
        plt.ylabel('Valore Effettivo')
#       plt.show()


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
# modello senza laselezione delle features
# init_models(data_list=data, labels_list=labels, randomness=10, test_size=0.2, threshold=THRESHOLD)

# calcolo delle features con più peso
pesi_features = mutual_info_classif(data, labels)
selected_features = pd.Series(pesi_features, pd.DataFrame(data).columns)

# feat_imp.plot(kind='barh')
# plt.yticks(pd.DataFrame(data).columns, dataset[0]['audio_features'].keys(), rotation='horizontal')
# plt.show()

# ottieni gli indici degli elementi in ordine decrescente di importanza
indices = np.argsort(selected_features)[::-1]

# seleziona i primi NUM_FEATURES indici
top_indices = indices[:NUM_FEATURES]

# aggiornamento delle features con quelle selezionate migliori
selected_features = selected_features[top_indices]
print("Valore minimo importanza feature:", selected_features.min())

# Plot delle features migliori
plot_labels_new = [list(dataset[0]['audio_features'].keys())]
labels_new = np.array(plot_labels_new)
important_features_indexes = selected_features.index.tolist()
labels_new = labels_new[0][important_features_indexes]
selected_features.plot(kind='barh')
plt.yticks(range(len(labels_new)), labels_new, rotation='horizontal')
# plt.show()

reduced_data = []
for element_features in data:
    element_new_features = [element_features[index] for index in important_features_indexes]
    reduced_data.append(element_new_features)
# sns.boxplot(reduced_data[: 5])
print("Reduced data results")

init_models(data_list=reduced_data, labels_list=labels, randomness=0, test_size=0.2, threshold=THRESHOLD, seed=SEED)


