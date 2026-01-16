from django.urls import path
from .views import EvaluateAPIView

urlpatterns = [
    path("evaluate/", EvaluateAPIView.as_view()),
]
