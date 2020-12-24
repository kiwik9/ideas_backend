from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
import random
import json


@api_view(['POST'])
@csrf_exempt
def generateIdea(request):
    data = json.loads(str(request.body, encoding='utf-8'))
    theme = data.get('theme')
    if theme is not None:
        return Response({'idea': random_line('ideas/ideas.txt')}, status=status.HTTP_200_OK)
    return Response({'error': 'No se ha enviado el usuario'}, status=status.HTTP_400_BAD_REQUEST)

def random_line(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)
