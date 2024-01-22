from django.urls import path 
from . import views
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
path('', views.index, name='index'),
path('contact', views.contact, name='contact'),
path('dashboard', views.dashboard, name='dashboard'),
path('dashboard/appeal_list',views.appeal_list, name='appeal_list'),
path('dashboard/gallery_list',views.gallery_list,name='gallery_list'),
path('dashboard/image',views.create_image,name='create_image'),
path('auth/register/', views.register_user, name='register_user'),
path('auth/login/', views.login1, name='login'),
path('auth/log_out/', views.log_out, name='log_out')

]

