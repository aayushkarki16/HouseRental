from django.urls import path
from rent import views


urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('log', views.log, name='log'),
    path('login_views', views.login_views, name='login_views'),
    path('logout', views.logout_views, name='logout_views'),
    path('add_post', views.add_post, name='add_post'),
    path('add_post_views', views.add_post_views, name='add_post_views'),
    path('success', views.success, name='success'),
    path('deails/<int:id>', views.details, name='details'),
    path('profile/<int:id>', views.profile, name='profile'),
    path('search_rent', views.search_rent, name='search_rent'),
    path('delete_views/<int:id>', views.delete_views, name='delete_views'),
    path('delete_views/<int:id>', views.delete_views, name='delete_views')
]
