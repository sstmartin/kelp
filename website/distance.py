import urllib2

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