from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('board/', views.board, name='board'),
    path('board/<int:postId>/', views.post_detail, name='post_detail'),
    path('board/post_add', views.post_add, name='post_add'),
    path('board/post_new', views.post_new, name='post_new'),
    path('board/<int:postId>/post_edit/', views.post_edit, name='post_edit'),
    path('board/<int:postId>/post_update/', views.post_update, name='post_update'),
    path('board/<int:postId>/post_remove/', views.post_remove, name='post_remove'),
]