from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'books', views.BookViewSet)
router.register(r'locations', views.LocationViewSet)
router.register(r'booksAvailable', views.BookAvailableViewSet)
router.register(r'booksUnavailable', views.BookUnavailableViewSet)
router.register(r'series', views.SeriesViewSet)
router.register(r'authors', views.AuthorViewSet)
router.register(r'publishers', views.PublisherViewSet)
router.register(r'customers', views.CustomerViewSet)
router.register(r'students', views.StudentViewSet)
router.register(r'professors', views.ProfessorViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
