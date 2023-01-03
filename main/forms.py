from django.forms import ModelForm
from django import forms
from .models import *

class Formone(forms.ModelForm):
	class Meta:
		model=Form1
		fields=('name','email','age',)
class Formstwo(forms.ModelForm):
	class Meta:
		model=Form1
		fields=('date_of_birth','nationality',)

class Formthree(forms.ModelForm):
	class Meta:
		model=Form2
		fields=('file','last_level_of_studying','number_of_children_in_the_family','number_of_family_members','Family_total_income_level',)
class Formfour(forms.ModelForm):
	class Meta:
		model=Form2
		fields=('letter_to_manager',)