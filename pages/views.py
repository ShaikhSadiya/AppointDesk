from tempfile import template

from django.shortcuts import render

def home_view(request):
    template_name ='pages/home.html'
    context = {}
    return  render (request, template_name, context)

def about_view(request):
    template_name ='pages/about.html'
    context = {}
    return render(request, template_name, context)
