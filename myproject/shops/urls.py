from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_shop, name='register_shop'),
    path('search/', views.search_shops, name='search_shops'),
    path('api/shops/', views.shop_list_api, name='shop_list_api'),
]
