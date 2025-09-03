"""
! Writing your own middleware

Middleware factory is a callable that takes a a `get_response` callable param and returns a middleware.
Middleware is a callable that takes a request and returns a response 

! Activating Middleware

To activate the Middleware, add it to the `Middleware` list in `settings.py`

! IP Blocking

Ensure that the middleware component blocks requests from IPs in `BlockedIP` model, then return `403_Forbidden` status
"""

import logging
from django.http import HttpRequest, HttpResponse
from django.views.decorators.cache import cache_page
from rest_framework.status import HTTP_403_FORBIDDEN
from django_ip_geolocation.decorators import with_ip_geolocation

from ip_tracking.models import (
    RequestLog,
    BlockedIP
)


def logging_middleware(get_response):
    """
    Middleware that logs incoming HTTP requests and blocks requests from IP addresses listed in BlockedIP.
    Args:
        get_response (callable): The next middleware or view to be called.
    Returns:
        callable: The middleware function that processes the request.
    Behavior:
        - Checks if the request's IP address is in the BlockedIP model. If blocked, returns a 403 response.
        - Logs request method, IP address, user, headers, and full path.
        - Creates a RequestLog entry with the IP address and request path.
        - Passes the request to the next middleware or view.
    """

    @with_ip_geolocation
    @cache_page(60 * 24)
    def middleware(request: HttpRequest):
        ip_address = request.META['REMOTE_ADDR']
        exists = BlockedIP.objects.filter(ip_address=ip_address).exists()

        if exists:
            return HttpResponse("This IP Address has been blocked", HTTP_403_FORBIDDEN)

        logging.info(f"REQUEST METHOD: {request.method}")
        logging.info(f"IP ADDRESS: {ip_address}")
        logging.info(f"USER: {request.user}")
        logging.info(f"REQUEST HEADERS: {request.headers}")
        logging.info(f"FULL PATH: {request.get_full_path()}")

        city = request.geolocation['city']  # type:ignore
        country = request.geolocation['country']  # type:ignore

        RequestLog.objects.create(
            ip_address=ip_address,
            path=request.get_full_path(),
            country=country,
            city=city
        )

        return get_response(request)
    return middleware
