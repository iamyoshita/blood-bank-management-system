from django.conf.urls import url
from .import views


urlpatterns = [
     #/music/
    url(r'^donor/',views.all_donors,name='index'),
    url(r'^receiver/',views.all_receivers,name='ind'),
    #music/74/
     #url(r'^(?P<album_id>[0-9]+)/$',views.detail,name='detail'),

]