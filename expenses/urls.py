from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import index, add_expense, edit_expense, delete_expense, search_expenses, expense_category_summary, \
    stats_view, export_csv, export_excel


urlpatterns = [
    path('', index, name='expenses'),
    path('add-expense/', add_expense, name='add-expense'),
    path('edit-expense/<int:pk>/', edit_expense, name='edit-expense'),
    path('delete-expense/<int:pk>/', delete_expense, name='delete-expense'),
    path('search-expenses/', csrf_exempt(search_expenses), name='search_expenses'),
    path('expense_category_summary/', expense_category_summary, name='expense_category_summary'),
    path('stats/', stats_view, name='stats'),
    path('export-csv/', export_csv, name='export-csv'),
    path('export-excel/', export_excel, name='export-excel'),
]
