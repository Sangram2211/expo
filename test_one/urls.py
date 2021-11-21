from django.urls import include, path, re_path
from test_one.views import *

app_name = 'test_one'

urlpatterns = [

    path('get_api',get_api,name='get_api'),

    path('post_api',post_api,name='post_api'),
]
