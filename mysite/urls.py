# urls.py 
from django.contrib import admin
from django.urls import include, path
from register import views as v

from django.views.static import serve
from django.conf.urls import url

urlpatterns = [
    path('', include('main.urls')), # main will be the name of your app
    path("register/", v.register, name="register"),
    path('', include("django.contrib.auth.urls")),
    path('admin/', admin.site.urls),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]