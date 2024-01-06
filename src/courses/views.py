from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from .forms import CourseModelForm
from .models import Course

# Create your views here.

class CourseObjectMixin(object):
    model = Course
    def get_object(self):
        id = self.kwargs.get('id')
        obj = None
        if id is not None:
            obj = get_object_or_404(self.model, id=id)
        return obj 
    
class CourseDeleteView(CourseObjectMixin, View):
    template_name = "courses/course_delete.html" # DetailView
    def get(self, request, id=None, *args, **kwargs):
        # GET method
        context = {}
        obj = self.get_object()
        if obj is not None:
            context['object'] = obj
        return render(request, self.template_name, context)

    def post(self, request, id=None,  *args, **kwargs):
        # POST method
        context = {}
        obj = self.get_object()
        if obj is not None:
            obj.delete()
            context['object'] = None
            return redirect('/courses/')
        return render(request, self.template_name, context)

class CourseUpdateView(CourseObjectMixin, View):
    template_name = "courses/course_update.html" # DetailView

    def get(self, request, id=None, *args, **kwargs):
        # GET method
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = CourseModelForm(instance=obj)
            context['object'] = obj
            context['form'] = form
        return render(request, self.template_name, context)

    def post(self, request, id=None,  *args, **kwargs):
        # POST method
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = CourseModelForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
            context['object'] = obj
            context['form'] = form
        return render(request, self.template_name, context)

class CourseCreateView(View):
  template_name = "courses/course_create.html"  #DetailView
  # "id=None" means that id is not required
  def get(self, request, *args, **kwargs):
    # GET method
    form = CourseModelForm()
    context = {"form": form}
    return render(request, self.template_name, context)
  
  def post(self, request, *args, **kwargs):
    # POST method
    # Allows form data to go through
    form = CourseModelForm(request.POST)
    if form.is_valid():
      form.save()
      form = CourseModelForm()  # Reinitialize form so the form is empty
    context = {"form": form}
    return render(request, self.template_name, context)

class CourseListView(View):
  template_name = "courses/course_list.html"
  queryset = Course.objects.all()

  def get_queryset(self):
    return Course.objects.all()

  def get(self, request, *args, **kwargs):
    context = {'object_list': self.get_queryset()}
    return render(request, self.template_name, context)
  
# class MyListView(CourseListView):
#   queryset = Course.objects.filter(id=1)


class CourseView(CourseObjectMixin, View):
  template_name = "courses/course_detail.html"  #DetailView
  # "id=None" means that id is not required
  def get(self, request, id=None, *args, **kwargs):
    # GET method
    context = {'object': self.get_object()}
    #if id is not None:
      #obj = get_object_or_404(Course, id=id)
      #context['object'] = obj
    return render(request, self.template_name, context)
  
  # def post(request, *args, **kwargs):
  #   return render(request, 'contact.html', {})


# HTTP METHODS
# function-based view
def my_fbv(request, *args, **kwargs):
  return render(request, 'contact.html', {})