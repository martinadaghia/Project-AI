import os  # libreria che ci serve per modificare utilizzare directory
import json  # libreria per manipolare file json
import librosa
import matplotlib.pyplot as plt
import numpy as np
import json
import pprint

from scipy.stats import kurtosis, skew

directories_names = ['covidandroidnocough', 'covidandroidwithcough', 'asthmaandroidwithcough', 'healthyandroidnosymp', 'healthyandroidwithcough']

DIR_NAME = 'src/Test/'


def extract_features(audio, sr):
    onset_env = librosa.onset.onset_strength(y=audio, sr=sr)

    duration = librosa.get_duration(y=audio)
    print('duration', duration)

    times = librosa.times_like(onset_env, sr=sr)
    onset_frames = librosa.onset.onset_detect(onset_envelope=onset_env, sr=sr)
    print('onset_frames:', onset_frames)

    tempo = librosa.beat.tempo(onset_envelope=onset_env, sr=sr)
    print('tempo:', tempo[0])

    period = np.argmax(librosa.stft(audio))
    print('period:', period)

    rmse = librosa.feature.rms(y=audio)[0]
    print('rmse:', rmse)

    sc = librosa.feature.spectral_centroid(y=audio)
    print('spectral centroid:', sc[0])

    rolloff = librosa.feature.spectral_rolloff(y=audio, sr=sr, roll_percent=0.85)
    print('rolloff:', rolloff[0])

    zc = librosa.feature.zero_crossing_rate(y=audio)
    print('zero crossing:', zc[0])

    mfcc = librosa.feature.mfcc(y=audio, sr=sr)
    mfcc_delta = librosa.feature.delta(mfcc)
    mfcc_delta2 = librosa.feature.delta(mfcc, order=2)
    print('mfcc length', np.shape(len(mfcc)) + ' is ' + str(mfcc) + ' each component is long: ' + str(len(mfcc[0])))
    print('mfcc_delta:', np.shape(mfcc_delta))
    print('mfcc_delta2:', np.shape(mfcc_delta2))

    # return {
    #     'mean': str(np.mean(array)),
    #     'std_dev': str(np.std(array)),
    #     'min': str(np.min(array)),
    #     'max': str(np.max(array)),
    #     'e_norm': str(np.linalg.norm(array)),
    #     'median': str(np.median(array)),
    #     'skew': str(skew(array, axis=None)),
    #     'kurt': str(kurtosis(array, axis=None)),
    #     'perc25': str(np.percentile(array, 25)),
    #     'perc75': str(np.percentile(array, 75))
    # }


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
    with open(DIR_NAME + 'files.json', 'r') as f:
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
            audio_breath, breath_sr = librosa.core.load(DIR_NAME + dir_name + '/breath/' + filelist[0])
            audio_breath, _ = librosa.effects.trim(audio_breath)

            dataset_val[dir_name]['breath'].append({
                'filename': filelist[0],
                'covid': covid,
                # 'stft': extract_features(stft_breath),
                'audio_features': extract_features(audio_breath, breath_sr),
            })

            # Calcola la STFT e il valore assoluto degli spettri di potenza
            #stft_breath = get_stft_spec(audio_breath)

            # Calcola spettrogramma di Mel
            #mel_breath = get_mel_spect(audio_breath, sr, n_mel=128)

            # COUGH
            audio_cough, cough_sr = librosa.core.load(DIR_NAME + dir_name + '/cough/' + filelist[1])
            audio_cough, _ = librosa.effects.trim(audio_cough)

            dataset_val[dir_name]['cough'].append({
                'filename': filelist[1],
                'covid': covid,
                # 'stft': extract_features(stft_cough),
                'audio_features': extract_features(audio_cough, cough_sr),
            })

            # Calcola la STFT e il valore assoluto degli spettri di potenza
            #stft_cough = get_stft_spec(audio_cough)

            # Calcola spettrogramma di Mel
            #mel_cough = get_mel_spect(audio_cough, sr, n_mel=128)

    # pp = pprint.PrettyPrinter(indent=4)
    # pp.pprint(dataset_val)
    dict_ = dict(dataset_val)
    json_ = json.dumps(dict_, indent=4)
    # print('json', json_)

    # SCATENA L'INFERNO:
    #plot(dict_)
    #plt.show()

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
