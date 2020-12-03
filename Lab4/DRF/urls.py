from django.contrib import admin
from django.urls import path, include #, re_path

#from rest_framework import permissions
#from drf_yasg.views import get_schema_view
#from drf_yasg import openapi

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('posts.urls')),
    path('api-auth/', include('rest_framework.urls')),
    #path('api/v1/rest-auth/', include('rest_auth.urls')),
   # path('api/v1/rest-auth/registration/', include('rest_auth.registration.urls')),
]
