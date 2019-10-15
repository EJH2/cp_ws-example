from django.urls import path

from tasks import views

urlpatterns = [
    path('http', views.http_view, name='http'),
    path('http_error', views.http_error_view, name='http_error'),
    path('ws', views.ws_view, name='ws'),
    path('ws_error', views.ws_error_view, name='ws_error'),
    path('', views.index, name='index')
]
