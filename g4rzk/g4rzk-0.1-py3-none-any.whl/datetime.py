from g4rzk.module import *

ct = datetime.now()
n = ct.month
bulan =  ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
try:
	if n < 0 or n > 12:
		exit()
	nTemp = n - 1
except ValueError:
	exit()

current = datetime.now()
tahun = current.year
bu = current.month
hari = current.day
bulan = bulan[nTemp]

my_date = date.today()
hr = calendar.day_name[my_date.weekday()]
cv_hr = {"Sunday":"Minggu", "Monday":"Senin", "Tuesday":"Selasa", "Wednesday":"Rabu", "Thursday":"Kamis", "Friday":"Jumat", "Saturday":"Sabtu"}

nama_hari = cv_hr[hr]
tgl = (f"{hari}-{bulan}-{tahun}")
tanggal = (f"{nama_hari}-{hari}-{bulan}-{tahun}")
bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

now = datetime.now()
hour = now.hour
if hour < 4:
	waktu = "Selamat Dini Hari"
elif 4 <= hour < 12:
	waktu = "Selamat Pagi"
elif 12 <= hour < 15:
	waktu = "Selamat Siang"
elif 15 <= hour < 17:
	waktu = "Selamat Sore"
else:
	waktu = "Selamat Malam"