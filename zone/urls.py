from django.conf.urls import url,include
from . import views
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from zone import views as core_views

urlpatterns = [
    url(r'^$', views.index, name= 'index'),
    # url(r'^signup/$', core_views.signup, name='signup'),
    # url(r'^explore/$', views.explore, name = 'explore'),
    # # url(r'^profile/(\d+)$', views.profile, name = 'profile'),
    # url(r'^accounts/', include('registration.backends.simple.urls')),
    # url(r'^post/$', views.new_post, name='new_post'),
    # url(r'^search/$', views.search_profile, name='search_profile'),
    # url(r'^add/(\d+)$', views.comment, name='comment'),
    # url(r'^change_profile/(\d+)$', views.change_profile, name='change_profile'),
    

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
