from users import views
from django.urls import path

app_name='users'
urlpatterns = [
    path('register/',views.register,name='reg'),
    path('profile/',views.profile,name='profile'),
]