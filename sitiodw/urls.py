from datetime import datetime
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from portal import forms, views

urlpatterns = [
    path('', views.vista_inicio, name='inicio'),
    path('about/', views.vista_acercade, name='acercade'),
    path('contact/', views.vista_contactenos, name='contactenos'),
    path('login/',
        LoginView.as_view
        (
            template_name='portal/login.html',
            authentication_form=forms.LoginUsuarioForm,
            extra_context=
            {
                'titulo': 'Ejemplo MiApp',
                'fecha': datetime.now().year,
            }
        ),
        name='acceso'),
    path('logout/', LogoutView.as_view(next_page='/'), name='salir'),
    path('admin/', admin.site.urls),
]
