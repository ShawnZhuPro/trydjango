from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from django.views.generic import (
  CreateView,
  DetailView,
  ListView,
  UpdateView,
  ListView,
  DeleteView
)

from .models import Article
from .forms import ArticleModelForm
# Create your views here.

class ArticleListView(ListView):
  template_name = 'articles/article_list.html'
  queryset = Article.objects.all() # blog/<modelname>_list.html

class ArticleDetailView(DetailView):
  template_name = 'articles/article_detail.html'
  # has the ability to limit the choices available for the detail view (not needed to function)
  #Ex: Article.objects.filter(id__gt=1) --> Only uses id's greater than 1
  queryset = Article.objects.all() 

  def get_object(self):
    id_ = self.kwargs.get("id")
    return get_object_or_404(Article, id=id_)
  
class ArticleCreateView(CreateView):
  template_name = 'articles/article_create.html'
  form_class = ArticleModelForm
  queryset = Article.objects.all()
  # Changes the path by overriding the success_url 
  #success_url = '/'

  def form_valid(self, form):
    print(form.cleaned_data)
    return super().form_valid(form)
  
  # Changes the path by overriding the success_url 
  # def get_success_url(self):
  #   return '/'

class ArticleUpdateView(UpdateView):
  template_name = 'articles/article_create.html'
  form_class = ArticleModelForm
  queryset = Article.objects.all()

  # "grabs" the object
  def get_object(self):
    id_ = self.kwargs.get("id")
    return get_object_or_404(Article, id=id_)

  def form_valid(self, form):
    print(form.cleaned_data)
    return super().form_valid(form)
  
class ArticleDeleteView(DeleteView):
  template_name = 'articles/article_delete.html'
  queryset = Article.objects.all() 

  def get_object(self):
    id_ = self.kwargs.get("id")
    return get_object_or_404(Article, id=id_)
  
  # Changes the path after deleting the object by overriding the success_url 
  def get_success_url(self):
    return reverse('articles:article-list')