from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'), 
    path('wishlist', views.wishlist, name='wishlist'),
    path('searchlist', views.searchlist, name='searchlist'),
    path('buy', views.buy, name='buy'),
    path('login_user', views.login_user, name='login_user'),
    path('signup', views.signup, name='signup'),
    path('address', views.address, name='address'),
    path('logout_user', views.logout_user, name='logout_user'),
    path('user_profile', views.user_profile, name='user_profile'),
    path('save_address', views.save_address, name='save_address')

]