from django.urls import path
from . import views

urlpatterns = [
    path('sellers/', views.seller_list, name='seller_list'),
    path('sellers/add/', views.seller_add, name='seller_add'),
    path('sellers/<int:seller_id>/', views.seller_detail, name='seller_detail'),
    path('sellers/<int:seller_id>/edit/', views.seller_edit, name='seller_edit'),
    path('sellers/<int:seller_id>/delete/', views.seller_delete, name='seller_delete'),
    
    path('buyers/', views.buyer_list, name='buyer_list'),
    path('buyers/add/', views.buyer_add, name='buyer_add'),
    path('buyers/<int:buyer_id>/', views.buyer_detail, name='buyer_detail'),
    path('buyers/<int:buyer_id>/edit/', views.buyer_edit, name='buyer_edit'),
    path('buyers/<int:buyer_id>/delete/', views.buyer_delete, name='buyer_delete'),

    path('transactions/', views.transaction_list, name='transaction_list'),
    path('transactions/add/', views.add_transaction, name='add_transaction'),
]
