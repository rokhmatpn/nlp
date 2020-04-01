from __future__ import unicode_literals
from pprint import pprint

import spacy
from spacy import displacy
from collections import Counter
import xx_ent_wiki_sm
nlp = xx_ent_wiki_sm.load()

#doc = nlp('European authorities fined Google a record $5.1 billion on Wednesday for abusing its power in the mobile phone market and ordered the company to alter its practices')
#topredict = nlp('HAJIN, KOMPAS.com - Sebuah rekaman memperlihatkan seorang komandan Negara Islam Irak dan Suriah ( ISIS) tewas di pertempuran setelah ditinggalkan anak buahnya. Dilansir Daily Mirror Kamis (20/12/2018), rekaman yang berasal dari GoPro memperlihatkan komandan ISIS itu menyiapkan senapannya. Si komandan ISIS itu masih terus menyerang sebelum dia tertembak dan tewas. Videonya ditemukan oleh Pasukan Pertahanan Suriah (SDF). Berdasarkan laporan Idlib Post, peristiwa itu terjadi di Deir Ezzor, kota terbesar yang terletak di timur Suriah. Dalam akun media sosialnya, SDF menjelaskan para anggota ISIS berada dalam kebingungan dan memilih untuk tidak patuh kepada pemimpin mereka dengan meninggalkannya. Milisi Kurdi itu, diwartakan The Independent, tengah berada dalam operasi untuk membebaskan Hajin yang berada dalam kendali ISIS. Kota yang berlokasi di tepi sungai Eufrat itu merupakan benteng terakhir ISIS di Suriah. SDF mengumumkan telah menguasai sebagian besar Hajin. Pembebasan Hajin bakal menjadi batu pijakan penting bagi SDF yang sudah menjadi sekutu negara Barat untuk memerangi ISIS dalam empat tahun terakhir.')

#load url
from bs4 import BeautifulSoup
import requests
import re
def url_to_string(url):
    res = requests.get(url)
    html = res.text
    soup = BeautifulSoup(html, 'html5lib')
    for script in soup(["script", "style", 'aside']):
        script.extract()
    return " ".join(re.split(r'[\n\t]+', soup.get_text()))

#ny_bb = url_to_string('https://www.washingtonpost.com/news/opinions/wp/2018/12/26/a-lesson-for-pelosi-and-schumer-never-wrestle-with-a-pig/?noredirect=on&utm_term=.9b8dd0ce27a4')
#ny_bb = url_to_string('https://nasional.kompas.com/read/2018/12/27/16595571/7-anggota-dprd-sumut-didakwa-terima-uang-ketok-dari-gatot-pujo')
ny_bb = 'HAJIN, KOMPAS.com - Sebuah rekaman memperlihatkan seorang komandan Negara Islam Irak dan Suriah ( ISIS) tewas di pertempuran setelah ditinggalkan anak buahnya. Dilansir Daily Mirror Kamis (20/12/2018), rekaman yang berasal dari GoPro memperlihatkan komandan ISIS itu menyiapkan senapannya. Si komandan ISIS itu masih terus menyerang sebelum dia tertembak dan tewas. Videonya ditemukan oleh Pasukan Pertahanan Suriah (SDF). Berdasarkan laporan Idlib Post, peristiwa itu terjadi di Deir Ezzor, kota terbesar yang terletak di timur Suriah. Dalam akun media sosialnya, SDF menjelaskan para anggota ISIS berada dalam kebingungan dan memilih untuk tidak patuh kepada pemimpin mereka dengan meninggalkannya. Milisi Kurdi itu, diwartakan The Independent, tengah berada dalam operasi untuk membebaskan Hajin yang berada dalam kendali ISIS. Kota yang berlokasi di tepi sungai Eufrat itu merupakan benteng terakhir ISIS di Suriah. SDF mengumumkan telah menguasai sebagian besar Hajin. Pembebasan Hajin bakal menjadi batu pijakan penting bagi SDF yang sudah menjadi sekutu negara Barat untuk memerangi ISIS dalam empat tahun terakhir.'

doc = nlp(ny_bb)
pprint([(X.text, X.label_) for X in doc.ents])
#pprint([(X.text, X.label_) for X in topredict.ents])
