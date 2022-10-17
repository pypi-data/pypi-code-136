from django import forms 
from django.forms import ModelForm 

from .models import *


from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Button, HTML,Field,Div
from crispy_forms.bootstrap import TabHolder,Tab
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

class GrupuBambuForm(forms.ModelForm):
	# descriptiond = forms.CharField(label="Observasaun", widget=forms.Textarea(attrs={"rows":2}), required=False)

	class Meta:
		model = GrupuBambu
		fields = ['naran','suku','deskrisaun','imagen','kontaktu','naran_kordenador']


        

	def __init__(self, *args, **kwargs):
		super(GrupuBambuForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.fields['suku'].choices=[(item.pk, (str(item.naran) + str(" / Postu  ") + str(item.postu) + str(" / Munisípiu ") + str(item.postu.munisipiu) )) for item in Suku.objects.all()]
		self.helper.form_id = 'form_bambu'
		self.helper.layout = Layout(
			





			Row(
			Column('naran', css_class='form-group col-md-12 mb-0'),
			Column('naran_kordenador', css_class='form-group col-md-12 mb-0'),
			Column('kontaktu', css_class='form-group col-md-12 mb-0'),
			Column('imagen', css_class='form-group col-md-12 mb-0'),
			Column(Field('suku', css_class="form-select"), css_class='form-group col-md-12 mb-0'),
			# Column('kordinate_centru', css_class='form-group col-md-12 mb-0'),
			# Column('kordinate_area', css_class='form-group col-md-12 mb-0'),

				
			HTML(""" 

			{% if asaun  == 'edit' %}

			<input type='hidden' value='{% if kordinate == 'mamuk' %}  {{kordinate_centru}}  {% else %} {{kordinate}} {% endif %} ' id="kordinate_centru" name='kordinate_centru'>	<input type='hidden'  value ='{{kordinate_area}}' id = 'kordinate_area' name='kordinate_area'>
			{% else %}
			<input type='hidden' value='{% if kordinate != 'mamuk' %}  {{kordinate}} {% endif %}' id="kordinate_centru"  name='kordinate_centru'>	<input type='hidden'  id = 'kordinate_area' name='kordinate_area'>
			{% endif %}
	
	<br>
			 """),


			Column('deskrisaun', css_class='form-group col-md-12 mb-0'),
			# Column('kordinate_centru', css_class='form-group col-md-4 mb-0'),
			css_class='form-row'
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








class ImportasaunBambuForm(forms.ModelForm):
	# descriptiond = forms.CharField(label="Observasaun", widget=forms.Textarea(attrs={"rows":2}), required=False)
	data_importasaun = forms.DateField(label="Data ",widget=forms.TextInput(attrs={'type': 'date'}))
	class Meta:
		model = ImportasaunBambu
		fields = ['data_importasaun','kuantidade','deskrisaun']
	def __init__(self, *args, **kwargs):
		super(ImportasaunBambuForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.form_id = 'form_bambu'
		self.helper.layout = Layout(
			
		Row(

			Column('kuantidade', css_class='form-group col-md-6 mb-0'),
			Column(Field('data_importasaun', css_class="form-select"), css_class='form-group col-md-6 mb-0'),
			Column('deskrisaun', css_class='form-group col-md-12 mb-0'),
			css_class='row'),



			HTML(""" 
			<br>
				<div class='float-right'>
			<button  id = 'bambuinput' class="btn btn-sm btn-info" type="submit"><i class="fa fa-save"></i> {% if asaun  == 'edit' %} Atualiza {% else %} Rejistu {% endif %}
				</button>

					<a class="btn btn-sm btn-warning" onclick=self.history.back()><span class="btn-label"><i class="fa fa-window-close"></i></span> Kansela</a>
				</div>
				
				""")
		)
		






class GrupuViveirusForm(forms.ModelForm):
	# descriptiond = forms.CharField(label="Observasaun", widget=forms.Textarea(attrs={"rows":2}), required=False)

	class Meta:
		model = GrupuViveirus
		fields = ['naran','suku','deskrisaun','imagen','kontaktu','naran_kordenador']


        

	def __init__(self, *args, **kwargs):
		super(GrupuViveirusForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.fields['suku'].choices=[(item.pk, (str(item.naran) + str(" / Postu  ") + str(item.postu) + str(" / Munisípiu ") + str(item.postu.munisipiu) )) for item in Suku.objects.all()]
		self.helper.form_id = 'form_viveirus'
		self.helper.layout = Layout(
			





			Row(
			Column('naran', css_class='form-group col-md-12 mb-0'),
			Column('naran_kordenador', css_class='form-group col-md-12 mb-0'),
			Column('kontaktu', css_class='form-group col-md-12 mb-0'),
			Column('imagen', css_class='form-group col-md-12 mb-0'),
			Column(Field('suku', css_class="form-select"), css_class='form-group col-md-12 mb-0'),
			# Column('kordinate_centru', css_class='form-group col-md-12 mb-0'),
			# Column('kordinate_area', css_class='form-group col-md-12 mb-0'),

				
			HTML(""" 

			{% if asaun  == 'edit' %}

			<input type='hidden' value='{% if kordinate == 'mamuk' %}  {{kordinate_centru}}  {% else %} {{kordinate}} {% endif %} ' id="kordinate_centru" name='kordinate_centru'>	<input type='hidden'  value ='{{kordinate_area}}' id = 'kordinate_area' name='kordinate_area'>
			{% else %}
			<input type='hidden' value='{% if kordinate != 'mamuk' %}  {{kordinate}} {% endif %}' id="kordinate_centru"  name='kordinate_centru'>	<input type='hidden'  id = 'kordinate_area' name='kordinate_area'>
			{% endif %}
	
	<br>
			 """),


			Column('deskrisaun', css_class='form-group col-md-12 mb-0'),
			# Column('kordinate_centru', css_class='form-group col-md-4 mb-0'),
			css_class='form-row'
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







class AreaBambuForm(forms.ModelForm):
	# descriptiond = forms.CharField(label="Observasaun", widget=forms.Textarea(attrs={"rows":2}), required=False)

	class Meta:
		model = AreaBambu
		fields = ['naran','suku','deskrisaun','imagen','kontaktu','naran_kordenador','kordinate_area']


        

	def __init__(self, *args, **kwargs):
		super(AreaBambuForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.fields['suku'].choices=[(item.pk, (str(item.naran) + str(" / Postu  ") + str(item.postu) + str(" / Munisípiu ") + str(item.postu.munisipiu) )) for item in Suku.objects.all()]
		self.helper.form_id = 'form_viveirus'
		self.helper.layout = Layout(
			





			Row(
			# Column('kordinate_area', css_class='form-group col-md-12 mb-0'),
			Column('naran', css_class='form-group col-md-12 mb-0'),
			Column('naran_kordenador', css_class='form-group col-md-12 mb-0'),
			Column('kontaktu', css_class='form-group col-md-12 mb-0'),
			Column('imagen', css_class='form-group col-md-12 mb-0'),
			Column(Field('suku', css_class="form-select"), css_class='form-group col-md-12 mb-0'),
			# Column('kordinate_centru', css_class='form-group col-md-12 mb-0'),


				
				
			HTML(""" 

			{% if asaun  == 'edit' %}

			<input type='hidden' value=' {{kordinate_centru}}' id="kordinate_centru" name='kordinate_centru'>	<input type='hidden'  value ='{% if kordinate == 'mamuk' %}  {{kordinate_area}}  {% else %} {{kordinate}} {% endif %}' id = 'kordinate_area' name='kordinate_area'>
			{% else %}
			<input type='hidden' value='' id="kordinate_centru"  name='kordinate_centru'>	<input type='hidden'  id = 'kordinate_area' value='{% if kordinate != 'mamuk' %}  {{kordinate}} {% endif %}' name='kordinate_area'>
			{% endif %}
	
	<br>
			 """),


			Column('deskrisaun', css_class='form-group col-md-12 mb-0'),
			# Column('kordinate_centru', css_class='form-group col-md-4 mb-0'),
			css_class='form-row'
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
