from django.urls import path

from tasks import views

urlpatterns = [
    path('http', views.http_view),
    path('ws', views.ws_view)
]
