from django.urls import path
from api import views
from rest_framework.authtoken.views import obtain_auth_token

app_name="api"
urlpatterns = [

    path('register/',views.register.as_view(),name='register'),
    path('login/',obtain_auth_token,name='login'),
    path('loginout/',views.login.as_view(),name='loginout'),
    path('welcome',views.welcome.as_view(),name='welcome'),
    path('UserDetails/',views.UserDetails.as_view(),name='UserDetails'),
    path('UserDetails/<int:pk>/',views.UserDetails.as_view(),name='UserDetail'),

    
]
