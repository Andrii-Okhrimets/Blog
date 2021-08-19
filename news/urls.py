from django.urls import path
from .views import *

urlpatterns = [
    path('log_in/', Log_IN.as_view(), name='log_in'),
    path('log_up/', log_up, name='log_up'),
    path('logout/', log_out, name='logout'),
    path('', HomePost.as_view(), name='home'),
    path('category/<int:category_id>/', CategoryPost.as_view(), name='category'),
    path('posts/<int:pk>/', OnePost.as_view(), name='posts'),
    path('post/add_post/', Add_Post.as_view(), name='add_post'),
    path('<int:pk>/update_post/', Update_Post.as_view(), name='update_post'),
    path('<int:pk>/delete_post/', Delete_Post.as_view(), name='delete_post'),
]