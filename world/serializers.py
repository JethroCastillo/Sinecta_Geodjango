from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import Predio

class PredioSerializer(GeoFeatureModelSerializer):
# "" serializer to GeoJson compatible data """"

    class Meta:
        model= Predio
        geo_field = 'poly' # this file is requred to render geomodels
        fields = '__all__'
