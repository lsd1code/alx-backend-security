from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django_ratelimit.decorators import ratelimit


@api_view(['GET'])
def index(request: Request) -> Response:
    return Response("This is a test route")


def get_rate(g, r): return '10/m' if r.user.is_authenticated else '5/m'


@ratelimit(key='ip', rate=get_rate, block=True)
@api_view(['POST'])
def login(request: Request) -> Response:
    return Response("This is a test route")
