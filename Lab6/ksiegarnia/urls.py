from django.urls import path
from rest_framework.routers import SimpleRouter
from . import views
#from .views import KsiazkaList, KsiazkaDetail
from .views import UserViewSet, KsiazkaViewSet

urlpatterns = [
    
    #path('users/', UserList.as_view()),
     #path('users/<int:pk>/', UserDetail.as_view()), 

    ##path('<int:pk>/', KsiazkaDetail.as_view()),
     #path('', KsiazkaList.as_view()),

]
router = SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('', KsiazkaViewSet, basename='ksiazka')
urlpatterns = router.urls
