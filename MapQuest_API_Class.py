import json
import urllib.parse
import urllib.request
class MapQuest:

    def __init__(self,key):
        self._API_KEY = key
        


    def totalDistance(self,locations):
        """calculates the total distance between all the listed locations""" 
        #check if there are any locations
        if len(locations) <= 1:
            return 0

        else:
            
          baseURL = 'http://open.mapquestapi.com/directions/v2/route'
          total = 0
        #adding 2 locations into queryParameter and putting it through .parse to build url
          for i in range(len(locations)-1):
              place_1 = locations[i]
              place_2 = locations[i+1]
              queryParameter = [('key',self._API_KEY),('from',place_1),('to',place_2)]
              url = baseURL + '?' + urllib.parse.urlencode(queryParameter)
              response = None
            #using try/finally in case we get bad connection and don't want program to crash
              try:
                response = urllib.request.urlopen(url)
                results = json.load(response)
            #need to close the response
              finally:
                if response != None:
                  response.close()
            #adding up total distances 
              total += results['route']['distance']
            
          return total

    def totalTime(self,locations):
        """calculates the total time it will take from each location"""
        #checks if there's anything in locations
        if len(locations) <= 1:
            return 0

        else:
            
          baseURL = 'http://open.mapquestapi.com/directions/v2/route'
          total = 0
         #adding 2 locations into queryParameter and putting it through .parse to build url
          for i in range(len(locations)-1):
            place_1 = locations[i]
            place_2 = locations[i+1]

            queryParameter = [('key',self._API_KEY),('from',place_1),('to',place_2)]
            url = baseURL + '?' + urllib.parse.urlencode(queryParameter)
            response = None
            #using try/finally in case we get bad connection and don't want program to crash
            try:
              response = urllib.request.urlopen(url)
              results = json.load(response)
              #need to close the response
            finally:
              if response != None:
                response.close()
            #adding up total times
            total += results['route']['time']

            
        return total

    def directions(self,locations):
        """returns a string that represents the turn by turn directions from the first to last location"""
        #check if anythingn is in location
        if len(locations) <= 1:
            return ''

        else:
            #adding 2 locations into queryParameter and putting it through .parse to build url
          baseURL = 'http://open.mapquestapi.com/directions/v2/route'
          directions = ''

          for i in range(len(locations)-1):
            place_1 = locations[i]
            place_2 = locations[i+1]

            queryParameter = [('key',self._API_KEY),('from',place_1),('to',place_2)]
            url = baseURL + '?' + urllib.parse.urlencode(queryParameter)
            response = None
            #using try/finally in case we get bad connection and don't want program to crash
            try:
              response = urllib.request.urlopen(url)
              results = json.load(response)
            finally:
              if response != None:
                response.close()
            # adding each maneuver to string variable directions and adding a newline after each time
            for i in range(len(results['route']['legs'][0]['maneuvers'])):
                directions = directions + results['route']['legs'][0]['maneuvers'][i]['narrative'] + '\n'
        return directions 

    def pointOfInterest(self,locations,keyword,results):
        """returns a list of the what you a searching for at the location that you gave with the maximum number of results that you specified"""
        new_results = []

        #getting coordinates so we can search later
        baseURL = 'http://www.mapquestapi.com/geocoding/v1/address'
        coordinates = ''

       
        queryParameter = [('key',self._API_KEY),('location',locations)]
        url = baseURL + '?' + urllib.parse.urlencode(queryParameter)
        response = None

        try:
          response = urllib.request.urlopen(url)
          results2 = json.load(response)
        finally:
          if response != None:
            response.close()
        #formatting the coordinates so it matches the query parameter
        coordinates = str(results2['results'][0]['locations'][0]['latLng']['lng']) +  ',' + str(results2['results'][0]['locations'][0]['latLng']['lat']) 
        #putting all neccessary fields to create url with the specified location information
        otherUrl = 'http://www.mapquestapi.com/search/v4/place'
        queryParameter1 = [('location',coordinates),('sort','distance'),('feedback','false'),('key',self._API_KEY),('pageSize',str(results)),('q',keyword)] 
        url1 = otherUrl + '?' + urllib.parse.urlencode(queryParameter1)
        response1 = None

        try:
          response1 = urllib.request.urlopen(url1)
          results1 = json.load(response1)
        finally:
          if response1 != None:
            response1.close()

        #adding each result to list new_results

        for r in range(len(results1['results'])):
            new_results.append(results1['results'][r]['displayString'])

        return new_results
       

    
            
            
        
    

            
                

            
        
        
        
        


u = MapQuest('po7lt5A2Z4HAOjxXFyJi4P9rHdQxAauA')
v = u.totalDistance(['3750 barranca pkwy, Irvine, CA 92606', '4143 Campus Dr, Irvine, CA 92612', '3333 Bristol St, Costa Mesa, CA'])
z = u.totalTime(['3750 barranca pkwy, Irvine, CA 92606', '4143 Campus Dr, Irvine, CA 92612', '3333 Bristol St, Costa Mesa, CA'])
y = u.directions(['3750 barranca pkwy, Irvine, CA 92606', '4143 Campus Dr, Irvine, CA 92612', '3333 Bristol St, Costa Mesa, CA'])
x = u.pointOfInterest('4143 Campus Dr, Irvine, CA 92612', 'lacoste', 10)
print(x)

                    

            
        
           

        
        


