from django.urls import path

from .views import CategoryView, ProductView, StoreView

urlpatterns = [
    path('categories/', CategoryView.as_view()),
    path('products/', ProductView.as_view()),
    path('stores/', StoreView.as_view()),
]