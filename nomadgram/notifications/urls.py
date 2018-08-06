from django.urls import path, re_path
from . import views
app_name = "nomadgram.notifications"

#https://docs.djangoproject.com/en/2.0/ref/urls/#path
urlpatterns = [
    re_path(r'^$', view=views.Notifications.as_view(), name='notifications'),

]