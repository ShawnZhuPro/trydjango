from django.db import models
from django.urls import reverse

# Create your models here.
# Always run makemigrations and migrate when we change models.py
class Product(models.Model):
  title = models.CharField(max_length=120) # max_length is required
  description = models.TextField(blank=True, null=True) # If we don't want a description
  price = models.DecimalField(decimal_places=2, max_digits=10000)
  summary = models.TextField(blank = True, null=False) # blank pertains to the field, null pertains to the DB
  features = models.BooleanField(default=False) # null=True, default=True

  def get_absolute_url(self):
    """Returns the url that points to this product"""
    #return f"/products/{self.id}"
    
    # Makes url based off the name space products, not the entire app
    return reverse('products:product-detail', kwargs={'my_id': self.id})  