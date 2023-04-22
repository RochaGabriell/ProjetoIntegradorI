from django.urls import path
from blog.views.HomeView import HomeView
from blog.views.NewPostView import NewPostView

app_name = 'blog'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('new_post/', NewPostView.as_view(), name='new_post'),
]