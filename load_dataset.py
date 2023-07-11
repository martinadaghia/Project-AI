import json
import librosa
import numpy as np
import re
import sys
import warnings
from scipy.stats import kurtosis, skew

warnings.simplefilter(action='ignore', category=FutureWarning)

# definizione dei nomi delle directory
directories_names = [
    'covidandroidnocough',
    'covidandroidwithcough',
    'asthmaandroidwithcough',
    'healthyandroidnosymp',
    'healthyandroidwithcough'
]

def extract_features(audio, sr, dir_name, category_name):
    # calcola l'envelope di onset
    onset_env = librosa.onset.onset_strength(y=audio, sr=sr)
    trim, index = librosa.effects.trim(y=audio)
    duration = librosa.get_duration(y=trim)
    # rileva i frame di onset
    onset_frames = librosa.onset.onset_detect(onset_envelope=onset_env, sr=sr)
    # calcola il tempo di beat
    tempo = librosa.beat.tempo(onset_envelope=onset_env, sr=sr)
    # trova il periodo dominante
    period = np.argmax(librosa.stft(audio))
    # calcola la radice del mean square energy (RMSE)
    rmse = librosa.feature.rms(y=audio)[0]
    rmse_stat = extract_statistical_features(rmse, 'rmse')
    # calcola il centroide spettrale
    sc = librosa.feature.spectral_centroid(y=audio)
    sc_stat = extract_statistical_features(sc, 'sc')
    # calcola il roll-off spettrale
    roll_off = librosa.feature.spectral_rolloff(y=audio, sr=sr, roll_percent=0.85)
    roll_off_stat = extract_statistical_features(roll_off, 'roll_off')

    zc = librosa.feature.zero_crossing_rate(y=audio)
    zc_stat = extract_statistical_features(zc, 'zc')

    # calcola le features MFCC
    mfcc = librosa.feature.mfcc(y=audio, sr=sr)
    mfcc_feat = extract_statistical_features(mfcc, 'mfcc')

    # calcola le features delta delle MFCC
    mfcc_delta = librosa.feature.delta(mfcc)
    mfcc_feat_d = extract_statistical_features(mfcc_delta, 'mfcc_d')

    # calcola le features delta2 delle MFCC
    mfcc_delta2 = librosa.feature.delta(mfcc, order=2)
    mfcc_feat_d2 = extract_statistical_features(mfcc_delta2, 'mfcc_d2')

    features = {
        category_name + 'duration': float(duration),  # durata dell'audio
        category_name + 'tempo': float(tempo[0]),  # tempo dell'audio
        category_name + 'period': float(period),  # periodo dell'audio
        category_name + 'onset': len(onset_frames),  # numero di onset rilevati
        category_name + 'rmse': rmse_stat,  # statistiche sul valore RMSE
        category_name + 'sc': sc_stat,  # statistiche sul centroide spettrale
        category_name + 'roll_off': roll_off_stat,  # statistiche sul roll-off spettrale
        category_name + 'zc': zc_stat,  # statistiche sul zero crossing rate
        category_name + 'mfcc': mfcc_feat,  # statistiche sulle MFCC
        category_name + 'mfcc_d': mfcc_feat_d,  # statistiche sulle MFCC delta
        category_name + 'mfcc_d2': mfcc_feat_d2,  # statistiche sulle MFCC delta2
    }

    # rinomina le chiavi per includere il nome della categoria
    for name in [category_name + 'rmse', category_name + 'sc', category_name + 'roll_off', category_name + 'zc']:
        for key, value in features[name].items():
            parts = re.findall(r'[a-zA-Z]+|\d+', key)
            new_key = "_".join([name] + parts)
            features[new_key] = value
        del features[name]

    # rinomina le chiavi dei coefficienti MFCC per includere l'indice e il nome della categoria
    for name in [category_name + 'mfcc', category_name + 'mfcc_d', category_name + 'mfcc_d2']:
        for i, element in enumerate(features[name]):
            for key in element:
                new_key = name + '_' + str(i) + '_' + key
                features[new_key] = element[key]
        del features[name]

    return features

