from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


def train_and_test(data, labels, randomness, test_size):
    # Crea un'istanza del trasformatore e adattalo ai dati
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)

    # Dividi i dati in set di addestramento e di test
    x_train, x_test, y_train, y_test = train_test_split(scaled_data, labels, test_size=test_size)

    # Crea e addestra il modello di regressione logistica
    model = LogisticRegression(random_state=randomness)
    model.fit(x_train, y_train)

    # Effettua le previsioni sul set di test
    y_pred = model.predict(x_test)

    # Valuta le prestazioni del modello
    accuracy_lr = accuracy_score(y_test, y_pred) * 100
    print('LR Accuracy: %.2f' % accuracy_lr + '%\n')


