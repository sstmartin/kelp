from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from website.models import Businesses, Reviews, Users

# Create your views here.
def index(request):
    return render_to_response('index.html')