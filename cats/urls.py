
from django.urls import path
from . import views

app_name = 'cats'

urlpatterns = [
    path('', views.CatPostListView.as_view(), name='list'),
    path('home/', views.home, name='home'),
    path('post/new/', views.CatPostCreateView.as_view(), name='create'),
    path('post/<int:pk>/', views.cat_detail, name='post_detail'),
]

