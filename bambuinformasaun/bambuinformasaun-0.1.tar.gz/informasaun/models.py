from django.db import models
from jeral.models import *

from django.contrib.auth.models import User

from ckeditor.fields import RichTextField




class Parceiru(models.Model):
    naran			= models.CharField(max_length=150)
    logo		= models.ImageField(upload_to='pajina/', default='pajina/default.png')
    file_pdf	= models.FileField(upload_to='upload_file_parceiru/', null=True, blank=True, default='pdf_mamuk.pdf')
    data = models.DateField(verbose_name="Data",null=True, blank=True)
    user_created = models.ForeignKey(User, on_delete = models.CASCADE,null=True, blank=True, verbose_name = "Hili User")
    date_created = models.DateField(verbose_name="Data Rejistu",null=True, blank=True)
    hashed = models.TextField(null=True, blank=True)
    def save(self):
        super().save()

    def __str__(self):
        return "{}. {}".format(self.id, self.naran)


class Pajina(models.Model):
    naran			= models.CharField(max_length=150)
    data = models.DateField(verbose_name="Data",null=True, blank=True)
    user_created = models.ForeignKey(User, on_delete = models.CASCADE,null=True, blank=True, verbose_name = "Hili User")
    date_created = models.DateField(verbose_name="Data Rejistu",null=True, blank=True)
    hashed = models.TextField(null=True, blank=True)
    def save(self):
        super().save()

    def __str__(self):
        return "{}. {}".format(self.id, self.user_created)


 
class KonteuduPajina(models.Model):
    pajina = models.ForeignKey(Pajina, related_name='pajina', on_delete=models.CASCADE)
    titulu	= models.CharField(max_length=150)
    data = models.DateField(verbose_name="Data",null=True, blank=True)
    konteudu	= RichTextField(null=False, blank=False)
    imagen		= models.ImageField(upload_to='pajina/', default='pajina/default.png', null=True, blank=True)
    lingua 			= models.ForeignKey(Lingua,null=True, blank=True, on_delete=models.CASCADE)
    file_pdf	= models.FileField(upload_to='upload_file_konteudu/', null=True, blank=True, default='pdf_mamuk.pdf')
    linkvideo			= models.CharField(max_length=150, verbose_name ="Link Video", null = True, blank=True)
    user_created = models.ForeignKey(User, on_delete = models.CASCADE,null=True, blank=True, verbose_name = "Hili User")
    date_created = models.DateField(verbose_name="Data Rejistu",null=True, blank=True)
    hashed = models.TextField(null=True, blank=True)
    def save(self):
        super().save()

    def __str__(self):
        return "{}. {}".format(self.id, self.titulu)


class Informasaun(models.Model):
    imagen_main		= models.ImageField(upload_to='pajina/', default='pajina/default.png', null=True, blank=True)
    # lingua 			= models.ForeignKey(Lingua, related_name='lingua', on_delete=models.CASCADE)
    status = models.BooleanField(default=False,verbose_name='Staus Publika') 
    user_created = models.ForeignKey(User, on_delete = models.CASCADE,null=True, blank=True, verbose_name = "Hili User")
    data = models.DateField(verbose_name="Data",null=False, blank=False)
    date_created = models.DateField(verbose_name="Data Rejistu",null=True, blank=True)
    hashed = models.TextField(null=True, blank=True)
    def save(self):
        super().save()
    def __str__(self):
        return "{}. {}".format(self.id, self.hashed)


class KonteuduInformasaun(models.Model):
    informasaun = models.ForeignKey(Informasaun, on_delete = models.CASCADE,null=True, blank=True, verbose_name = "Hili informasaun")
    titulu = models.CharField(max_length=250,null=False, blank=False)
    konteudu	= RichTextField(null=False, blank=False)
    # imagen_main		= models.ImageField(upload_to='pajina/', default='pajina/default.png', null=True, blank=True)
    lingua = models.ForeignKey(Lingua, related_name='lingua', on_delete=models.CASCADE, default = 1,null=False, blank=False)
    status = models.BooleanField(default=False,verbose_name='Staus Publika') 
    user_created = models.ForeignKey(User, on_delete = models.CASCADE,null=True, blank=True, verbose_name = "Hili User")
    data = models.DateField(verbose_name="Data")
    date_created = models.DateField(verbose_name="Data Rejistu",null=True, blank=True)
    hashed = models.TextField(null=True, blank=True)
    def save(self):
        super().save()
    def __str__(self):
        return "{}. {}".format(self.id, self.titulu)


