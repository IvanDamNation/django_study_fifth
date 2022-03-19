from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('',
         LoginView.as_view(template_name='accounts_login.html'),
         name='login'),
    path('logout/',
         LogoutView.as_view(template_name='accounts_logout.html'),
         name='logout'),

]
