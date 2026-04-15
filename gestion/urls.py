from django.urls import path
from . import views

urlpatterns = [
    path("", views.prod_list, name='prod_list'),
    path('prod/<int:pk>/', views.prod_detail, name='prod_detail'),
    path('prod/new/', views.prod_new, name='prod_new'),
    path('prod/<int:pk>/edit/', views.prod_edit, name='prod_edit'),
    path('prod/<int:pk>/supprimer', views.prod_supprim, name='prod_supprim')
]

