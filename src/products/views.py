from django.shortcuts import render, get_object_or_404, redirect

# "." indicates current directory
from .models import Product
from .forms import ProductForm, RawProductForm

# Create your views here.
# Place that handles various web pages
def product_detail_view(request):
  obj = Product.objects.get(id=1)
  # context = {
  #   'title': obj.title,
  #   'description': obj.description,
  # }
  context = {
    'object': obj
  }
  return render(request, 'products/product_detail.html', context)  

def render_initial_data(request):
  initial_data = {
    'title': "My awesome title"
  }
  # editing model form data + setting initial data
  # remove "initial = initial_data" for editing
  obj = Product.objects.get(id=1)
  form = ProductForm(request.POST or None, initial = initial_data, instance=obj)
  if form.is_valid():
    form.save()
  context = {
    'form': form
  }
  return render(request, 'products/product_create.html', context)  

def dynamic_lookup_view(request, my_id):
  #obj = Product.objects.get(id=my_id)
  obj = get_object_or_404(Product, id=my_id)
  context = {
    "object": obj
  }
  return render(request, "products/product_detail.html", context)

def product_delete_view(request, my_id):
  obj = get_object_or_404(Product, id=my_id)
  if request.method == "POST":
    # Confirming delete
    obj.delete()
    return redirect('home')
  context = {
    "object": obj
  }
  return render(request, "products/product_delete.html", context)

def product_list_view(request):
  queryset = Product.objects.all() # list of objects
  context = {
    "object_list": queryset # page object that contains the list of objects
  }
  return render(request, "products/product_list.html", context)

def product_create_view(request):
  form = ProductForm(request.POST or None)
  if form.is_valid():
    form.save()
    # Rerenders the data to remove previous text in the form
    form = ProductForm()
  context = {
    'form': form
  }
  return render(request, 'products/product_create.html', context)  

# def product_create_view(request):
#   # Don't use GET for getting data, use POST because it's safer
#   # This is a bad way of saving data
#   if request.method == "POST":
#     my_new_title = request.POST.get('title')
#     # Product.objects.create(title=my_new_title)
#   context = {}
#   return render(request, 'products/product_create.html', context)  

# def product_create_view(request):
#   # When the request method is not a POST, the RawProductForm form is 
#   #not bound to any data, so an empty form is rendered to the user.
#   my_form = RawProductForm()
#   if request.method == "POST":
#     my_form = RawProductForm(request.POST)
#     if my_form.is_valid():
#       # now the data is good
#       print(my_form.cleaned_data)
#       Product.objects.create(**my_form.cleaned_data)
#     else:
#       print(my_form.errors)
#   context = {
#     'form': my_form,
#   }
#   return render(request, 'products/product_create.html', context)  