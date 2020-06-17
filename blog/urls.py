from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views

from django.conf.urls import url

from . import views
from .models import LikeDislike
from blog.models import Post, Comment

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    path('post/<pk>/publish/', views.post_publish, name='post_publish'),
    path('post/<pk>/remove/', views.post_remove, name='post_remove'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),

    path('post/<int:pk>/like', views.VotesView.as_view(model=Post, vote_type=LikeDislike.LIKE), name='like_post'),
    path('post/<int:pk>/dislike', views.VotesView.as_view(model=Post, vote_type=LikeDislike.DISLIKE), name='dislike_post'),
# path(r'^article/(?P<pk>\d+)/like/$',
#         login_required(views.VotesView.as_view(model=Post, vote_type=LikeDislike.LIKE)),
#         name='article_like'),
#     path(r'^article/(?P<pk>\d+)/dislike/$',
#         login_required(views.VotesView.as_view(model=Post, vote_type=LikeDislike.DISLIKE)),
#         name='article_dislike'),
#     path(r'^comment/(?P<pk>\d+)/like/$',
#         login_required(views.VotesView.as_view(model=Comment, vote_type=LikeDislike.LIKE)),
#         name='comment_like'),
#     path(r'^comment/(?P<pk>\d+)/dislike/$',
#         login_required(views.VotesView.as_view(model=Comment, vote_type=LikeDislike.DISLIKE)),
#         name='comment_dislike'),
 ]






