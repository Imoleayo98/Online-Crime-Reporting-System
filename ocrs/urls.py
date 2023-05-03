"""ocrs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from . import settings
from . import views
from django.contrib.auth.decorators import login_required



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.landing_page, name='landing_page'),
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('index/', views.index, name='index'),
    path('administrator/', views.administrator, name='administrator'),
    path('user/', include('complaints.urls'), name='user'),
    path('police/', views.police, name='police'),
    path('test/', views.test, name='test'),
    path('get_district/', views.get_districts, name='get_districts'),
    path('get_police_stations/', views.get_police_stations, name='get_police_stations'),
    path('get_districts_register/', views.get_districts_register, name='get_districts_register'),
    path('police_incharge_home/', views.police_incharge_home, name='police_incharge_home'),
    path('manage_complaint/<int:complaint_id>/', views.manage_complaint, name='manage_complaint'),
    path('police_incharge_view_complaint/', views.police_incharge_view_complaint, name='police_incharge_view_complaint'),
    path('register_fir_csr/', views.register_fir_csr, name='register_fir_csr'),
    path('view_fir/', views.view_fir, name='view_fir'),
    path('manage_fir/<int:fir_id>/', views.manage_fir, name='manage_fir'),
    path('view_csr/', views.view_csr, name='view_csr'),
    path('manage_csr/<int:csr_id>/', views.manage_csr, name='manage_csr'),
    path('view_only_fir/<int:fir_id>/', views.view_only_fir, name='view_only_fir'),
    path('view_only_csr/<int:csr_id>/', views.view_only_csr, name='view_only_csr'),
    path('view_only_firs/', views.view_only_firs, name='view_only_firs'),
    path('view_only_csrs/', views.view_only_csrs, name='view_only_csrs'),

] + static(settings.STATIC_URL, document_root=settings.BASE_DIR / 'static') + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)