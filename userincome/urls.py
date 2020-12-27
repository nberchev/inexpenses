from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import index, add_income, edit_income, delete_income, search_income


urlpatterns = [
    path('', index, name='income'),
    path('add-income/', add_income, name='add-income'),
    path('edit-income/<int:pk>/', edit_income, name='edit-income'),
    path('delete-income/<int:pk>/', delete_income, name='delete-income'),
    path('search-income/', csrf_exempt(search_income), name='search_income'),
]
