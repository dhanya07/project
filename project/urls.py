"""project URL Configuration

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
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.conf.urls.static import static
from siteadmin import views as siteadmin_view
from educator import views as educator_view
from user import views as user_view
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',siteadmin_view.login),
    url('login/',siteadmin_view.login,name='login'),
    url('educators/',siteadmin_view.educatorregister,name='educators'),
    url('educatorregisteraction/',siteadmin_view.educatorregisteraction,name='educatorregisteraction'),
    url('users/',siteadmin_view.userregister,name='users'),
    url('userregisteraction/',siteadmin_view.userregisteraction,name='userregisteraction'),
    url('loginaction/',siteadmin_view.loginaction,name='loginaction'),
    url('viewall',siteadmin_view.alleducator,name='viewall'),
    url('approve/(?P<uid>\d+)/$',siteadmin_view.approve,name='approve'),
    url('skill/',siteadmin_view.skill,name='skill'),
    url('skillaction/',siteadmin_view.skillaction,name='skillaction'),
    url('tim/',siteadmin_view.tim,name='tim'),
    url('timeaction/',siteadmin_view.timeaction,name='timeaction'),
    url('request/',siteadmin_view.viewrequest,name='request'),
    url('accept/(?P<uid>\d+)/$',siteadmin_view.accept,name='accept'),
    url('acceptaction/',siteadmin_view.acceptaction,name='acceptaction'),
    url('accepted/',siteadmin_view.accepted,name='accepted'),
    url('booking/',siteadmin_view.booking,name='booking'),
    url('pay/(?P<uid>\d+)/$',siteadmin_view.pay,name='pay'),
    url('payaction/',siteadmin_view.payaction,name='payaction'),
    url('viewbooked/',siteadmin_view.viewbooked,name='viewbooked'),
    url('see/',siteadmin_view.see,name='see'),
    
   
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
