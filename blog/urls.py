from django.urls import path
from .views import (PostListView,
                    PostDetailView
, PostCreateView, PostUpdateView,PostDeleteView)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),#TO get the detail view of the single post if we click on the post
    path('post/new/', PostCreateView.as_view(), name='post-create'),#To create the new post
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),# To update the exisitng post
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'), # To delete the existing post
    path('about/',views.about,name='blog-about')
]
