from django.contrib.auth import get_user_model 
from datetime import datetime
from rest_framework import generics 
from .models import Ksiazka
from .permissions import IsAuthorOrReadOnly ,IsAssigned
from rest_framework import filters , generics, permissions ,viewsets
from .serializers import KsiazkaSerializer  , UserSerializer
from rest_framework import permissions
class KsiazkaViewSet(viewsets.ModelViewSet): 
    permission_classes = (permissions.IsAuthenticated,IsAuthorOrReadOnly)
    queryset = Ksiazka.objects.all()
    serializer_class = KsiazkaSerializer
    filter_backends = [filters.SearchFilter ,filters.OrderingFilter]
    search_fields = ['title']   

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,IsAuthorOrReadOnly)
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter ,filters.OrderingFilter]
    search_fields = ['username']




""" 
class KsiazkaList(generics.ListCreateAPIView):
    #permission_classes = (permissions.IsAuthenticated,)
    queryset = Ksiazka.objects.all()
    serializer_class = KsiazkaSerializer
    filter_backends = [filters.SearchFilter ,filters.OrderingFilter]
    search_fields = ['title']
    #ordering_fields = ['title']
class KsiazkaDetail(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = (permissions.IsAuthenticated,)
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Ksiazka.objects.all()
    serializer_class = KsiazkaSerializer
"""

    