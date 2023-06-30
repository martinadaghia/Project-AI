from sklearn.preprocessing import StandardScaler
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


def train_and_test(data, labels, randomness, test_size):
    # Crea un'istanza del trasformatore e adattalo ai dati
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)

    # Divisione dei dati in set di addestramento e di test
    x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size=test_size)

    # Training SVM
    clf = svm.SVC(random_state=randomness)
    clf.fit(x_train, y_train)

    # Effettua le previsioni sul set di test
    y_pred = clf.predict(x_test)



    # Valuta le prestazioni del modello
    #accuracy_svm = accuracy_score(y_test, y_pred) * 100
    #print('SVM Accuracy: %.2f' % accuracy_svm + '%\n')
    print('SVM')
    # Calcola il classification report
    report = classification_report(y_test, y_pred)
    print(report)

    #print(str(np.floor(np.mean(y_test) * 100)) + '% of ones in y_test')
    # Calcola la matrice di confusione
    confusion_mtx = confusion_matrix(y_test, y_pred)
    # Creazione di un dataframe dalla matrice di confusione
    confusion_df = pd.DataFrame(confusion_mtx, index=['Actual 0', 'Actual 1'], columns=['Predicted 0', 'Predicted 1'])

    # Creazione della heatmap della matrice di confusione
    plt.figure(figsize=(8, 6))
    sns.heatmap(confusion_df, annot=True, fmt='d', cmap='Blues')
    plt.title('Matrice di Confusione SVG')
    plt.xlabel('Valore Predetto')
    plt.ylabel('Valore Effettivo')
    plt.show()