from django.db import models

# 0. Country
class Country(models.Model):
    name = models.CharField(max_length=255)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

# 1. Provinsi
# ref. https://www.brilio.net/creator/9-istilah-pembagian-administratif-di-indonesia-dalam-bahasa-inggris-7f6bfd.html
class Province(models.Model):
    '''
        Relasi :
            -
        Deskripsi :
            tanpa site, karena semua site menggunakan table :
            provinsi, kabupaten, kecamatan, kelurahan
    '''
    name = models.CharField(max_length=255)  

    # Optional fields
    country = models.ForeignKey(Country, null=True, blank=True, on_delete=models.PROTECT)        
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

# 2. Kabupaten        
class Regency(models.Model):
    '''
        Relasi :
            Provinsi --1:N-- Kabupaten
        Deskripsi :
            Relasi Protect digunakan untuk antisipasi kehilangan data
            karena proses hapus data provinsi, data kabupaten yg berhubungan ikut terhapus
            dengan protect ini, munculin pesan kalau data masih digunakan di kabupaten
            baru bisa hapus data provinsi        
    '''
    name = models.CharField(max_length=255)

    # Optional Fields :
    province = models.ForeignKey(Province, null=True, blank=True, on_delete=models.PROTECT)    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name   

# 3. Kecamatan
class SubDistrict(models.Model):
    '''
        Relasi :
            Kabupaten --1:N-- Kecamatan
        Deskripsi :
            -
    '''
    name = models.CharField(max_length=255)

    # Optional Fields :
    regency = models.ForeignKey(Regency, null=True, blank=True, on_delete=models.PROTECT)    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name 

# ward / region
# 4. Kelurahan
class UrbanVillage(models.Model):
    '''
        Relasi :
            Kecamatan --1:N-- Kelurahan
        Deskripsi :
            -
    '''    
    name = models.CharField(max_length=255)

    # Optional Fields:
    sub_district = models.ForeignKey(SubDistrict, null=True, blank=True, on_delete=models.PROTECT)    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name 