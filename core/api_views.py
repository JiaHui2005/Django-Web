from rest_framework import viewsets
from .permisstions import IsOwnerOrReadOnly
from .models import Post
from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    search_fields = ['title', 'content']
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        