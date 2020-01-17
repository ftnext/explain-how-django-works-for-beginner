from django.urls import path

from . import views


urlpatterns = [
    # URLが 127.0.0.1:8000/ のときは、blog/views.py の post_list 関数を呼び出す
    path('', views.post_list, name='post_list'),
    # URLが 127.0.0.1:8000/ 以外の場合は設定していないのでエラー
]
