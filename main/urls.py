from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='main/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('russia/', views.russia, name='russia'),
    path('japan/', views.japan, name='japan'),
    path('india/', views.india, name='india'),
    path('china/', views.china, name='china'),
    path('italy/', views.italy, name='italy'),
    path('ireland/', views.ireland, name='ireland'),
    path('iceland/', views.iceland, name='iceland'),
    path('germany/', views.germany, name='germany'),
    path('france/', views.france, name='france'),
    path('austria/', views.austria, name='austria'),
    path('profile/', views.profile_view, name='profile'),
    path('test/', views.test_view, name='test'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='main/password_change.html', success_url='/profile/'),
         name='password_change'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


