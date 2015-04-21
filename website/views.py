from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from website.models import Businesses, Reviews, Users
from website import services

# Create your views here.
def trending(request):
    business = Businesses.objects.filter(business_id="zzucnDH33KlmbkI4rLyQTA").get()

    return render_to_response('trending.html',{'business':business}, context_instance=RequestContext(request))

def results(request):
    if 'search-text' in request.GET:
        search_results = request.GET['search-text']

    close_businesses = services.conduct_search(search_results)

    return render_to_response('results.html', {'businesses':close_businesses,'zip':search_results}, context_instance=RequestContext(request))
    
def details(request, query):
    # sample id: zzucnDH33KlmbkI4rLyQTA

    business_processme = Businesses.objects.filter(business_id=query).get()
    business = services.package_business(business_processme)
    high_activity_users = services.check_users()
    reviews = Reviews.objects.filter(business_id=query).order_by('-review_date').exclude(user_id__in=high_activity_users)  #minus orders by descending 

    return render_to_response('details.html',{'business':business, 'reviews':reviews},context_instance=RequestContext(request))
