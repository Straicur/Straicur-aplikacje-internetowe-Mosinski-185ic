from django.urls import path
#from rest_framework.routers import SimpleRouter

from .views import PostList, PostDetail
#from .views import UserViewSet, PostViewSet


urlpatterns = [
     path('<int:pk>/', PostDetail.as_view()),
     path('', PostList.as_view()),

]