from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def products_list(request):

    print('good job')
    return Response('good job')

@api_view([])
def product_detail():
    pass