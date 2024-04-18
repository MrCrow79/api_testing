from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.routers import DefaultRouter


schema_view = get_schema_view(
    openapi.Info(
        title="DA",
        default_version='v1',
        description="Django app for testing",
    ),
    public=True,
)


from users.views import UserListAPIView, UserDetailAPIView
from users.views import JobPositionListCreateAPIView, JobPositionRetrieveUpdateDestroyAPIView


router = DefaultRouter()

router.register('users', UserListAPIView, basename='user-list')
router.register('users', UserDetailAPIView, basename='user-detail')
router.register('jobpositions', JobPositionListCreateAPIView, basename='jobposition')
router.register('jobpositions', JobPositionRetrieveUpdateDestroyAPIView, basename='jobposition-detail')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('users/', UserListAPIView.as_view(), name='user-list'),
#     path('users/<int:pk>/', UserDetailAPIView.as_view(), name='user-detail'),
#     path('jobpositions/', JobPositionListCreateAPIView.as_view(), name='jobposition-list-create'),
#     path('jobpositions/<int:pk>/', JobPositionRetrieveUpdateDestroyAPIView.as_view(), name='jobposition-detail'),
# ]