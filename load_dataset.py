import os  # libreria che ci serve per modificare utilizzare directory
import json  # libreria per manipolare file json
import librosa
import numpy as np
import json
import pprint
import re
import sys

import warnings

from scipy.stats import kurtosis, skew


warnings.simplefilter(action='ignore', category=FutureWarning)

directories_names = ['covidandroidnocough', 'covidandroidwithcough', 'asthmaandroidwithcough', 'healthyandroidnosymp',
                     'healthyandroidwithcough']


def extract_features(audio, sr, dir_name, category_name):
    onset_env = librosa.onset.onset_strength(y=audio, sr=sr)

    trim, index = librosa.effects.trim(y=audio)
    duration = librosa.get_duration(y=trim)
    # print('duration', duration)

    # times = librosa.times_like(onset_env, sr=sr)
    onset_frames = librosa.onset.onset_detect(onset_envelope=onset_env, sr=sr)

    # print('onset_frames:', onset_frames)

    tempo = librosa.beat.tempo(onset_envelope=onset_env, sr=sr)
    # print('tempo:', tempo[0])

    period = np.argmax(librosa.stft(audio))
    # print('period:', period)

    rmse = librosa.feature.rms(y=audio)[0]
    rmse_stat = extract_statistical_features(rmse, 'rmse')
    # print('rmse:', np.shape(rmse))

    sc = librosa.feature.spectral_centroid(y=audio)
    sc_stat = extract_statistical_features(sc, 'sc')
    # print('spectral centroid:' + str(np.shape(sc[0])) + ' ' + str(np.shape(sc)))

    roll_off = librosa.feature.spectral_rolloff(y=audio, sr=sr, roll_percent=0.85)
    roll_off_stat = extract_statistical_features(roll_off, 'roll_off')
    # print('roll_off:' + str(np.shape(roll_off[0])) + ' ' + str(np.shape(roll_off)))

    zc = librosa.feature.zero_crossing_rate(y=audio)
    zc_stat = extract_statistical_features(zc, 'zc')
    # print('zero crossing:' + str(np.shape(zc[0])) + ' ' + str(np.shape(zc)))

    # la funzione mfcc restituisce matrici che stenderemo e ne calcoleremo gli indicatori statistici
    mfcc = librosa.feature.mfcc(y=audio, sr=sr)
    mfcc_feat = extract_statistical_features(mfcc, 'mfcc')

    mfcc_delta = librosa.feature.delta(mfcc)
    mfcc_feat_d = extract_statistical_features(mfcc_delta, 'mfcc_d')

    mfcc_delta2 = librosa.feature.delta(mfcc, order=2)
    mfcc_feat_d2 = extract_statistical_features(mfcc_delta2, 'mfcc_d2')

    full_label = get_full_label(dir_name)
    category = get_category(category_name)
    features = {
        #'full_label': full_label,
        #'category': category,
        'duration': float(duration),
        'tempo': float(tempo[0]),
        'period': float(period),
        'onset': len(onset_frames),
        'rmse': rmse_stat,
        'sc': sc_stat,
        'roll_off': roll_off_stat,
        'zc': zc_stat,
        'mfcc': mfcc_feat,
        'mfcc_d': mfcc_feat_d,
        'mfcc_d2': mfcc_feat_d2,
    }

    # This piece of code expand these arrays from
    # 'name': { 'stat_1': stat_1, ..., 'stat_n': stat_n }
    # to
    # 'name_stat_1': stat_1, ...,'name_stat_n': stat_n
    for name in ['rmse', 'sc', 'roll_off', 'zc']:
        for key, value in features[name].items():
            # Split the original key name into separate parts
            parts = re.findall(r'[a-zA-Z]+|\d+', key)
            # Build the new key name by joining the parts with underscores
            new_key = "_".join([name] + parts)
            # Add the new key and value to the output dictionary
            features[new_key] = value
        del features[name]

    # This code perform the flattening of the mfcc-like matrices
    for name in ['mfcc', 'mfcc_d', 'mfcc_d2']:
        for i, element in enumerate(features[name]):
            for key in element:
                new_key = name+'_'+str(i)+'_'+key
                features[new_key] = element[key]
        del features[name]

    return features


def extract_statistical_features(vec, name='None'):
    # prendiamo i primi 13 array e per ogni variante di mfcc
    if name == 'mfcc' or name == 'mfcc_d' or name == 'mfcc_d2':
        vec_features = []
        # ne calcoliamo gli indicatori statistici
        for i, array in enumerate(vec[0:13]):
            # scarto interquartile
            vec_features.append(statistic_obj(array))
        return vec_features
    else:
        return statistic_obj(vec)


def statistic_obj(array):
    q3, q1 = np.percentile(array, [75, 25])
    return dict({
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
    })


def is_covid(dir_name):
    if dir_name.find('covid') != -1:
        return 1
    else:
        return 0


def get_mel_spect(audio, sr, n_mel):
    mel_d = librosa.feature.melspectrogram(y=audio, sr=sr, n_mels=n_mel)
    mel_spect = librosa.power_to_db(mel_d, ref=np.max)
    return mel_spect


def get_category(category_name):
    if category_name == 'breath':
        return 0
    else:
        return 1


def get_full_label(name):
    if name == 'covidandroidnocough':
        return 1
    if name == 'covidandroidwithcough':
        return 2
    if name == 'asthmaandroidwithcough':
        return 3
    if name == 'healthyandroidnosymp':
        return 4
    if name == 'healthyandroidwithcough':
        return 5


def load_data(parent_directory):
    with open(parent_directory + 'files.json', 'r') as f:
        file_dict = json.load(f)

    dataset = []
    for k, dir_name in enumerate(directories_names):
        print('\nLoading... ' + str(k+1) + '/' + str(len(directories_names)))
        for i, filelist in enumerate(file_dict[dir_name]):
            sys.stdout.write('\rElement ' + str(i+1) + '/' + str(len(file_dict[dir_name])))
            sys.stdout.flush()
            # Get covid label (1 o 0)
            covid = is_covid(dir_name)
            # BREATH
            audio_breath, breath_sr = librosa.core.load(parent_directory + dir_name + '/breath/' + filelist[0])
            audio_breath, _ = librosa.effects.trim(audio_breath)

            dataset.append({
                'filename': filelist[0],
                'covid': covid,
                'audio_features': extract_features(audio_breath, breath_sr, dir_name, 'breath'),
            })

            # Calcola spettrogramma di Mel
            # mel_breath = get_mel_spect(audio_breath, sr, n_mel=128)

            # COUGH
            audio_cough, cough_sr = librosa.core.load(parent_directory + dir_name + '/cough/' + filelist[1])
            audio_cough, _ = librosa.effects.trim(audio_cough)

            dataset.append({
                'filename': filelist[1],
                'covid': covid,
                'audio_features': extract_features(audio_cough, cough_sr, dir_name, 'cough'),
            })

            # Calcola la STFT e il valore assoluto degli spettri di potenza
            # stft_cough = get_stft_spec(audio_cough)

            # Calcola spettrogramma di Mel
            # mel_cough = get_mel_spect(audio_cough, sr, n_mel=128)
    pp = pprint.PrettyPrinter(indent=4)
    # pp.pprint(dataset)

    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(dataset, f, ensure_ascii=False, indent=4)
