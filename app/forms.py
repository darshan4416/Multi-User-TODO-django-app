from django.forms import ModelForm
from .models import TODO

class TODOForm(ModelForm):
    class Meta:
        model = TODO
        fields = ['title','priority','status']
        