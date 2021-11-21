from django.shortcuts import render
import requests
import json
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.


@api_view(['GET',])
def get_api(request):
    response = {
            'status':200,
            'message': "success",
            }
    return JsonResponse(response)


@api_view(['POST',])
def post_api(request):
    if request.method == "POST":
        name = request.POST['name']
        age = request.POST['age']
        response = {
                'status':200,
                'message': "success",
                'name': name,
                'age':age
                }
        return JsonResponse(response)