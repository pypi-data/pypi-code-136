from django import forms 
from django.forms import ModelForm 

from .models import *



from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Button, HTML,Field,Div
from crispy_forms.bootstrap import TabHolder,Tab,Modal
# class DetailluNotisiaForm(forms.ModelForm):
# 	class Meta:
# 		model = Detaillu_Notisia 
# 		fields = ['sub_kategoria']

# class HakerekNotisiaKategoriaJornalForm(forms.ModelForm):
# 	class Meta:
# 		model = Notisia
# 		fields = ['titulu','sub_titulu','body','kategoria']


# class EditorNotisiaForm(forms.ModelForm):
# 	class Meta:
# 		model = Notisia
# 		fields = ['titulu','sub_titulu','body']

# 		widgets = {
#         'body': forms.Textarea(attrs={
#             'class':'form-control django-ckeditor-widget ckeditor',
#             'id':'form-control',
#             'spellcheck':'False'}),
#     }


# class uploadImagenNotisiaForm(forms.ModelForm):
# 	imagen_sub = forms.ImageField(required=True)
# 	class Meta:
# 		model = Imagen
# 		fields = ['imagen_sub']

# class FormFileUpload(forms.ModelForm):
# 	class Meta:
# 		model = FileUpload
# 		fields = ['deskrisaun','file_upload']

# class FormDokumentu(forms.ModelForm):
# 	class Meta:
# 		model = Dokumentu
# 		fields = ['naran','data_asinatura','aprovadu_cm','aprovadu_pm','resolusaun','tipu','lingua','nasaun','localizasaun','kategoria','date_hahu','date_remata','validade']

# 		widgets = {
# 			'data_asinatura': forms.DateInput(attrs={'type':'date'}),
# 			'date_hahu': forms.DateInput(attrs={'type':'date'}),
# 			'date_remata': forms.DateInput(attrs={'type':'date'})
		# }








