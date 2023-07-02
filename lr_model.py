import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


def train_and_test(data, labels, randomness, test_size, threshold, seed, dict):
    # Crea un'istanza del trasformatore e adattalo ai dati
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)

    # Dividi i dati in set di addestramento e di test
    x_train, x_test, y_train, y_test = train_test_split(scaled_data, labels, test_size=test_size, stratify=labels, random_state=seed)

    # Crea e addestra il modello di regressione logistica
    model = LogisticRegression(random_state=randomness, max_iter=10000000000)
    model.fit(x_train, y_train)

    # Effettua le previsioni sul set di test
    y_pred_proba = model.predict_proba(x_test)
    y_pred = np.where(y_pred_proba[:, 1] > threshold, 1, 0)
    # Valuta le prestazioni del modello
    # accuracy_lr = accuracy_score(y_test, y_pred) * 100
    # print('LR Accuracy: %.2f' % accuracy_lr + '%\n')
    # print('LR')
    # Calcola il classification report
    report = classification_report(y_test, y_pred, output_dict=dict)

    # print(report)

    # Calcola la matrice di confusione
    confusion_mtx = confusion_matrix(y_test, y_pred)
    # Creazione di un dataframe dalla matrice di confusione
    confusion_df = pd.DataFrame(confusion_mtx, index=['Actual 0', 'Actual 1'], columns=['Predicted 0', 'Predicted 1'])

    # Creazione della heatmap della matrice di confusione
    # plt.figure(figsize=(8, 6))
    # sns.heatmap(confusion_df, annot=True, fmt='d', cmap='Blues')
    # plt.title('Matrice di Confusione LR')
    # plt.xlabel('Valore Predetto')
    # plt.ylabel('Valore Effettivo')
    # plt.show()
    return report, confusion_mtx

