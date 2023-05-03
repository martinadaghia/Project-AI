import os  # libreria che ci serve per modificare utilizzare directory
import json  # libreria per manipolare file json
import librosa
import matplotlib.pyplot as plt
import numpy as np
import json
import pprint

from scipy.stats import kurtosis, skew

directories_names = ['covidandroidnocough', 'covidandroidwithcough', 'asthmaandroidwithcough', 'healthyandroidnosymp', 'healthyandroidwithcough']


def extract_features(array, data_type):
    # Normalizzazione dell'array fra -1 e 1.
    # da decide se positiva/inifluente/utile/ecc
    # array = 2 * (array - np.min(array)) / (np.max(array) - np.min(array)) - 1
    if data_type == 'mfcc':
        return (

        )

    elif data_type == 'stft':
        return (

        )

    else data_type == 'mel':
        return {
            'mean': str(np.mean(array)),
            'std_dev': str(np.std(array)),
            'min': str(np.min(array)),
            'max': str(np.max(array)),
            'e_norm': str(np.linalg.norm(array)),
            'median': str(np.median(array)),
            'skew': str(skew(array, axis=None)),
            'kurt': str(kurtosis(array, axis=None)),
            'perc25': str(np.percentile(array, 25)),
            'perc75': str(np.percentile(array, 75))
        }


def is_covid(dir_name):
    if dir_name.find('covid') != -1:
        return 1
    else:
        return 0


def get_mel_spect(audio, sr, n_mel):
    mel_d = librosa.feature.melspectrogram(y=audio, sr=sr, n_mels=n_mel)
    mel_spect = librosa.power_to_db(mel_d, ref=np.max)
    return mel_spect


def get_stft_spec(audio):
    stft_d = librosa.stft(audio)
    stft_spect = librosa.amplitude_to_db(np.abs(stft_d), ref=np.max)
    return stft_spect


def get_mfcc_spec(audio, sr):
    return librosa.feature.mfcc(audio, sr)


def load_data():
    with open('src/Test/files.json', 'r') as f:
        file_dict = json.load(f)

    dataset_val = {}
    for dir_name in directories_names:
        dataset_val[dir_name] = {
            'cough': [],
            'breath': []
        }
        for filelist in file_dict[dir_name]:
            # Get covid label (1 o 0)
            covid = is_covid(dir_name)

            # BREATH
            audio_breath, sr = librosa.core.load('src/Test/' + dir_name + '/breath/' + filelist[0])

            # Calcola la STFT e il valore assoluto degli spettri di potenza
            stft_breath = get_stft_spec(audio_breath)

            # Calcola spettrogramma di Mel
            mel_breath = get_mel_spect(audio_breath, sr, n_mel=128)

            # COUGH
            audio_cough, sr = librosa.core.load('src/Test/' + dir_name + '/cough/' + filelist[1])

            # Calcola la STFT e il valore assoluto degli spettri di potenza
            stft_cough = get_stft_spec(audio_cough)

            # Calcola spettrogramma di Mel
            mel_cough = get_mel_spect(audio_cough, sr, n_mel=128)

            dataset_val[dir_name]['breath'].append({
                'filename': filelist[0],
                'covid': covid,
                'stft': extract_features(stft_breath),
                'mel': extract_features(mel_breath),
            })
            dataset_val[dir_name]['cough'].append({
                'filename': filelist[1],
                'covid': covid,
                'stft': extract_features(stft_cough),
                'mel': extract_features(mel_cough),
            })

    # pp = pprint.PrettyPrinter(indent=4)
    # pp.pprint(dataset_val)
    dict_ = dict(dataset_val)
    json_ = json.dumps(dict_, indent=4)
    print('json', json_)
    # SCATENA L'INFERNO:
    plot(dict_)
    plt.show()

    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(dict(dataset_val), f, ensure_ascii=False, indent=4)


def plot(dict_):
    features_names = ['mean', 'std_dev', 'min', 'max', 'e_norm', 'median', 'skew', 'kurt', 'perc25', 'perc75']
    i = 0
    for feature in features_names:
        covid = []
        nocovid = []
        i = i+1
        for ctg in directories_names:
            for el in dict_[ctg]['cough']:
                if float(el['covid']) == 1:
                    covid.append(float(el['stft'][feature]))
                    nocovid.append(float(0))
                else:
                    nocovid.append(float(el['stft'][feature]))
                    covid.append(float(0))
        plt.figure(i)
        plt.plot(list(range(1, 11)), covid, 'ro')
        plt.plot(list(range(1, 11)), nocovid, 'bo')
        plt.title(feature)


load_data()

#bisogna vedere come performa il modello con le feauture nuove ma soprattutto bisogna capire come dare al nostro modello non dei valori scalari che definiscono vettori #bensì dei vettori stessi. In primis bisogna prendere i primi 13 array della funzione mfcc e poi calcolarne (per questi 13 vettori) i 10 valori statistici: 'mean', #'std_dev', #'min', 'max', 'e_norm', 'median', 'skew', 'kurt', 'perc25', 'perc75'.  
# fatto questo dovremmo avere abbastanza features rilevanti per avere una giusta quantità di dati per ricavare la nostra ipotesi e capire ulteriori cose.
#STAY TUNED HOES!
