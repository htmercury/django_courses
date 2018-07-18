from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.redirect_home),
    url(r'^courses$', views.index),
    url(r'^courses/create$', views.create),
    url(r'^courses/(?P<course_id>\d+)/confirm$', views.confirm),
    url(r'^courses/(?P<course_id>\d+)/delete$', views.destroy)
]