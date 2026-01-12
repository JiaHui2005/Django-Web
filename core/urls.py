from django.urls import path
from . import views
from .views import PostListView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('posts/', PostListView.as_view(), name='post_list'),
    path('contact/', views.contact, name='contact'),
    path('posts/create/', PostCreateView.as_view(), name='post_create'),
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post_update'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
]
