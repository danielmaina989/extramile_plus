from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name= 'blog'
urlpatterns = [

        # 🔹 Login & Logout URLs
    path('admin-login/', auth_views.LoginView.as_view(template_name='blog/admin_login.html'), name='admin_login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='blog:blog_list'), name='logout'),

    path('', views.BlogListView.as_view(), name='blog_list'),
    path('add/', views.PostCreateView.as_view(), name='post_create'),
    path('<slug:slug>/edit/', views.PostUpdateView.as_view(), name='post_update'),
    path('<slug:slug>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
        path('<slug:slug>/', views.BlogDetailView.as_view(), name='blog_detail'),


]
