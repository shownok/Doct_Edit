from django.forms import ModelForm
from . models import document

class documentsForm(ModelForm):
    class Meta:
        model = document
        fields = '__all__'
