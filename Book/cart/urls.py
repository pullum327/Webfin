from django.urls import path
from . import views
 
app_name = 'cart'
 
urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('wishl/', views.wishl, name='wishl'),
    path('home/', views.product_list, name='home'),
    path('cart/', views.view_cart, name='view_cart'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('home/details/<int:id>', views.details, name='details'),
    path('payment//<int:product_id>/', views.payment, name='payment'),
    path('payment/', views.view_payment, name='view_payment'),
    path('manage/', views.manage, name='manage'),
    path('personal/', views.personal, name='personal'),
    path('products/', views.product_search, name='product_search'),
    
]