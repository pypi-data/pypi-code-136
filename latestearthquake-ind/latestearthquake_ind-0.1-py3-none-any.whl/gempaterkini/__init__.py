import requests
from bs4 import BeautifulSoup

import gempaterkini


def ekstraksi_data():
    """
    Tanggal: 15 Oktober 2022
    Waktu: 00:40:44 WIB
    Magnitudo: 4.9
    Kedalaman: 10 km
    Lokasi: LS=3.83 BT=103.68
    Pusat Gempa: Pusat gempa berada di darat 16 km tenggara Lahat
    Dirasakan: Dirasakan (Skala MMI): III-IV Lahat, III-IV Muara Enim
    :return:
    """
    try:
        content = requests.get('https://bmkg.go.id')
    except Exception:
        return None
    if content.status_code==200:
        soup = BeautifulSoup(content.text, 'html.parser')
        result = soup.find('span', {'class': 'waktu'})
        result = result.text.split(', ')
        tanggal = result[0]
        waktu = result[1]

        result = soup.find('div', {'class': 'col-md-6 col-xs-6 gempabumi-detail no-padding'})
        result = result.findChildren('li')
        i = 0
        magnitudo = None
        kedalaman = None
        koordinat = None
        ls = None
        bt = None
        dirasakan = None
        for res in result:
            if i == 1:
                magnitudo = res.text
            elif i == 2:
                kedalaman = res.text
            elif i == 3:
                koordinat = res.text.split(' - ')
                ls = koordinat[0]
                bt = koordinat[1]
            elif i == 4:
                lokasi = res.text
            elif i == 5:
                dirasakan = res.text
            i = i + 1

        hasil = dict()
        hasil['tanggal'] = tanggal
        hasil['waktu'] = waktu
        hasil['magnitudo'] = magnitudo
        hasil['kedalaman'] = kedalaman
        hasil['koordinat'] = {'ls': ls, 'bt': bt}
        hasil['lokasi'] = 'Pusat gempa berada di darat 16 km tenggara Lahat'
        hasil['dirasakan'] = dirasakan #'Dirasakan (Skala MMI): III-IV Lahat, III-IV Muara Enim'
        return hasil
    else:
        return None



def tampilkan_data(result):
    if result is None:
        print('Tidak bisa menemukan data gempa terkini')
        return
    print('Gempa terakhir berdasarkan BMKG')
    print(f"Tanggal: {result['tanggal']}")
    print(f"Waktu: {result['waktu']}")
    print(f"Magnitudo: {result['magnitudo']}")
    print(f"Kedalaman: {result['kedalaman']}")
    print(f"Koordinat: LS={result['koordinat']['ls']} BT={result['koordinat']['bt']}")
    print(f"Lokasi: {result['lokasi']}")
    print(f"Dirasakan: {result['dirasakan']}")

if __name__ == '__main__':
    result = ekstraksi_data()
    tampilkan_data(result)
