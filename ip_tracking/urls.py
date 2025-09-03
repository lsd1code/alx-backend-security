from django.urls import path
from ip_tracking.views import index

urlpatterns = [
    path('home/', index, name='index')
]