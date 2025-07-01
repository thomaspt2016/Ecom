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
from shop import views
app_name = 'shop'

urlpatterns = [
    path('',views.Categoryview.as_view(),name='category'),
    path('subcategory/<int:i>', views.subcategoryview.as_view(), name='subcategory'),
    path('productdetail/<int:i>', views.ProdDetailView.as_view(), name='productdetail'),
    path('Newcat',views.NewCategory.as_view(),name="Newcat"),
    path('newprod',views.Newproduct.as_view(),name='newprod'),
    path('updatecate/<int:i>',views.UpdateCategory.as_view(),name='updatecate'),
    path('deletecate/<int:i>',views.DeleteCategory.as_view(),name='deletecate'),
    path('updateprod/<int:i>',views.UpdateProduct.as_view(),name='updateprod'),
    path('deleteprod/<int:i>',views.DeleteProduct.as_view(),name='deleteprod'),
    path('Proddetail/<int:i>', views.Proddetail.as_view(), name='Proddetail'),
    path('catego/<int:i>',views.Categodetail.as_view(),name='categorydetail')
]
