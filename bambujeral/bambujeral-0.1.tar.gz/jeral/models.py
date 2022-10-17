from django.db import models
from django.contrib.auth.models import User
# Create your models here.



TIPO = (
        ("copia", "copia"),
        ("original", "original"),
        ("copia/original", "copia/original"),
        )


APROVE_TYPE = (
        ("sim", "sim"),
        ("nao", "nao"),
        ("nao/necesario", "nao/necesario"),
        )



class Munisipiu(models.Model):
    naran 	= models.CharField(max_length=255,null=False, blank=False)
    date_created = models.DateField(verbose_name="Data Rejistu",null=True, blank=True)
    hashed = models.TextField(null=True, blank=True)
    def __str__(self):
        return "{}".format(self.naran)
        return template.format(self)
    class Meta :
        verbose_name_plural = "Munisipiu"



class Postu(models.Model):
    naran 	= models.CharField(max_length=255,null=False, blank=False)
    munisipiu = models.ForeignKey(Munisipiu, on_delete = models.CASCADE, verbose_name = "Hili Munisipiu")
    date_created = models.DateField(verbose_name="Data Rejistu",null=True, blank=True)
    hashed = models.TextField(null=True, blank=True)
    def __str__(self):
        return "{}".format(self.naran)
        return template.format(self)
    class Meta :
        verbose_name_plural = "Postu"




class Suku(models.Model):
    naran 	= models.CharField(max_length=255,null=False, blank=False)
    postu = models.ForeignKey(Postu, on_delete = models.CASCADE, verbose_name = "Hili Postu")
    date_created = models.DateField(verbose_name="Data Rejistu",null=True, blank=True)
    hashed = models.TextField(null=True, blank=True)
    def __str__(self):
        return "{}".format(self.naran)
        return template.format(self)
    class Meta :
        verbose_name_plural = "Suku"



class Lingua(models.Model):
    naran 	= models.CharField(max_length=255,null=False, blank=False)
    icon		= models.ImageField(upload_to='lingua/', default='pajina/default.jpg', null=True, blank=True)
    def __str__(self):
        return "{}.".format(self.naran)
        return template.format(self)
    class Meta :
        verbose_name_plural = "Lingua"












# class Rejiaun(models.Model):
#     rejiaun 	= models.CharField(max_length=255,null=False, blank=False)
#     user_created = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = "User Ne'ebe Kria")
#     date_created = models.DateField(verbose_name="Data Rejistu",null=True, blank=True)
#     user_update = models.CharField(max_length=255)

#     def __str__(self):
#         return "{}. {}".format(self.id, self.rejiaun, )
#     class Meta :
#         verbose_name_plural = "Relijiaun"



# class Nasaun(models.Model):
#     nasaun 	= models.CharField(max_length=255,null=False, blank=False)
#     rejiaun			= models.ForeignKey(Rejiaun, on_delete=models.CASCADE, null=False, blank=False)
#     user_created = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = "User Ne'ebe Kria")
#     date_created = models.DateField(verbose_name="Data Rejistu",null=True, blank=True)
#     user_update = models.CharField(max_length=255)

#     def __str__(self):
#         return "{}. {} - {}".format(self.id, self.nasaun, self.rejiaun.rejiaun)
#     class Meta :
#         verbose_name_plural = "Nasaun"





# class Lokalizasaun(models.Model):
#     lokalizasaun 	= models.CharField(max_length=255,null=False, blank=False)
#     deskrisaun 	= models.TextField(max_length=255,null=False, blank=False)
#     user_created = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = "User Ne'ebe Kria")
#     date_created = models.DateField(verbose_name="Data Rejistu",null=True, blank=True)
#     user_update = models.CharField(max_length=255)
#     def __str__(self):
#         return "{}. {} - {}".format(self.id, self.lokalizasaun, self.deskrisaun)
#     class Meta :
#         verbose_name_plural ="Lokalizasaun"



