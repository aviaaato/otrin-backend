from django.urls import path

from .views import CategoryView, ProductView, StoreView, PriceView

urlpatterns = [
    path('categories/', CategoryView.as_view()),
    path('products/', ProductView.as_view()),
    path('stores/', StoreView.as_view()),
    path('prices/', PriceView.as_view()),
]