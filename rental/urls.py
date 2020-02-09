
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_view
from pages import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),

    path('login/', auth_view.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('logout/', auth_view.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
]
