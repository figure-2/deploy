from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('<username>/', views.profile, name='profile'),
    path('<username>/follow/', views.follow, name='follow'),
    path('<username>/followers/', views.followers, name='followers'),
    path('<username>/followings/', views.followings, name='followings'),
    path('<username>/like_posts/', views.like_posts, name='like_posts'),
]