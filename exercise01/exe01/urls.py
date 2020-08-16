from django.conf.urls import url
from exe01 import views

app_name = 'exe01'

urlpatterns = [
    url(r'^apps/$',views.apps, name = 'apps'),
    url('registration/',views.registration, name = 'registration'),
    url(r'^users/',views.users_ls, name = 'users'),
    url(r'^login/',views.user_login, name = 'user_login'),
]
