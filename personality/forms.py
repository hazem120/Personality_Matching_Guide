from django import forms  
from .models import Personality

class PersonalityForm(forms.ModelForm): 
    class Meta: 
        model = Personality
        fields = '__all__' 
        exclude = ['user']