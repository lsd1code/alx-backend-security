"""
! Writing your own middleware

Middleware factory is a callable that takes a a `get_response` callable param and returns a middleware.
Middleware is a callable that takes a request and returns a response 

! Activating Middleware

To activate the Middleware, add it to the `Middleware` list in `settings.py`
"""

import logging
from django.http import HttpRequest


def logging_middleware(get_response):
    def middleware(request: HttpRequest):
        logging.info(f"User: {request.user}")
        logging.info(f"Request Headers: {request.headers}")
        logging.info(f"Full Path: {request.get_full_path()}")
        logging.info(f"Request Method: {request.method}")

        return get_response(request)

    return middleware
