from django.urls import path, re_path

from . import views

app_name = "users"

urlpatterns = [
    re_path(r'^explore/$', view=views.ExploreUsers.as_view(), name='explore_users'),
    re_path(r'^(?P<user_id>[0-9]+)/follow/$', view=views.FollowUser.as_view(), name='follow_users'),
    re_path(r'^(?P<user_id>[0-9]+)/unfollow/$', view=views.UnFollowUser.as_view(), name='follow_users'),
    re_path(r'^(?P<username>\w+)/followers/$', view=views.UserFollowers.as_view(), name='user_followers'),
    re_path(r'^(?P<username>\w+)/following/$', view=views.UserFollowing.as_view(), name='user_following'),
    re_path(r'^search/$', view=views.Search.as_view(), name='user_following'),
    re_path(r'^(?P<username>\w+)/$', view=views.UserProfile.as_view(), name='user_profile'),
    re_path(r'^(?P<username>\w+)/password/$', view=views.ChangePassword.as_view(), name='change'),
    re_path(r'^login/facebook/$', view=views.FacebookLogin.as_view(), name='fb_login'),
]