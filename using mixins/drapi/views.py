'''from django.shortcuts import render
from .models import Aiquest
from .serializers import AiquestSerializer
from rest_framework.views import APIView #class based view
from rest_framework.response import Response'''
#Using generic class-based views

from .models import Aiquest #import model class
from .serializers import AiquestSerializer #import serializer class
from rest_framework.generics import GenericAPIView #class based view for CRUD operation 
from rest_framework.mixins import ListModelMixin , CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin #list view mixins for list view and create view mixins for create view



#class based view for list
class AiquestList(ListModelMixin, GenericAPIView):
    queryset = Aiquest.objects.all()
    serializer_class = AiquestSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


#class based view for create 
class AiquestCreate(CreateModelMixin, GenericAPIView):
    queryset = Aiquest.objects.all()
    serializer_class = AiquestSerializer
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

#class based view for retrieve      
class AiquestRetrieve(RetrieveModelMixin, GenericAPIView):
    queryset = Aiquest.objects.all()
    serializer_class = AiquestSerializer
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs) 
    
#class based view for update
class AiquestUpdate(GenericAPIView, UpdateModelMixin):
    queryset = Aiquest.objects.all()
    serializer_class = AiquestSerializer
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

#class based view for delete
class AiquestDelete(GenericAPIView, DestroyModelMixin):
    queryset = Aiquest.objects.all()
    serializer_class = AiquestSerializer
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



 
'''
#class based view
class AiquestCreate(APIView):
    def get(self, request, pk=None, format=None):
        id =pk
        if id is not None:
            #complex data to variable
            ai = Aiquest.objects.get(id = id)
            #python dictionary convert
            serializer = AiquestSerializer(ai)
            #render json
            return Response(serializer.data)
        #complex data to variable
        ai = Aiquest.objects.all()
        #python dictionary convert
        serializer = AiquestSerializer(ai, many=True)
        #render json
        return Response(serializer.data)
    
    
    # post request
    def post(self, request, format=None):
        #stream to python dictionary convert
        serializer = AiquestSerializer(data=request.data)
        #python dictionary to complex data convert
        if serializer.is_valid():
            serializer.save()
            #response = {'msg':'Data successfully inserted'} it is for third party apps
            return Response({'msg':'Data successfully inserted'})
        return Response(serializer.errors)
    
    # put request
    def put(self, request, pk, format=None):
        id = pk
        ai = Aiquest.objects.get(id = id)
        serializer = AiquestSerializer(ai, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data successfully Updated'})
        return Response(serializer.errors)
    
    # patch request
    def patch(self, request, pk, format=None):
        id = pk
        ai = Aiquest.objects.get(id = id)
        serializer = AiquestSerializer(ai, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data successfully Updated'})
        return Response(serializer.errors)
    
    # delete request
    def delete(self, request, pk, format=None):
        id=pk
        ai = Aiquest.objects.get(id = id)
        ai.delete()
        return Response({'msg':'Data successfully Deleted'})
    '''
    
    












"""

# this is a basic example of how to create a REST API using Django Rest Framework

from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import io
from rest_framework.parsers import JSONParser


# create serializer class
#QuerySet
def aiquest_info(request):
    #complex data to variable
    ai = Aiquest.objects.all()
    #python dictionary convert
    serializer = AiquestSerializer(ai, many=True)              #take serializer class from drapi/serializers.py
    #render json
    json_data = JSONRenderer().render(serializer.data)        #take JSONRenderer class from rest_framework.renderers
    #json sent to user
    return HttpResponse(json_data, content_type='application/json')


#model instance (single object)
def aiquest_ins(request, pk):
    #complex data to variable
    ai = Aiquest.objects.get(id = pk)
    #python dictionary convert
    serializer = AiquestSerializer(ai)              #take serializer class from drapi/serializers.py
    #render json
    json_data = JSONRenderer().render(serializer.data)        #take JSONRenderer class from rest_framework.renderers
    #json sent to user
    return HttpResponse(json_data, content_type='application/json')






#deserialization (create)
@csrf_exempt
def aiquest_create(request):
    if request.method == 'POST':
        json_data = request.body
        #json to stream convert
        stream = io.BytesIO(json_data)
        #stream to python dictionary convert
        python_data = JSONParser().parse(stream)        #take JSONParser class from rest_framework.parsers
        #python dictionary to complex data convert
        serializer = AiquestSerializer(data = python_data)              #take serializer class from drapi/serializers.py
        #validation
        if serializer.is_valid():
            serializer.save()
            #success response
            response = {'msg':'Data successfully Created'}
            #python dictionary to json convert
            json_data = JSONRenderer().render(response)        #take JSONRenderer class from rest_framework.renderers
            #json sent to user
            return HttpResponse(json_data, content_type='application/json')
        #error response
        json_data = JSONRenderer().render(serializer.errors)        #take JSONRenderer class from rest_framework.renderers
        #json sent to user
        return HttpResponse(json_data, content_type='application/json')
    
    #update data
    if request.method == 'PUT':
        json_data = request.body
        #json to stream convert
        stream = io.BytesIO(json_data)
        #stream to python dictionary convert
        python_data = JSONParser().parse(stream)        #take JSONParser class from rest_framework.parsers
        #python dictionary to complex data convert
        id = python_data.get('id') #get id
        ai = Aiquest.objects.get(id = id) #get instance
        serializer = AiquestSerializer(ai, data = python_data, partial = True)       #take serializer class from drapi/serializers.py update partial data
        #validation
        if serializer.is_valid():
            serializer.save()
            #success response
            response = {'msg':'Data successfully Updated'}
            #python dictionary to json convert
            json_data = JSONRenderer().render(response)        #take JSONRenderer class from rest_framework.renderers
            #json sent to user
            return HttpResponse(json_data, content_type='application/json')
        #error response
        json_data = JSONRenderer().render(serializer.errors)        #take JSONRenderer class from rest_framework.renderers
        #json sent to user
        return HttpResponse(json_data, content_type='application/json')

    #delete data
    if request.method == 'DELETE':
        #complex data to variable
        json_data = request.body
        #json to stream convert
        stream = io.BytesIO(json_data)
        #stream to python dictionary convert  
        python_data = JSONParser().parse(stream)        #take JSONParser class from rest_framework.parsers
        #python dictionary to complex data convert
        id = python_data.get('id') #get id
        ai = Aiquest.objects.get(id = id) #get instance
        ai.delete()
        #success response
        response = {'msg':'Data successfully Deleted'}
        #python dictionary to json convert
        json_data = JSONRenderer().render(response)        #take JSONRenderer class from rest_framework.renderers
        #json sent to user
        return HttpResponse(json_data, content_type='application/json')  """

