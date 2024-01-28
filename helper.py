import joblib
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
import re
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import pandas as pd
from zipfile import ZipFile
import numpy as np

alay_df = pd.read_csv(r'data/new_kamusalay.csv',
                      encoding='latin-1', header=None)
alay_df = alay_df.rename(columns={0: 'alay', 1: 'normalize'})

stopword_df = pd.read_csv(r'data/stopwordbahasa.csv', header=None)
stopword_df = stopword_df.rename(columns={0: 'stopword'})

kamus_alay_map = dict(zip(alay_df['alay'], alay_df['normalize']))
factory = StemmerFactory()
stemmer = factory.create_stemmer()

model = tf.keras.models.load_model(r"model/main_model", compile=False)
model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])
tokenizer = joblib.load(r"model/tokenizer.joblib")


def huruf_kecil(teks):
    return teks.lower()


def hilangkan_karakter_tidak_perlu(teks):
    teks = re.sub(
        r'\n|rt|user|((www.[^\s]+)|(https?://[^\s]+)|(http?://[^\s]+))| +|[^0-9a-zA-Z]+', ' ', teks)
    return teks


def normalisasi_alay(teks):
    return ' '.join([kamus_alay_map[kata] if kata in kamus_alay_map else kata for kata in teks.split(' ')])


def stemming(teks):
    return stemmer.stem(teks)


def hilangkan_stopword(teks):
    teks = ' '.join(
        ['' if kata in stopword_df.stopword.values else kata for kata in teks.split(' ')])
    teks = re.sub(' +', ' ', teks)
    teks = teks.strip()
    return teks


def preprocess(teks):
    teks = huruf_kecil(teks)  # 1
    teks = hilangkan_karakter_tidak_perlu(teks)  # 2
    teks = normalisasi_alay(teks)  # 3
    teks = stemming(teks)  # 4
    teks = hilangkan_stopword(teks)  # 5
    return teks


def seq_pad_and_trunc(sentences, tokenizer, padding='post', truncating='post', maxlen=16):

    sequences = tokenizer.texts_to_sequences(sentences)
    pad_trunc_sequences = pad_sequences(
        sequences, maxlen=maxlen, padding=padding, truncating=truncating)

    return pad_trunc_sequences


def predict(sentence):
    sentence = preprocess(sentence)

    if len(sentence) == 0:
        return False

    sentence = np.expand_dims(sentence, axis=-1)
    pad_trunc_sequence = seq_pad_and_trunc(sentence, tokenizer)
    prob = model.predict(pad_trunc_sequence)

    if prob > 0.5:
        return True
    return False