# class KategoriaDoc(models.Model):
#     kategoria 	= models.CharField(max_length=255,null=False, blank=False)
#     user_created = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = "User Ne'ebe Kria")
#     date_created = models.DateField(verbose_name="Data Rejistu",null=True, blank=True)
#     user_update = models.CharField(max_length=255)
#     def __str__(self):
#         return "{}. {}".format(self.id, self.kategoria)
#     class Meta :
#         verbose_name_plural ="Kategoria Dokumentu"


# class  Dokumentu(models.Model):
#     naran 	= models.TextField(null=False, blank=False)
#     data_asinatura			= models.DateField(verbose_name="Data Rejistu",null=True, blank=True)
#     aprovadu_cm = models.CharField(max_length=50,choices=APROVE_TYPE,verbose_name='Aprovadu CM : ',null = True, blank = True)
#     aprovadu_pm = models.CharField(max_length=50,choices=APROVE_TYPE,verbose_name='Aprovadu PM : ',null = True, blank = True)
#     resolusaun = models.TextField(default=False,null=True, blank = True, verbose_name = "Resolusaun")
#     tipu = models.CharField(max_length=50,choices=TIPO,verbose_name='Tipu Dokumentu : ',null = True, blank = True)
#     lingua = models.ForeignKey(Lingua, on_delete = models.CASCADE, verbose_name = "Lingua")
#     nasaun = models.ForeignKey(Nasaun, on_delete = models.CASCADE, verbose_name = "Nasaun")
#     localizasaun = models.ForeignKey(Lokalizasaun, on_delete = models.CASCADE, verbose_name = "Nasaun")
#     kategoria = models.ForeignKey(KategoriaDoc, on_delete = models.CASCADE, verbose_name = "Kategoria Dokumentu")
#     date_hahu= models.DateField(verbose_name="Data Hahu",null=True, blank=True)
#     date_remata = models.DateField(verbose_name="Data Remata",null=True, blank=True)
#     validade = models.TextField(verbose_name="Validade",null=True, blank=True)
#     user_created = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = "User Ne'ebe Kria",null=True, blank=True)
#     date_created = models.DateField(verbose_name="Data Rejistu",null=True, blank=True)
#     user_update = models.CharField(max_length=255, null=True, blank = True)
#     status 	= models.BooleanField(default=False)
#     def __str__(self):
#         return "{}. {}".format(self.id, self.naran)
#     class Meta :
#         verbose_name_plural ="Dokumentu"



# class FileUpload(models.Model):
#     dokumentu = models.ForeignKey(Dokumentu, on_delete = models.CASCADE, verbose_name = "Dokumentu")
#     deskrisaun 	= models.TextField(null=True, blank=True)
#     file_upload = models.FileField(upload_to="file_dokumentu/",  null=False, blank=False)
#     date_upload = models.DateField(verbose_name="Data Upload",null=True, blank=True)
#     user_created = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = "User Ne'ebe Kria",null=True, blank=True)
#     date_created = models.DateField(verbose_name="Data Rejistu",null=True, blank=True)
#     user_update = models.CharField(max_length=255)

#     def __str__(self):
#         return "{}. {} - {}".format(self.id,self.dokumentu, self.date_created)

#     class Meta :
#         verbose_name_plural ="File Upload"



# class  Komentariu(models.Model):
#     dokumentu = models.ForeignKey(Dokumentu, on_delete = models.CASCADE, verbose_name = "Dokumentu")
#     komentariu 		= models.TextField()
#     user_created = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = "User Ne'ebe Kria")
#     date_created = models.DateField(verbose_name="Data Rejistu",null=True, blank=True)
#     user_update = models.CharField(max_length=255)

#     def __str__(self):
#         return "{}. {} - {} - {} - {}".format(self.id, self.user_created, self.komentariu, self.user_created.first_name, self.dokumentu)

#     class Meta :
#         verbose_name_plural ="Komentario"
