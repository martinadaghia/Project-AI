from sklearn.preprocessing import StandardScaler
from sklearn import svm
from sklearn.model_selection import train_test_split
import numpy as np
from codecarbon import track_emissions
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report


@track_emissions()
def train_and_test(data, labels, randomness, test_size, threshold, seed, dict):
    # Crea un'istanza del trasformatore e adattalo ai dati
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)

    # Divisione dei dati in set di addestramento e di test
    x_train, x_test, y_train, y_test = train_test_split(scaled_data, labels, test_size=test_size, stratify=labels, random_state=seed)

    # Training SVM
    clf = svm.SVC(probability=True, random_state=randomness)
    clf.fit(x_train, y_train)

    # Effettua le previsioni sul set di test
    y_pred_proba = clf.predict_proba(x_test)
    # print(y_pred_proba)
    y_pred = np.where(y_pred_proba[:, 1] > threshold, 1, 0)

    # Calcola il classification report
    report = classification_report(y_test, y_pred, output_dict=dict)
    # print(report)

    # Calcola la matrice di confusione
    confusion_mtx = confusion_matrix(y_test, y_pred)

    return report, confusion_mtx
