from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='vaccine-home'),
    path('search-centers', views.search_center, name='search-center'),
    path('book-vaccines', views.BookVaccineView.as_view(), name='book-vaccine'),
]