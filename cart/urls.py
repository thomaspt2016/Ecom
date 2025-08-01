"""
URL configuration for ecom project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cart import views
app_name = 'cart'

urlpatterns = [
    path('addtocart/<int:i>',views.AddtoCart.as_view(),name='addtocart'),
    path('carview', views.CartView.as_view(), name='cartview'),
    path('removeitem/<int:i>', views.CartReductionView.as_view(), name='removeitem'),
    path('deleteitem/<int:i>', views.DeleteItemView.as_view(), name='deleteitem'),
    path('Qtyupdate/<int:i>', views.QtyUpdateCartView.as_view(), name='Qtyupdate'),
    path('orderview',views.OrderformView.as_view(),name='orderview'),
    path('paymentsuccess/<str:i>',views.PaymentScucess.as_view(),name='paymentsuccess')
]
