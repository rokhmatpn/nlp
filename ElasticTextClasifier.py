import requests

url = "http://10.9.8.237:9200"

data = '''
{
  "query": {
    "more_like_this": {
      "fields": [
        "content"
      ],
      "like": "KOMPAS.com Pemerintah Provinsi (Pemprov) DKI Jakarta sebelumnya telah meluncurkan program satu peta, satu data, dan satu kebijakan yang terangkum dalam program Jakarta Satu. Gubernur DKI Jakarta Anies Baswedan menegaskan, hal ini dilakukan untuk menerapkan skema good governance yang sistematis berdasarkan satu pengelolaan data. Melalui sistem ini, kebijakan yang diambil Pemprov DKI Jakarta  dapat dilakukan secara konsisten berdasarkan pada kesamaan data dan informasi. Jadi, Jakarta Satu sebagai salah satu contoh perubahan menuju good governance sistematis yang sedang kita mulai, kata Anies melalui rilis tertulis yang Kompas.com terima, Rabu (12/13/18). Dengan adanya program yang telah diluncurkan pada 17 Januari 2018 ini, data-data dari seluruh Satuan Kerja Perangkat Daerah (SKPD) akan terintegrasi dan dapat diakses langsung oleh Pemprov DKI Jakarta di dalam peta dasar tunggal. Nah dengan program ini, maka kita bisa terintegrasi. Harapannya, meningkatkan keakuratan, keputusan, dan kebijakan langsung bagi Pemprov DKI Jakarta. Selain itu, kita juga bisa meningkatkan pendapatan, jelasnya. Pelaksana Tugas (Plt) Kepala Dinas Komunikasi, Informatika dan Statistik Provinsi (Diskominfotik) DKI Jakarta Atika Nur Rahmania menerangkan, melalui program ini seluruh jajaran Pemprov DKI Jakarta tanpa kecuali akan memiliki satu acuan data dan peta yang sama. Melalui sistem ini, kebijakan yang diambil Pemprov dapat dilakukan secara konsisten berdasarkan pada kesamaan data dan informasi. Peta dan informasi data itu akan diperbarui secara berkala oleh setiap SKPD agar lebih akurat. Dengan Jakarta Satu berarti Jakarta semakin meningkatkan lagi pemanfaatan Big Data, kata Atika.",
      "min_term_freq": 1,
      "max_query_terms": 20
    }
  }
}
'''

from operator import itemgetter
def get_best_category(response):
    categories = {}
    for hit in response['hits']['hits']:
        score = hit['_score']
        category = hit['_source']['category']
        if category not in categories:
            categories[category] = score
        else:
            categories[category] += score
    if len(categories) > 0:
        sortedCategories = sorted(categories.items(), key=itemgetter(1), reverse=True)
        category = sortedCategories[0][0]
    return category

print(get_best_category(requests.post("%s/trainingset/_search" % url, data=data, headers={"Content-Type": "application/json"}).json()))
