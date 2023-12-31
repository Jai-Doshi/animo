from django.urls import path
from . import views

app_name = 'posts'

urlPatterns = [
	path('',views.PostList.as_view(),name='all'),
	path('new/',views.CreatePost.as_view(),name='create'),
	path('by/<username>',views.UserPosts.as_view(),name='for_user'),
	path('by/<username>/init:<pk>',views.PostDetail.as_view(),name='single'),
	path("delete/<int:pk>/",views.DeletePost.as_view(),name="delete"),
]