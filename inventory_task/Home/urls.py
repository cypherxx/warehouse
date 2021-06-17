from django.urls import path,include
from . import views

urlpatterns = [
    
    path('',views.index,name='index'),
    path('view_product_movement/',views.Product_movement_view,name='view_product_movement'),
    path('view_products/',views.Product_view,name='view_products'),
    path('view_locations/',views.Location_view,name='view_locations'),
    path('add_product_movement/', views.add_product_movement, name='add_product_movement'),
    path('add_product/', views.add_product, name='add_product'),
    path('add_location/', views.add_location, name='add_location'),

]
