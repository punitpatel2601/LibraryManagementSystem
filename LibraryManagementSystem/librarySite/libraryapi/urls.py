from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'books', views.BookViewSet)
router.register(r'locations', views.LocationViewSet)
router.register(r'booksStatus', views.BookStatusViewSet)
router.register(r'series', views.SeriesViewSet)
router.register(r'authors', views.AuthorViewSet)
router.register(r'publishers', views.PublisherViewSet)
router.register(r'persons', views.PersonViewSet)
router.register(r'students', views.StudentViewSet)
router.register(r'professors', views.ProfessorViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('register/', views.register),
    path('login/', views.login),
    path('index/', views.index),
    path('welcome/', views.welcome),
    path('login/notSuccess/', views.unsuccessful),
    path('welcome/viewBooks/', views.display_books),
    path('welcome/searchBook/', views.search_book),
    path('searchBook/', views.search_book),
    path('selectBook/', views.borrow_book),
    path('welcome/selectBook/', views.borrow_book),
    path('welcome/viewBooks/selectBook/', views.borrow_book),
]
