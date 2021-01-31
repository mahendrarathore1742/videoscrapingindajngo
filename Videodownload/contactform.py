from .models import contact;
from django import forms;

 
class contactdata(forms.ModelForm):
	class Meta:
		model=contact;
		fields=('__all__')





