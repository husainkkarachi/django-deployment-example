from django.conf.urls import url
from level5app import views

app_name = 'level5app'

urlpatterns=[
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='user_login'),
    ]
