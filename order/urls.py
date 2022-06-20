from django.urls import path
from .views import RetrieveUpdateDestroyOrderAPIView, ListCreateOrderView

urlpatterns = [
    path('', ListCreateOrderView.as_view()),
    path('<int:pk>/', RetrieveUpdateDestroyOrderAPIView.as_view()),
]
