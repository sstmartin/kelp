from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from website.models import Businesses, Reviews, Users

# Create your views here.
def trending(request):
    return render_to_response('trending.html')

def results(request):
    if 'search-text' in request.GET:
        search_results = request.GET['search-text']
    return render_to_response('results.html', {'search_results': search_results}, context_instance=RequestContext(request))
    
def details(request):
    return render_to_response('details.html')
