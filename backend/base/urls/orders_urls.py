from django.urls import path
from base.views import order_view as  views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)

urlpatterns = [
    path('add/',views.addOrderItems,name='orders-add'),
    path('<str:pk>/deliver/',views.updateOrderToDelivered,name='delivered-order'),
    path('myorders/',views.getMyOrders,name='my-orders'),
    path('',views.myOrders,name='orders'),
    
    path('<str:pk>/',views.getOrderById,name='user-order'),
    path('<str:pk>/pay/',views.updateOrderToPaid,name='pay'),

]