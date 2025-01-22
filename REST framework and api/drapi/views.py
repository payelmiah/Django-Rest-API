from django.shortcuts import render
from .models import Aiquest
from .serializers import AiquestSerializer
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
        return HttpResponse(json_data, content_type='application/json')  

