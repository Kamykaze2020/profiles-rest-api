# from django.shortcuts import render
# The rest_framework is the Django rest framework that we isntalled in our requirements.txt
from rest_framework.views import APIView
# imports the response object which is used to return responses from the api view
# so when you call(django rest api) the api view it's expected to return this standard response object
from rest_framework.response import Response

# Create your views here.
class HelloApiView(APIView):
    """Test API View"""

    # request object that is pasted in by the django rest framework and contains details of the request beeing made to the api
    # format which is used to add a format suffix to our url.
    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Givew you the most control over your application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
