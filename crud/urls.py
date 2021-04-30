from django.urls import path
from .views import sign_up
from django.contrib.auth.views import LoginView,LogoutView


app_name='crud'
urlpatterns=[
    path('login/',LoginView.as_view(template_name='login.html'),name="login_url"),
    path('logout/',LogoutView.as_view(template_name='logout.html'),name="logout"),

]