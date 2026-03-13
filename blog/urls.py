from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    # home page
    path("", views.index, name="index"),

    # detail page using integer ID
    path("post/<int:post_id>/", views.post_detail, name="post-detail"),

    # detail page using slug (we'll use this more seriously later)
    path("post/slug/"
         "<slug:slug>/", views.post_detail_slug, name="post-detail-slug"),

    # new url
    path("new-url/", views.new_blog_url, name="new-blog-url"),

    # old url that should redirect to the new url
    path("old-url/", views.old_blog_url, name="old-blog-url"),
]