def extract_statistical_features(vec, name='None'):
    if name == 'mfcc' or name == 'mfcc_d' or name == 'mfcc_d2':
        vec_features = []
        # calcola gli indicatori statistici per i primi 13 array appartenenti alle matrici "mfcc"
        for i, array in enumerate(vec[0:13]):
            # per ogni vettore dei 13 di mfcc ne calcola i valori statistici della funzione sottostante
            vec_features.append(statistic_obj(array))
        return vec_features
    else:
        return statistic_obj(vec)


def statistic_obj(array):
    # calcola i valori statistici dell'array
    q3, q1 = np.percentile(array, [75, 25])
    return {
        'mean': float(np.mean(array)),
        'std_dev': float(np.std(array)),
        'min': float(np.min(array)),
        'max': float(np.max(array)),
        'median': float(np.median(array)),
        'skew': float(skew(array, axis=None)),
        'kurt': float(kurtosis(array, axis=None)),
        'perc25': float(q1),
        'perc75': float(q3),
        'root_mean_sqr': float(np.sqrt(np.mean(array ** 2))),
        'iqr': float(q3 - q1)
    }


def is_covid(dir_name):
    # controlla se la directory contiene la parola "covid"
    return 1 if dir_name.find('covid') != -1 else 0


def get_mel_spect(audio, sr, n_mel):
    # calcola lo spettrogramma di Mel
    mel_d = librosa.feature.melspectrogram(y=audio, sr=sr, n_mels=n_mel)
    mel_spect = librosa.power_to_db(mel_d, ref=np.max)
    return mel_spect


def get_category(category_name):
    # converte il nome della categoria in un valore numerico
    return 0 if category_name == 'breath' else 1


def get_full_label(name):
    # restituisce l'etichetta completa in base al nome della directory
    labels = {
        'covidandroidnocough': 1,
        'covidandroidwithcough': 2,
        'asthmaandroidwithcough': 3,
        'healthyandroidnosymp': 4,
        'healthyandroidwithcough': 5
    }
    return labels.get(name, None)


def load_data(parent_directory):
    # carica il file JSON con i dati dei file
    with open(parent_directory + 'files.json', 'r') as f:
        file_dict = json.load(f)

    dataset = []
    for k, dir_name in enumerate(directories_names):
        # stampa il progresso del caricamento delle directory
        print('\nLoading... ' + str(k + 1) + '/' + str(len(directories_names)))
        for i, filelist in enumerate(file_dict[dir_name]):
            # stampa il progresso del caricamento dei file all'interno di una directory
            sys.stdout.write('\rElement ' + str(i + 1) + '/' + str(len(file_dict[dir_name])))
            sys.stdout.flush()

            # determina se il file è relativo a un caso di COVID
            covid = is_covid(dir_name)

            # carica l'audio del respiro
            audio_breath, breath_sr = librosa.core.load(parent_directory + dir_name + '/breath/' + filelist[0])
            audio_breath, _ = librosa.effects.trim(audio_breath)
            # estrai le caratteristiche audio del respiro
            breath_features = extract_features(audio_breath, breath_sr, dir_name, 'breath_')

            # carica l'audio della tosse
            audio_cough, cough_sr = librosa.core.load(parent_directory + dir_name + '/cough/' + filelist[1])
            audio_cough, _ = librosa.effects.trim(audio_cough)
            # estrai le caratteristiche audio della tosse
            cough_features = extract_features(audio_cough, cough_sr, dir_name, 'cough_')

            # unisce le caratteristiche audio del respiro e della tosse
            cough_and_breath = breath_features | cough_features

            # aggiunge i dati al dataset
            dataset.append({
                'filename_breath': filelist[0],
                'filename_cough': filelist[1],
                'covid': covid,
                'audio_features': cough_and_breath
            })

    # salva il dataset nel file json data.json
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(dataset, f, ensure_ascii=False, indent=4)
