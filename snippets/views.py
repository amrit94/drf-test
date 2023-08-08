from django.http import HttpResponse
from snippets.models import *
from snippets.serializers import *
from rest_framework import mixins, generics, permissions
from django.contrib.auth.models import User
from rest_framework.authentication import BasicAuthentication, SessionAuthentication


def home(request):
    if request.user.is_authenticated:
        html2 = "<h2> Hi "+ request.user.email +"</h2><a href='/api-auth/logout'>Logout</a><br>"
    else:
        html2 = "<a href='/api-auth/login'>Login</a><br>"
    html1  = "<html><body style='text-align:center'>" 
    html3 ="""
                <br><a href='/snippets/'>Snippets</a><br>
                <br><a href='/users/'>Users</a><br>
                <br><a href='/albums/'>Albums</a><br>
                <br><a href='/tracks/'>Tracks</a><br>
                <br><a href='/products/'>Products</a><br>
                <br><a href='/collections/'>Collections</a><br>
                <br><a href='/pdcollections/'>Product Collections</a>
            </body></html>
           """
    html = html1 + html2 + html3
    return HttpResponse(html)


class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    # No Auth required

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    # No Auth required


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # Basic Auth
    authentication_classes = (BasicAuthentication,)
    permission_classes = [permissions.IsAuthenticated]

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # Basic Auth
    authentication_classes = (BasicAuthentication,)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    

class AlbumList(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    # Session Auth
    authentication_classes = (SessionAuthentication,)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class AlbumDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    # Session Auth
    authentication_classes = (SessionAuthentication,)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TrackList(generics.ListCreateAPIView):
    queryset = Track.objects.all()
    serializer_class = AlbumSerializer

class TrackDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Track.objects.all()
    serializer_class = AlbumSerializer
    

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    

class CollectionList(generics.ListCreateAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer

class CollectionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer


class ProductCollectionList(generics.ListCreateAPIView):
    queryset = ProductCollection.objects.all()
    serializer_class = ProductCollectionSerializer

class ProductCollectionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductCollection.objects.all()
    serializer_class = ProductCollectionSerializer
