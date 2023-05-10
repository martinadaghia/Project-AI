from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def train_and_test(data, labels, randomness, test_size):
    # Divisione dei dati in set di addestramento e di test
    x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size=test_size)

    # Training SVM
    clf = svm.SVC(random_state=randomness)
    clf.fit(x_train, y_train)

    # Effettua le previsioni sul set di test
    y_pred = clf.predict(x_test)

    # Valuta le prestazioni del modello
    accuracy_svm = accuracy_score(y_test, y_pred)
    print('SVM Accuracy:', accuracy_svm)
