from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from website.models import Businesses, Reviews, Users

# Create your views here.
def trending(request):
    return render_to_response('trending.html')

def results(request):
    return render_to_response('results.html')

def details(request):
    return render_to_response('details.html')