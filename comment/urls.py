from django.urls import path, re_path
from django.views.decorators.cache import cache_page

from . import views

urlpatterns = [
    path('<int:song_id>.html',views.commentView,name="comment")
]