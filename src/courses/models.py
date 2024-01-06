from django.db import models
from django import forms

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=120)

    # Field validation
    #General format: def clean_<fieldname>
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if title.lower() == 'abc':
            raise forms.ValidationError("This is not a valid title")
        return title