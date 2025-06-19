from django.urls import path
from django.contrib.auth.views import LoginView
from .views import home, PublicAPIView, ProtectedAPIView, RegisterView

urlpatterns = [
    path('', home, name='home'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('api/public/', PublicAPIView.as_view(), name='public-api'),
    path('api/protected/', ProtectedAPIView.as_view(), name='protected-api'),
    path('api/register/', RegisterView.as_view(), name='register'),
]
