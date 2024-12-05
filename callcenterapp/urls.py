from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page or main listing page
    path('import-csv/', views.import_csv, name='import_csv'),  # CSV import view
    path('book/update/<int:book_id>/', views.update_book, name='update_book'),  # Update specific book
]