class PerfilForm(forms.ModelForm):

	# descriptiond = forms.CharField(label="Observasaun", widget=forms.Textarea(attrs={"rows":2}), required=False)


	class Meta:
		model = Pajina
		fields = ['naran']


        

	def __init__(self, *args, **kwargs):
		super(PerfilForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.form_id = 'form_perfil'
		self.helper.layout = Layout(
		

			Row(
			Column('naran', css_class='form-group col-md-12 mb-0'),
			HTML(""" 

		
			
			<br>
				<div class='float-right'>



			<button  id = 'bambuinput' class="btn btn-sm btn-info" type="submit"><i class="fa fa-save"></i> {% if asaun  == 'edit' %} Atualiza {% else %} Rejistu {% endif %}
				</button>

					<a class="btn btn-sm btn-warning" onclick=self.history.back()><span class="btn-label"><i class="fa fa-window-close"></i></span> Kansela</a>		
				</div>
				
				""")
		)
		)



class KonteuduPajinaForm(forms.ModelForm):
	
	# descriptiond = forms.CharField(label="Observasaun", widget=forms.Textarea(attrs={"rows":2}), required=False)
	data = forms.DateField(label="Data ",widget=forms.TextInput(attrs={'type': 'date'}))

	class Meta:
		model = KonteuduPajina
		fields = ['titulu','konteudu','imagen','file_pdf','linkvideo','data']
	def __init__(self, *args, **kwargs):
		super(KonteuduPajinaForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.form_id = 'form_perfil'
		self.helper.layout = Layout(
		
		   Column(
			Column('titulu', css_class='form-group col-md-12 mb-0'),
		    ),

		  Row(

			Column('konteudu', css_class='form-group col-md-12 mb-0'),
		    ),

		   HTML("""<hr>Atatch File<hr>"""),
				Row(
			Column('imagen', css_class='form-group col-md-6 mb-0'),
			Column('file_pdf', css_class='form-group col-md-6 mb-0'),
			Column('linkvideo', css_class='form-group col-md-6 mb-0'),
			Column('data', css_class='form-group col-md-6 mb-0'),

			

		    ),

			HTML(""" 
			<br>
				<div class='float-right'>
			<button  id = 'bambuinput' class="btn btn-sm btn-info" type="submit"><i class="fa fa-save"></i> {% if asaun  == 'edit' %} Atualiza {% else %} Rejistu {% endif %}
				</button>

					<a class="btn btn-sm btn-warning" onclick=self.history.back()><span class="btn-label"><i class="fa fa-window-close"></i></span> Kansela</a>
				</div>
				
				""")
	
		)


		
	# 	    titulu = models.CharField(max_length=250,null=True, blank=True)
    # konteudu	= models.TextField(null=True, blank=True)
    # imagen_main		= models.ImageField(upload_to='pajina/', default='pajina/default.jpg', null=True, blank=True)
    # lingua 			= models.ForeignKey(Lingua, related_name='lingua', on_delete=models.CASCADE)
    # user_created = models.ForeignKey(User, on_delete = models.CASCADE,null=True, blank=True, verbose_name = "Hili User")
    # date_created = models.DateField(verbose_name="Data Rejistu",null=True, blank=True)





class InformasaunForm(forms.ModelForm):
	# descriptiond = forms.CharField(label="Observasaun", widget=forms.Textarea(attrs={"rows":2}), required=False)
	data = forms.DateField(label="Data ",widget=forms.TextInput(attrs={'type': 'date'}))

	class Meta:
		model = Informasaun
		fields = ['data']

	def __init__(self, *args, **kwargs):
		super(InformasaunForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.form_id = 'form_perfil'
		self.helper.layout = Layout(
		
		   Column(
			Column('data', css_class='form-group col-md-12 mb-0'),
		    ),
			HTML(""" 
			<br>
				<div class='float-right'>
			<button  id = 'bambuinput' class="btn btn-sm btn-info" type="submit"><i class="fa fa-save"></i> {% if asaun  == 'edit' %} Atualiza {% else %} Rejistu {% endif %}
				</button>

					<a class="btn btn-sm btn-warning" onclick=self.history.back()><span class="btn-label"><i class="fa fa-window-close"></i></span> Kansela</a>
				
				</div>
				
				""")
	
		)



class ParceiruForm(forms.ModelForm):
	# descriptiond = forms.CharField(label="Observasaun", widget=forms.Textarea(attrs={"rows":2}), required=False)

	class Meta:
		model = Parceiru
		fields = ['naran','logo','file_pdf']

	def __init__(self, *args, **kwargs):
		super(ParceiruForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.form_id = 'form_perfil'
		self.helper.layout = Layout(
		   Column(
			Column('naran', css_class='form-group col-md-12 mb-0'),
			Column('logo', css_class='form-group col-md-12 mb-0'),
			Column('file_pdf', css_class='form-group col-md-12 mb-0'),

		    ),



	

			HTML(""" 
			<br>
				<div class='float-right'>
			<button  id = 'bambuinput' class="btn btn-sm btn-info" type="submit"><i class="fa fa-save"></i> {% if asaun  == 'edit' %} Atualiza {% else %} Rejistu {% endif %}
				</button>

					<a class="btn btn-sm btn-warning" onclick=self.history.back()><span class="btn-label"><i class="fa fa-window-close"></i></span> Kansela</a>


			
				
				</div>
				
				""")
	
		)




# class ImagenInformasaun(models.Model):
#     informasaun =  models.ForeignKey(Informasaun, related_name='pajina', on_delete=models.CASCADE)
#     deskrisaun =  models.TextField(null=True, blank=True)
#     imagen		= models.ImageField(upload_to='pajina/', default='pajina/default.jpg', null=True, blank=True)


class ImagenInformasaunForm(forms.ModelForm):
	# descriptiond = forms.CharField(label="Observasaun", widget=forms.Textarea(attrs={"rows":2}), required=False)

	class Meta:
		model = ImagenInformasaun
		fields = ['imagen']
	def __init__(self, *args, **kwargs):
		super(ImagenInformasaunForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.form_id = 'form_informasaun'
		self.helper.layout = Layout(

	

		Row(
			Column('imagen', css_class='form-group col-md-12 mb-0', onchange="myFunction()"),
			Column(HTML("""<br><button style='float:right;' id = 'bambuinput' class='form-group btn btn-primary' type='submit'> Upload</button>"""), css_class='form-group col-md-12 mb-0'),
		    css_class='row'),

		)





class KonteuduInformasaunForm(forms.ModelForm):
	data = forms.DateField(label="Data ",widget=forms.TextInput(attrs={'type': 'date'}))
	class Meta:
		model = KonteuduInformasaun
		fields = ['titulu','konteudu','data']
	def __init__(self, *args, **kwargs):
		super(KonteuduInformasaunForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.form_id = 'form_informasaun'
		self.helper.layout = Layout(
		Row(
			Column('titulu', css_class='form-group col-md-12 mb-0', onchange="myFunction()"),
			Column('konteudu', css_class='form-group col-md-12 mb-0'),
			Column(Field('data', css_class="form-select"), css_class='form-group col-md-12 mb-0'),
			Column(HTML(""" 

		
			<br>
		<div class='float-right'>
			<button  id = 'bambuinput' class="btn btn-sm btn-info" type="submit"><i class="fa fa-save"></i> {% if asaun  == 'edit' %} Atualiza {% else %} Rejistu {% endif %}
				</button>

					<a class="btn btn-sm btn-warning" onclick=self.history.back()><span class="btn-label"><i class="fa fa-window-close"></i></span> Kansela</a>	
				</div>
				
				""")
	
		, css_class='form-group col-md-12 mb-0'),
		    css_class='row'),
		)



class ProdutuForm(forms.ModelForm):
	class Meta:
		model = Produtu
		fields = ['kategoriaprodutu','presu','foun']





		
class KonteuduProdutuForm2(forms.ModelForm):


	data_produsaun = forms.DateField(label="Data Publika ",widget=forms.TextInput(attrs={'type': 'date'}))
	kategoria = forms.ChoiceField(label='Kategoria Produtu', widget=forms.Select)

	class Meta:
		model = KonteuduProdutu
		fields = ['titulu','konteudu','data_produsaun']
	def __init__(self, *args, **kwargs):
		super(KonteuduProdutuForm2, self).__init__(*args, **kwargs)
		self.fields['kategoria'].choices=[(item.pk, (str(item.titulu)  )) for item in KategoriaProdutu.objects.all()]
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.form_id = 'form_produtu'
		self.helper.layout = Layout(

		Row(
			Column('titulu', css_class='form-group col-md-12 mb-0', onchange="myFunction()"),
			Column(HTML("""<br>""")),
			Column('konteudu', css_class='form-group col-md-12 mb-0'),
			Column(HTML("""<br>""")),
			Column(Field('data_produsaun', css_class="form-select"), css_class='form-group col-md-12 mb-0'),
			Column(HTML("""<br>""")),
			Column(Field('kategoria', css_class="form-select"), css_class='form-group col-md-12 mb-0'),
			Column(HTML(""" <br>  {% load crispy_forms_tags %} {{forms2|crispy}}  """), css_class='form-group col-md-12 mb-0'),
			Column(HTML(""" 
			

			{% if asaun  == 'edit' %}

			<div id="div_id_presu" class="form-group"> <label for="id_presu" class="">
                Presu
            </label> <div> <input type="text" value='{{presu}}' name="presu" maxlength="250" class="textinput textInput form-control" id="id_presu"> </div> </div>
		
			{% if foun   %}



			<div class="form-group"> <div id="div_id_foun" class="form-check"> <input checked type="checkbox" name="foun" class="checkboxinput form-check-input" id="id_foun"> <label for="id_foun" class="form-check-label">
                    Foun
                </label> </div> </div>

			{% else %}


			 		<div class="form-group"> <div id="div_id_foun" class="form-check"> <input type="checkbox" name="foun" class="checkboxinput form-check-input" id="id_foun"> <label for="id_foun" class="form-check-label">
                    Foun
                </label> </div> </div>

          
			 {% endif %}
			 {% endif %}
			 
			  """), css_class='form-group col-md-12 mb-0'),







			Column(HTML("""<br> 
			<div class='float-right'>
			<button  id = 'bambuinput' class="btn btn-sm btn-info" type="submit"><i class="fa fa-save"></i> {% if asaun  == 'edit' %} Atualiza {% else %} Rejistu {% endif %}
			</button>
			<a class="btn btn-sm btn-warning" onclick=self.history.back()><span class="btn-label"><i class="fa fa-window-close"></i></span> Kansela</a>	
			</div>
			""")
		, css_class='form-group col-md-12 mb-0'),
		    css_class='row'),

		)



		
class KonteuduProdutuForm(forms.ModelForm):


	data_produsaun = forms.DateField(label="Data Publika ",widget=forms.TextInput(attrs={'type': 'date'}))
	# kategoria = forms.ChoiceField(label='Kategoria Produtu', widget=forms.Select)

	class Meta:
		model = KonteuduProdutu
		fields = ['titulu','konteudu','data_produsaun']
	def __init__(self, *args, **kwargs):
		super(KonteuduProdutuForm, self).__init__(*args, **kwargs)
		# self.fields['kategoria'].choices=[(item.pk, (str(item.titulu)  )) for item in KategoriaProdutu.objects.all()]
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.form_id = 'form_produtu'
		self.helper.layout = Layout(

		Row(
			Column('titulu', css_class='form-group col-md-12 mb-0', onchange="myFunction()"),
			Column(HTML("""<br>""")),
			Column('konteudu', css_class='form-group col-md-12 mb-0'),
			Column(HTML("""<br>""")),
			Column(Field('data_produsaun', css_class="form-select"), css_class='form-group col-md-12 mb-0'),
			Column(HTML("""<br>""")),
			Column(HTML("""  {% load crispy_forms_tags %} {{forms2|crispy}}  """), css_class='form-group col-md-12 mb-0'),








			Column(HTML("""<br> 
			<div class='float-right'>
			<button  id = 'bambuinput' class="btn btn-sm btn-info" type="submit"><i class="fa fa-save"></i> {% if asaun  == 'edit' %} Atualiza {% else %} Rejistu {% endif %}
			</button>
			<a class="btn btn-sm btn-warning" onclick=self.history.back()><span class="btn-label"><i class="fa fa-window-close"></i></span> Kansela</a>	
			</div>
			""")
		, css_class='form-group col-md-12 mb-0'),
		    css_class='row'),

		)


class ImagenProdutuForm(forms.ModelForm):
	# descriptiond = forms.CharField(label="Observasaun", widget=forms.Textarea(attrs={"rows":2}), required=False)

	class Meta:
		model = ImagenProdutu
		fields = ['imagen']
	def __init__(self, *args, **kwargs):
		super(ImagenProdutuForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.form_id = 'form_informasaun'
		self.helper.layout = Layout(

	

		Row(
			Column('imagen', css_class='form-group col-md-12 mb-0', onchange="myFunction()"),
			Column(HTML("""<br><button style='float:right;' id = 'bambuinput' class='form-group btn btn-primary' type='submit'> Upload</button>"""), css_class='form-group col-md-12 mb-0'),
		    css_class='row'),

		)




		


	

		





# class GrupuBambuForm(forms.ModelForm):

# 	class Meta:
# 		model = GrupuBambu
# 		fields = ['naran','suku','deskrisaun']

# 	def __init__(self, *args, **kwargs):
# 		super(GrupuBambuForm, self).__init__(*args, **kwargs)
# 		self.helper = FormHelper()
# 		#     self.fields['aldeia'].choices=[
# 		#  (item.id, (str(item.name) )) for item in Aldeia.objects.filter(Q(village__id= site_id))]
# 		self.helper.form_method = 'post'
# 		self.helper.form_id = 'grupubambu'
        
#         # self.fields['aldeia'].choices=[(item.pk, (" Aldeia " + str(item.name) +" / Suku  " + str(item.village) + " / Postu "+ str(item.village.administrativepost) + " / Munisipiu " + str(item.village.administrativepost.municipality))) for item in Aldeia.objects.all()]


# 		self.helper.layout = Layout(

# 				Row(
# 				Column('naran', css_class='form-group col-md-4 mb-0'),
# 				Column('suku', css_class='form-group col-md-4 mb-0'),
# 				# Column('kordinate_centru', css_class='form-group col-md-4 mb-0'),
# 				css_class='form-row'
# 				),

# 				Row(
# 				# Column('kordinate_area', css_class='form-group col-md-4 mb-0'),
# 				Column('deskrisaun', css_class='form-group col-md-4 mb-0'),
# 				css_class='form-row'
# 				),

# 					HTML("""
						
# 							<a href='#'    id = '' class="btn btn-info" ><i class="fa fa-save"></i>  Rai </a>
# 					<a class="btn btn-sm btn-labeled btn-secondary" onclick=self.history.back()><span class="btn-label"><i class="fa fa-window-close"></i></span> Kansela</a>
			
# 				"""),
# 		)	






# class FormKomentariu(forms.ModelForm):
# 	class Meta:
# 		model = Komentariu
# 		fields = ['komentariu']





# class DateInput(forms.DateInput):
# 	input_type = 'date'
# class EdisaunNotisiaForm(forms.ModelForm):
# 	class Meta:
# 		model = Edisaun 
# 		fields = ['titulu','kategoria_edisaun','data','file_pdf']

# 		widgets = {
# 			'data': DateInput(),
# 		}


# class UploadFilePdf(forms.ModelForm):
# 	class Meta:
# 		model = Edisaun
# 		fields = ['file_pdf']
