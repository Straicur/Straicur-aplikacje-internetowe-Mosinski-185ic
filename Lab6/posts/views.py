#from django.contrib.auth import get_user_model 


from rest_framework import generics 
from .models import Post
from .permissions import IsAuthorOrReadOnly 
from django.http import HttpResponse  
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

def setcookie(request):
    html = HttpResponse("<h1>Cookie</h1>")
    if request.COOKIES.get('visits'):
        html.set_cookie('dataflair', 'Welcome Back')
        value = int(request.COOKIES.get('visits'))
        html.set_cookie('visits', value + 1)
    else:
        value = 1
        text = "Welcome for the first time"
        html.set_cookie('visits', value)
        html.set_cookie('dataflair', text)
    return html