import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from keras.models import Sequential
from keras.layers import Dense

class NeuralNetworkModel:
    def __init__(self, input_dim, hidden_units, output_units, activation='relu', optimizer='adam', epochs=15, batch_size=10):
        self.input_dim = input_dim
        self.hidden_units = hidden_units
        self.output_units = output_units
        self.activation = activation
        self.optimizer = optimizer
        self.epochs = epochs
        self.batch_size = batch_size
        self.model = self.build_model()

    def build_model(self):
        model = Sequential()
        model.add(Dense(self.hidden_units, input_dim=self.input_dim, activation=self.activation))
        model.add(Dense(self.output_units, activation='sigmoid'))
        model.compile(loss='binary_crossentropy', optimizer=self.optimizer, metrics=['accuracy'])
        return model

    def prepare_data(self, X, y):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        scaler = StandardScaler()
        X_train = scaler.fit_transform(X_train)
        X_test = scaler.transform(X_test)
        return X_train, X_test, y_train, y_test

    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train, epochs=self.epochs, batch_size=self.batch_size, verbose=2)

    def inference(self, X):
        return self.model.predict(X)

file_path = "data.txt"
df = pd.read_csv(file_path, header=None)

X = df.iloc[:, :-1]
y = df.iloc[:, -1]

nn_model = NeuralNetworkModel(input_dim=X.shape[1], hidden_units=12, output_units=1, epochs=15, batch_size=10)

X_train, X_test, y_train, y_test = nn_model.prepare_data(X, y)

nn_model.train(X_train, y_train)

predictions = nn_model.inference(X_test[:3])
print(predictions)
