#load the dataset
import pandas as pd
from sklearn.externals import joblib
import pickle
import datetime
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

import spacy
import xx_ent_wiki_sm
from flask import json

#ini sengaja salah
#
#
#
#


def classify(text):
	# create stemmer
	factory = StemmerFactory()
	stemmer = factory.create_stemmer()

	filename = 'finalized_model.sav'
	#topredict = [stemmer.stem('HAJIN, KOMPAS.com - Sebuah rekaman memperlihatkan seorang komandan Negara Islam Irak dan Suriah ( ISIS) tewas di pertempuran setelah ditinggalkan anak buahnya. Dilansir Daily Mirror Kamis (20/12/2018), rekaman yang berasal dari GoPro memperlihatkan komandan ISIS itu menyiapkan senapannya. Si komandan ISIS itu masih terus menyerang sebelum dia tertembak dan tewas. Videonya ditemukan oleh Pasukan Pertahanan Suriah (SDF). Berdasarkan laporan Idlib Post, peristiwa itu terjadi di Deir Ezzor, kota terbesar yang terletak di timur Suriah. Dalam akun media sosialnya, SDF menjelaskan para anggota ISIS berada dalam kebingungan dan memilih untuk tidak patuh kepada pemimpin mereka dengan meninggalkannya. Milisi Kurdi itu, diwartakan The Independent, tengah berada dalam operasi untuk membebaskan Hajin yang berada dalam kendali ISIS. Kota yang berlokasi di tepi sungai Eufrat itu merupakan benteng terakhir ISIS di Suriah. SDF mengumumkan telah menguasai sebagian besar Hajin. Pembebasan Hajin bakal menjadi batu pijakan penting bagi SDF yang sudah menjadi sekutu negara Barat untuk memerangi ISIS dalam empat tahun terakhir.')]
	topredict = [stemmer.stem(text)]

	#load model
	loaded_model = joblib.load(open(filename, 'rb'))
	return ''.join(loaded_model.predict(topredict))


def ner(text):
	nlp = xx_ent_wiki_sm.load()
	doc = nlp(text.decode('utf-8', 'ignore'))
	
	#pprint([(X.text, X.label_) for X in doc.ents])
	result = '{"entities":['
	for X in doc.ents:
		result += '{"entity":"%s","ne":"%s"},'%(X.text, X.label_)
	return result[:-1] + ']}'
