from django.urls import path
from .views import home, profile, settings, signin, signup, account_settings, logout_view

urlpatterns =[
    path("" , home),
    path('profile/' , profile),
    path('settings/' , settings),
    path('signin/' , signin),
    path('signup/' , signup),
    path('account-settings/' , account_settings),
    path('logout/' , logout_view),

]