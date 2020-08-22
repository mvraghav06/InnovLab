from django.contrib import admin
from . import views
from django.conf.urls import url

app_name='Tmplate'

urlpatterns = [
    url(r'^home/',views.home,name='home'),
    url(r'^login/',views.user_login,name='login'),
    url(r'^register/',views.register,name='register'),
    url(r'^page1/',views.page1,name='page1'),
    url(r'^page2/',views.page2,name='page2'),
    ]
