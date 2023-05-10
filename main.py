import os
import json
import numpy as np

import svm_model
import lr_model
import load_dataset

DIR_NAME = 'src/Audio/'

# load_dataset.load_data(DIR_NAME)

with open('./data.json', 'r') as f:
    dataset = json.load(f)
data = []
labels = []
for element in dataset:
    array = np.array(list(element['audio_features'].values()))
    data.append(array)
    labels.append(element['covid'])
print('\nEnd.')
print('Each element has ' + str(len(dataset[0]['audio_features'])) + ' features ')
lr_model.train_and_test(data, labels)
svm_model.train_and_test(data, labels)

