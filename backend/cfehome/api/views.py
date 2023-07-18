import json
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.models import Product
from django.forms.models import model_to_dict
from products.serializers import ProductSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework import status


# ===========================================================
# This code is for to get understand

# @api_view(['GET'])
# @api_view(['POST'])
# def api_home(request, *args, **kwargs):
#     # request -> httprequest -> Django
#     # requst.body
#     # body = request.body # byte string of json data
    # print(body)
    # data = {}
    # try:
    #     data = json.loads(body) # -> string of JSON data -> python Dict
    # except:
    #     pass
    # print(data.keys())
    # '''DRF API VIEW'''
    
    # instance = Product.objects.all().order_by("?").first()
    # data = {}
    # if instance:

        # data['id'] = model_data.id
        # data['title'] = model_data.title
        # data['content'] = model_data.content
        # data['price'] = model_data.price
        # model instance (model_data)
        # turn a  python dict
        # return JSON to client
        # data = model_to_dict(instance, fields=['id', 'title', 'price', 'sale_price'])        
        # serializer = ProductSerializer(instance).data


    # return JsonResponse(data)

        #  return Response(serializer)

# =======================================================================
@api_view(['GET'])
def api_home(request, *args, **kwargs):
    '''This is a get method'''
    
    instance = Product.objects.all().order_by("?").first()
    if instance:
        serializer = ProductSerializer(instance).data
        return Response(serializer)


# =========================================================================

# @api_view(['POST'])
# def api_home(request, *args, **kwargs):

    # '''  This is post method'''

#     serializer = ProductSerializer(data=request.data)
#     if serializer.is_valid():
#         print(serializer.data)
#         # serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)



# ========================================================================
# @api_view(['GET', 'POST'])
# def api_home(request):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         snippets = Product.objects.all()
#         serializer = ProductSerializer(snippets, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# ==============================================================================
# def api_home(request):
#     pass

















