from django.conf.urls import include,url
from .import views
from django.contrib import admin

urlpatterns = [
    #/basic/
    url(r'^$',views.index,name='index'),
    url(r'^admin/',admin.site.urls),
    url(r'^donor/',include('Blood_bank.urls')),
    url(r'^receiver/', include('Blood_bank.urls')),
]