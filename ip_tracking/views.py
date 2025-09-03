from django.shortcuts import render

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def index(request: Request) -> Response:
    return Response("This is a test route")
