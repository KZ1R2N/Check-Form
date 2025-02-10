from django.urls import path
from . import views  # Import views from the same app

urlpatterns = [
    path('', views.form_view, name='form_view'),
    path('show_data/', views.show_data, name='show_data'),
]
