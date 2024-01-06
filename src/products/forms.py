from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
  title = forms.CharField(label='my new title', widget=forms.TextInput(attrs={"placeholder": "Your title"}))
  description = forms.CharField(
    required=False, 
    widget=forms.Textarea(
      attrs={
        "class": "new-class-name two",
        "id": "my-id-for-textarea",
        "rows": 20,
        "cols": 120,
        "placeholder": "Your description"
      }))
  price = forms.DecimalField(initial=199.99)
  class Meta:
    model = Product
    fields = [
      'title',
      'description',
      'price'
    ]

  # Use this if you want a certain field to contain a certain phrase
  # Syntax: def clean_<my_field_name>
  def clean_title(self, *args, **kwargs):
    title = self.cleaned_data.get("title")
    if not "test" in title:
      raise forms.ValidationError("Title must include the word 'test'")
    return title

class RawProductForm(forms.Form):
  title = forms.CharField(label='my new title', widget=forms.TextInput(attrs={"placeholder": "Your title"}))
  description = forms.CharField(
    required=False, 
    widget=forms.Textarea(
      attrs={
        "class": "new-class-name two",
        "id": "my-id-for-textarea",
        "rows": 20,
        "cols": 120,
        "placeholder": "Your description"
      }))
  price = forms.DecimalField(initial=199.99)