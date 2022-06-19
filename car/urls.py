from django.urls import path
from .views import ListCreateCarAPIView, RetrieveUpdateDestroyCarAPIView, \
    ListCreateCategoryAPIView, \
    RetrieveUpdateDestroyCategoryAPIView, \
    ListCreateBrandAPIView, \
    RetrieveUpdateDestroyBrandAPIView

urlpatterns = [
    path('car/', ListCreateCarAPIView.as_view()),
    path('car/<int:pk>/', RetrieveUpdateDestroyCarAPIView.as_view()),

    path('category/', ListCreateCategoryAPIView.as_view()),
    path('category/<int:pk>/', RetrieveUpdateDestroyCategoryAPIView.as_view()),

    path('brand/', ListCreateBrandAPIView.as_view()),
    path('brand/<int:pk>/', RetrieveUpdateDestroyBrandAPIView.as_view()),
]
