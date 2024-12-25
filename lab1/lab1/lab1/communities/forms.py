from django import forms 
from . import models 

class CreatePost(forms.ModelForm): 
    class Meta: 
        model = models.Communities
        fields = ['name','description','slug','free','banner']