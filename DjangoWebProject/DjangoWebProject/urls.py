"""
Definition of urls for DjangoWebProject.
"""

from django.conf.urls import include, url
from django.contrib import admin
from adoptions import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', DjangoWebProject.views.home, name='home'),
    # url(r'^DjangoWebProject/', include('DjangoWebProject.DjangoWebProject.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

   url(r'^admin/', admin.site.urls),
   url(r'^$', views.home, name='home'),
   url(r'^adoptions/(\d+)/', views.pet_detail, name='pet_detail')

 ]

