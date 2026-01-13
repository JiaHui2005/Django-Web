from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from .api_views import PostViewSet


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]

router = DefaultRouter()
router.register(r'api/posts', PostViewSet, basename='post')

urlpatterns += router.urls
