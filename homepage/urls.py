from django.conf.urls import url, include
from homepage import views
from photologue.views import *

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^curriculum-vitae/$', views.cv, name='cv'),
]
