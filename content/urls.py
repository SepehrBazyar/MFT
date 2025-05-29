from django.urls import path

from content.views import (
    post_list,
    post_detail,
)


app_name, urlpatterns = "content", [
    path(
        "post/",
        post_list,
        name="post-list",
    ),
    path(
        "post/<int:id>/",
        post_detail,
        name="post-detail",
    )
]
