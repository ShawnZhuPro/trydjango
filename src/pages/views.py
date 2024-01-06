from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# Place that handles various web pages
def home_view(request, *args, **kwargs):
  print(args, kwargs)
  print(request.user)
  # return HttpResponse("<h1>Hello World</h1>")
  return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
  # return HttpResponse("<h1>Contact Page</h1>")
  my_context = {
    "title": "This is about us",
    "my_number": 123,
    "my_list": [123,234,345],
    "my_html": "<h1>This is my html</h1>"
  }
  return render(request, "contact.html", my_context)
