from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import index, add_expense, edit_expense, delete_expense, search_expenses


urlpatterns = [
    path('', index, name='expenses'),
    path('add-expense/', add_expense, name='add-expense'),
    path('edit-expense/<int:pk>/', edit_expense, name='edit-expense'),
    path('delete-expense/<int:pk>/', delete_expense, name='delete-expense'),
    path('search-expenses/', csrf_exempt(search_expenses), name='search_expenses'),
]
