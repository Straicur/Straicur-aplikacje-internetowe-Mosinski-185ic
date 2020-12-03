#from django.contrib.auth import get_user_model 


from rest_framework import generics 
from .models import Ksiazka
from .permissions import IsAuthorOrReadOnly 
from rest_framework import filters
from .serializers import KsiazkaSerializer 

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


    