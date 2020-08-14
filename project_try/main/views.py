from django.shortcuts import render
import time
# Create your views here.
from . models import Agregate
from . serializer import AgregateSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class AgregateList(APIView):
    """
    http://0.0.0.0:8001/v1/get-agr/1/2019-08-08and2019-10-18/
    """
    def get(self, request, id_a, ds_de):
        print('START TO DB')
        start = time.time()
        obj = Agregate.objects.filter(number_of_controller=id_a, 
                                        zdate__gte=ds_de.split('and')[0],
                                        zdate__lte=ds_de.split('and')[1])
        print('FINISH TO DB')
        print(f'time is up {time.time() - start}')
        print(len(obj))

        serializer = AgregateSerializer(obj, many=True)
        return Response(serializer.data)

# class GetCorpZoneArgViewSet(APIView):
#     """
#     view for get data with corpus, zone, agregate and range date.
#     format http://0.0.0.0:8001/getcorpzonearg/23/1/1/2019-08-08and2019-10-18/
#     """
#     def get(self, request, id_c, id_z, id_a, ds_de):

#         obj = Controller.objects.filter(id_zone__base_id__pavilion=id_c, id_zone__base_id__zone=id_z, 
#                                         number_of_controller=id_a, 
#                                         id_zone__zdate__gte=ds_de.split('and')[0], 
#                                         id_zone__zdate__lte=ds_de.split('and')[1])
        
#         serializer = GetCorpZoneArgSerializer(obj, many=True)
#         return Response(serializer.data)
   