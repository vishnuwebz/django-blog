from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse

def index(request):
    return HttpResponse("Hello, world. this is the blog home page!")

def post_detail(request, post_id: int):
    """
    Temporary detail view using an integer ID.
    In a future module, we'll fetch data from the database using this ID.
    """
    return HttpResponse(f"Post detail page for post ID: {post_id}")

def post_detail_slug(request, slug: str):
    """
    Temporary detail view using a slug.
    Later, we'll use this to fetch posts by slug from the database.
    :param request:
    :param slug:
    :return:
    """
    return HttpResponse(f"Post detail page for slug: {slug}")

def new_blog_url(request):
    """
    This represents a new URL users should use.
    """
    return HttpResponse("You have been redirected to the NEW blog URL.")

def old_blog_url(request):
    """
    This view demonstrates how to redirect from an old URL to a new one.
    We use the URL name instead of hard-coding the path.
    """
    new_url = reverse("blog:new-blog-url")
    return redirect(new_url)