class ImagenInformasaun(models.Model):
    informasaun =  models.ForeignKey(Informasaun, related_name='pajina', on_delete=models.CASCADE)
    imagen		= models.ImageField(upload_to='pajina/', default='pajina/default.png')
    user_created = models.ForeignKey(User, on_delete = models.CASCADE,null=False, blank=False, verbose_name = "Hili User")
    date_created = models.DateField(verbose_name="Data Rejistu",null=True, blank=True)
    hashed = models.TextField(null=True, blank=True)
    def save(self):
        super().save()
    def __str__(self):
        return "{}".format(self.id)


class KonteuduImagenInformasaun(models.Model):
    imageinformasaun =  models.ForeignKey(ImagenInformasaun, related_name='imageninformasaun', on_delete=models.CASCADE)
    deskrisaun =  RichTextField(max_length = 70, null=False, blank=False)
    user_created = models.ForeignKey(User, on_delete = models.CASCADE,null=True, blank=True, verbose_name = "Hili User")
    date_created = models.DateField(verbose_name="Data Rejistu",null=True, blank=True)
    hashed = models.TextField(null=True, blank=True)
    def save(self):
        super().save()
    def __str__(self):
        return "{}. {}".format(self.id, self.hashed)




class KategoriaProdutu(models.Model):
    lingua = models.ForeignKey(Lingua, on_delete = models.CASCADE,null=True, blank=True, verbose_name = "Hili Lingua")
    titulu = models.CharField(max_length=250,null=False, blank=False)
    imagen		= models.ImageField(upload_to='pajina/', default='produtu/default.png', null=True, blank=True)
    user_created = models.ForeignKey(User, on_delete = models.CASCADE,null=True, blank=True, verbose_name = "Hili User")
    date_created = models.DateField(verbose_name="Data Rejistu",null=True, blank=True)
    hashed = models.TextField(null=True, blank=True)
    def save(self):
        super().save()
    def __str__(self):
        return "{}. {}".format(self.id, self.titulu)


class Produtu(models.Model):
    imagen_main		= models.ImageField(upload_to='produtu/', default='produtu/default.png', null=True, blank=True)
    presu = models.FloatField(max_length=250,null=False, blank=False)
    status = models.BooleanField(default=False,verbose_name='Staus Publika')
    kategoriaprodutu = models.ForeignKey(KategoriaProdutu, related_name='kategoria', on_delete = models.CASCADE,null=False, blank=False)
    user_created = models.ForeignKey(User, on_delete = models.CASCADE,null=True, blank=True, verbose_name = "Hili User")
    data = models.DateField(verbose_name="Data Publika",null=False, blank=False)
    date_created = models.DateField(verbose_name="Data Rejistu",null=True, blank=True)
    hashed = models.TextField(null=True, blank=True)
    foun = models.BooleanField(default=False,verbose_name='Foun')
    def save(self):
        super().save()
    def __str__(self):
        return "{}. {}".format(self.id, self.hashed)


class KonteuduProdutu(models.Model):
    produtu = models.ForeignKey(Produtu, on_delete = models.CASCADE,null=True, blank=True, verbose_name = "Hili produtu")
    titulu = models.CharField(max_length=250,null=False, blank=False)
    konteudu	= RichTextField(null=False, blank=False)
    lingua = models.ForeignKey(Lingua, related_name='linguaprodutu', on_delete=models.CASCADE, default = 1,null=False, blank=False)
    user_created = models.ForeignKey(User, on_delete = models.CASCADE,null=True, blank=True, verbose_name = "Hili User")
    data_produsaun = models.DateField(verbose_name="Data Publika",null=False, blank=False)
    date_created = models.DateField(verbose_name="Data Rejistu",null=True, blank=True)
    hashed = models.TextField(null=True, blank=True)
    def save(self):
        super().save()
    def __str__(self):
        return "{}. {}".format(self.id, self.titulu)


class ImagenProdutu(models.Model):
    produtu =  models.ForeignKey(Produtu, related_name='Produtu', on_delete=models.CASCADE)
    imagen		= models.ImageField(upload_to='produtu/', default='produtu/default.png')
    user_created = models.ForeignKey(User, on_delete = models.CASCADE,null=True, blank=True, verbose_name = "Hili User")
    date_created = models.DateField(verbose_name="Data Rejistu",null=True, blank=True)
    hashed = models.TextField(null=True, blank=True)
    def save(self):
        super().save()
    def __str__(self):
        return "{}. {}".format(self.id, self.hashed)