"""webs4solution URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from websblog import views
from django.contrib import admin
from django.urls import path,include
from django.conf import settings  # media
from django.conf.urls.static import static  # media



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
path('who-we-are', views.who_we_are, name='who_we_are'),
    path('blog/', views.blog, name='blog'),
    path('blog-details/<slug:slug>/',views.blog_details,name='blog_details'),
path('projects-details/<slug:slug>/',views.projects_details,name='projects_details'),
path('career/', views.career, name='career'),
path('team/', views.team, name='team'),
path('support/', views.support, name='support'),
path('portfolio/', views.portfolio, name='portfolio'),
path('portfolio-details/<slug:slug>/',views.portfolio_details,name='portfolio_details'),
path('contactus/',views.contact_us,name='contact_us'),
# path('footer/',views.contact_us_base,name='contact_us_base'),
path('signup',views.handlesignup,name='handlesignup'),
path('login',views.handleLogin,name='handleLogin'),
path('logout',views.handleLogout,name='handleLogout'),
path('php-development/', views.php_development, name='php_development'),
path('django-web-development-services/', views.django_development, name='django_development'),
path('python-web-development/', views.python_development, name='python_development'),
path('development_process/', views.development_process, name='development_process'),
path('ios-app-development-services/', views.ios_app, name='ios_app'),
path('android-app-development/', views.android_app, name='android_app'),
path('wordpress-development/', views.wordpress_development, name='wordpress_development'),
path('laravel-development/', views.laravel_development, name='laravel_development'),
path('drupal-development/', views.drupal_app, name='drupal_app'),
path('magento-development/', views.magento_app, name='magento_app'),
path('ui-ux-design/', views.ui_ux_design, name='ui_ux_design'),
path('web-development-services/', views.web_development_services, name='web_development_services'),
path('government-e-marketplace/', views.government_e_marketplace, name='government_e_marketplace'),
path('digital-signature-certificate/', views.digital_signature_certificate, name='digital_signature_certificate'),
path('packages/', views.packages, name='packages'),
path('bid-particiaption/', views.bid_particiaption, name='bid_particiaption'),
    path('poit_checklist/', views.poit_checklist, name='poit_checklist')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)