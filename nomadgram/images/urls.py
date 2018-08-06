from django.urls import path, re_path
from . import views
app_name = "nomadgram.images'"

#https://docs.djangoproject.com/en/2.0/ref/urls/#path
urlpatterns = [
    re_path(r'^$', view=views.Images.as_view(), name='feed'),
    re_path(r'^(?P<image_id>[0-9]+)/$', view=views.ImageDetail.as_view(), name='feed'),
    re_path(r'^(?P<image_id>[0-9]+)/likes/$', view=views.LikeImage.as_view(), name='like_image'),
    re_path(r'^(?P<image_id>[0-9]+)/unlikes/$', view=views.UnLikeImage.as_view(), name='like_image'),
    re_path(r'^(?P<image_id>[0-9]+)/comments/$', view=views.CommentOnImage.as_view(), name='comment_image'),
    re_path(r'^(?P<image_id>[0-9]+)/comments/(?P<comment_id>[0-9]+)/$', view=views.ModerateComments.as_view(), name='comment_image'),
    re_path(r'^comments/(?P<comment_id>[0-9]+)/$', view=views.Comment.as_view(), name='comment'),
    re_path(r'^search/$', view=views.Search.as_view(), name='search'),

    # path("all/", view=views.ListAllImages.as_view(), name="all_images"),
    # path("comments/", view=views.ListAllComments.as_view(), name="all_comments"),
    # path("likes/", view=views.ListAllLikes.as_view(), name="all_likes"),
]

# /images/2/like/

# 0 create the url and the view
# 1 take the id from the url
# 2 we want to find an image with this id
# 3 we want to create like for the image