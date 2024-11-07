from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),  # Main page displaying all orders
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('order/<int:order_id>/<str:new_status>/', views.update_order_status, name='update_order_status'),
]
