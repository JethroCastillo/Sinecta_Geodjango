    #Maybe need it in future ->
# from django.contrib.gis.geos import GEOSGeometry
# from django.contrib.gis.db.models.functions import AsGML

from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from .serializers import PredioSerializer
from .models import Predio

# Create your views here.

@csrf_exempt
def PredioApi(request):
    if request.method== 'GET':
        #Get all Predio Data 
        snippets = Predio.objects.all()
        serializer = PredioSerializer(snippets, many=True)
        # this will be returned as GeoJSON
        return JsonResponse(serializer.data, safe= False)
        # get the data from the client
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        # this step convert all the json data to postgis data
        serializer = PredioSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            # this return the data as GeoJson
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

#TODO Delete, Update

### Model for WKT arguments # WKT= 'POLYGON((30 10, 40 40, 20 40, 10 20, 30 10))'