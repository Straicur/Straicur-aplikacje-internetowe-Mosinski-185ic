#from django.contrib.auth import get_user_model 


from rest_framework import generics 
from .models import Post
from .permissions import IsAuthorOrReadOnly 

from .serializers import PostSerializer 

class PostList(generics.ListCreateAPIView):
    #permission_classes = (permissions.IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = (permissions.IsAuthenticated,)
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
