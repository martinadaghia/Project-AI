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
NUM_FEATURES = 600
# NUMBER OF TESTS TO RUN
NUM_TESTS = 50
# SEED FOR SPLITTING
# TOP SEEDS: 10 0
SEED = 1


PERCENT = 25


def print_mean_report(results, model):
    # Inizializza i risultati
    precision_list = []
    recall_list = []
    f1_score_list = []

    # Calcola le metriche per ciascun report
    for report in results:
        report_dict = report["1"]
        precision_list.append(report_dict['precision'])
        recall_list.append(report_dict['recall'])
        f1_score_list.append(report_dict['f1-score'])

    # Calcola la media delle metriche
    mean_precision = np.mean(precision_list)
    mean_recall = np.mean(recall_list)
    mean_f1_score = np.mean(f1_score_list)
    print('Mean Precision '+model+': %.2f' % mean_precision)
    print('Mean Recall '+model+': %.2f' % mean_recall)
    print('Mean F1-score '+model+': %.2f' % mean_f1_score)


def print_report(report, model):
    print(model + '\n' + report)


def init_models(data_list, labels_list, randomness, test_size, threshold, seed):
    lr_report, lr_mtx = lr_model.train_and_test(data_list, labels_list, randomness, test_size, threshold, seed, False)
    svm_report, svm_mtx = svm_model.train_and_test(data_list, labels_list, randomness, test_size, threshold, seed, False)

    print_report(lr_report, 'LR')
    print_report(svm_report, 'SVM')

    lr_confusion_df = pd.DataFrame(lr_mtx, index=['Actual 0', 'Actual 1'], columns=['Predicted 0', 'Predicted 1'])
    # Creazione della heatmap della matrice di confusione
    plt.figure(figsize=(8, 6))
    sns.heatmap(lr_confusion_df, annot=True, fmt='d', cmap='Blues')
    plt.title('Matrice di Confusione LR')
    plt.xlabel('Valore Predetto')
    plt.ylabel('Valore Effettivo')

    svm_confusion_df = pd.DataFrame(svm_mtx, index=['Actual 0', 'Actual 1'], columns=['Predicted 0', 'Predicted 1'])
    # Creazione della heatmap della matrice di confusione
    plt.figure(figsize=(8, 6))
    sns.heatmap(svm_confusion_df, annot=True, fmt='d', cmap='Blues')
    plt.title('Matrice di Confusione SVM')
    plt.xlabel('Valore Predetto')
    plt.ylabel('Valore Effettivo')
    plt.show()


def init_models_iter(data_list, labels_list, randomness, test_size, threshold):
    lr_results = []
    svm_results = []
    lr_aggregated_confusion_mtx = np.zeros_like([[0, 0], [0, 0]])
    svm_aggregated_confusion_mtx = np.zeros_like([[0, 0], [0, 0]])

    for _ in range(NUM_TESTS):
        # Esegui il test di regressione logistica
        lr_result, lr_mtx = lr_model.train_and_test(data_list, labels_list, randomness, test_size, threshold, True)
        lr_results.append(lr_result)
        lr_aggregated_confusion_mtx += lr_mtx

        # Esegui il test di SVM
        svm_result, svm_mtx = svm_model.train_and_test(data_list, labels_list, randomness, test_size, threshold, True)
        svm_results.append(svm_result)
        svm_aggregated_confusion_mtx += svm_mtx

    # Stampa la media dei risultati
    print_mean_report(lr_results, 'LR')
    print_mean_report(svm_results, 'SVM')

    lr_avg_cnf_mtx = lr_aggregated_confusion_mtx / NUM_TESTS
    lr_confusion_df = pd.DataFrame(lr_avg_cnf_mtx, index=['Actual 0', 'Actual 1'], columns=['Predicted 0', 'Predicted 1'])

    # Creazione della heatmap della matrice di confusione
    plt.figure(figsize=(8, 6))
    sns.heatmap(lr_confusion_df, annot=True, fmt='.2f', cmap='Blues')
    plt.title('Matrice di Confusione LR')
    plt.xlabel('Valore Predetto')
    plt.ylabel('Valore Effettivo')

    svm_avg_cnf_mtx = svm_aggregated_confusion_mtx / NUM_TESTS
    svm_confusion_df = pd.DataFrame(svm_avg_cnf_mtx, index=['Actual 0', 'Actual 1'], columns=['Predicted 0', 'Predicted 1'])

    # Creazione della heatmap della matrice di confusione
    plt.figure(figsize=(8, 6))
    sns.heatmap(svm_confusion_df, annot=True, fmt='.2f', cmap='Blues')
    plt.title('Matrice di Confusione SVM')
    plt.xlabel('Valore Predetto')
    plt.ylabel('Valore Effettivo')
    plt.show()


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
# plt.show()

reduced_data = []
for element_features in data:
    element_new_features = [element_features[index] for index in important_features_indexes]
    reduced_data.append(element_new_features)
# sns.boxplot(reduced_data[: 5])
print("Reduced data results")
init_models(data_list=reduced_data, labels_list=labels, randomness=0, test_size=0.2, threshold=THRESHOLD, seed=SEED)


