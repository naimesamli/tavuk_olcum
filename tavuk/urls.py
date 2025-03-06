from django.urls import path
from .views import tavuk_olcum_view

urlpatterns = [
    path('', tavuk_olcum_view, name='tavuk_olcum_view'),
]
