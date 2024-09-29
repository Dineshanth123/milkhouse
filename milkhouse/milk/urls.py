from django.urls import path
from . import views

urlpatterns = [
    # Seller URLs
    path('sellers/', views.seller_list, name='seller_list'),
    path('sellers/<int:id>/', views.seller_detail, name='seller_detail'),

    # Buyer URLs
    path('buyers/', views.buyer_list, name='buyer_list'),
    path('buyers/<int:id>/', views.buyer_detail, name='buyer_detail'),
]
