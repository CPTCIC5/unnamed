from django.urls import path
from .views import LoginView,SignupView,UserViewSet,ChangePasswordView,LogoutView
from rest_framework import routers


router = routers.DefaultRouter()



router.register('users', UserViewSet, basename='users')
urlpatterns= [
    path('login/', LoginView.as_view(), name="login"),
    path('register/', SignupView.as_view(), name="signup"),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('logout/', LogoutView.as_view(), name='logout')
    
] + router.urls