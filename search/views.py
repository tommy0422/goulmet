from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.
class SearchView(ListView):
    model = ''
    template_name = 'search/search.html'

