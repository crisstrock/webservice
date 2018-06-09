from django.conf.urls import url
from usuarios import views

urlpatterns = [
    url(r'^usuarios/$', views.usuario_list),
    url(r'^usuarios/(?P<pk>[0-9]+)/$', views.usuario_detail),
    url(r'^carreras/$', views.carrera_list),
    url(r'^carreras/(?P<pk>[0-9]+)/$', views.carrera_detail),
]