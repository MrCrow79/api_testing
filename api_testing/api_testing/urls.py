from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
#...
from rest_framework import routers

from users.views import UserListAPIView, UserDetailAPIView
from users.views import JobPositionListCreateAPIView, JobPositionRetrieveUpdateDestroyAPIView


router = DefaultRouter()

router.register('users', UserListAPIView, basename='user-list')
router.register('users', UserDetailAPIView, basename='user-detail')
router.register('jobpositions', JobPositionListCreateAPIView, basename='jobposition')
router.register('jobpositions', JobPositionRetrieveUpdateDestroyAPIView, basename='jobposition-detail')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('users/', UserListAPIView.as_view(), name='user-list'),
#     path('users/<int:pk>/', UserDetailAPIView.as_view(), name='user-detail'),
#     path('jobpositions/', JobPositionListCreateAPIView.as_view(), name='jobposition-list-create'),
#     path('jobpositions/<int:pk>/', JobPositionRetrieveUpdateDestroyAPIView.as_view(), name='jobposition-detail'),
# ]