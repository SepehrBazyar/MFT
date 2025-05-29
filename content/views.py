from django.http import HttpRequest
from django.shortcuts import (
    render,
    get_object_or_404,
)

from content.models import Post

# Create your views here.
def post_list(request: HttpRequest):
    posts = Post.objects.all()
    return render(
        request,
        "content/list.html",
        context={
            "posts": posts,
        },
    )


def post_detail(request: HttpRequest, id: int):
    post = get_object_or_404(Post, id=id)
    return render(
        request,
        "content/detail.html",
        context={
            "post": post,
            "comments": post.comments.count(),
        },
    )
