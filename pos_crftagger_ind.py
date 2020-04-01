from __future__ import unicode_literals
from nltk import word_tokenize
from nltk.tag import CRFTagger
ct = CRFTagger()
ct.set_model_file('all_indo_man_tag_corpus_model.crf.tagger')
hasil = ct.tag_sents([['Saya','bekerja','di','Bandung']])

hasil2 = ct.tag_sents([word_tokenize('Saya bekerja di Bandung')])

hasil3 = ct.tag_sents([word_tokenize('HAJIN, KOMPAS.com - Sebuah rekaman memperlihatkan seorang komandan Negara Islam Irak dan Suriah ( ISIS) tewas di pertempuran setelah ditinggalkan anak buahnya. Dilansir Daily Mirror Kamis (20/12/2018), rekaman yang berasal dari GoPro memperlihatkan komandan ISIS itu menyiapkan senapannya. Si komandan ISIS itu masih terus menyerang sebelum dia tertembak dan tewas. Videonya ditemukan oleh Pasukan Pertahanan Suriah (SDF). Berdasarkan laporan Idlib Post, peristiwa itu terjadi di Deir Ezzor, kota terbesar yang terletak di timur Suriah. Dalam akun media sosialnya, SDF menjelaskan para anggota ISIS berada dalam kebingungan dan memilih untuk tidak patuh kepada pemimpin mereka dengan meninggalkannya. Milisi Kurdi itu, diwartakan The Independent, tengah berada dalam operasi untuk membebaskan Hajin yang berada dalam kendali ISIS. Kota yang berlokasi di tepi sungai Eufrat itu merupakan benteng terakhir ISIS di Suriah. SDF mengumumkan telah menguasai sebagian besar Hajin. Pembebasan Hajin bakal menjadi batu pijakan penting bagi SDF yang sudah menjadi sekutu negara Barat untuk memerangi ISIS dalam empat tahun terakhir.')])

#print(hasil)
print(hasil3)
#print(word_tokenize('Saya bekerja di Bandung'))
