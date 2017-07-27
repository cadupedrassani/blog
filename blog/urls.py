from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^home/', views.post_list),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail),
    url(r'^postnew/', views.post_new),
    url(r'^$', views.logar),
]