import urllib2
from website.models import Businesses, Reviews, Users

def distance(zip1, zip2):
    #zip1 = '30068'
    #zip2 = '30318'
    zip1 = str(zip1)
    zip2 = str(zip2)
    request = 'http://www.zipcodeapi.com/rest/l9VQZwNPcw1P7b6dThOQ8XDRnfZ90lzluvbu2Ykevl4DxbRrsGhADUs1arbaMLvh/distance.csv/' + zip1 + '/' + zip2 + '/mile'
    response = urllib2.urlopen(request)
    distance = response.read()
    distance = distance[9:-2]
    #returns distance in miles
    return distance

def conduct_search(zip):
    businesses = Businesses.objects.all().filter(full_address__contains=zip).filter(stars=5).order_by('-review_count')[0:10]
    #dist = distance(zip,21104)

    return businesses

def package_business(business):
    temp = {
        'name':business.business_name,
        'address':business.full_address,
        'categories':business.categories,
        'reviews':business.review_count,
        'stars':business.stars,
        'longitude':business.longitude,
        'latitude':business.latitude
    }
    temp['categories'] = temp['categories'].replace('"','').replace('[','').replace(']','').replace(',',', ')
    return temp
    
def check_users():
	high_users = Users.objects.all().filter(average_stars__gte=5).values('user_id')
	return high_users    
