from django.conf.urls import url
from . import views           # This line is new!

#models -- views -- templates

urlpatterns = [
  url(r'^$', views.index),     # This line has changed!
 ]