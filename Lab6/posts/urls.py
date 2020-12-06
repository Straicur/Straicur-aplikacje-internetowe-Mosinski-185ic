from django.urls import path
#from rest_framework.routers import SimpleRouter

from .views import PostList, PostDetail 
from . import views
#from .views import UserViewSet, PostViewSet


urlpatterns = [

     #path('users/', UserList.as_view()),
     #path('users/<int:pk>/', UserDetail.as_view()), 
     path('test_cookie/', views.setcookie, name='test_cookie'),
     path('<int:pk>/', PostDetail.as_view()),
     path('', PostList.as_view()),

]