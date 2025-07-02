from django.urls import path

from content.views import (
    PostDetailView,
    PostListView,
)


app_name, urlpatterns = "content", [
    path(
        "post/",
        PostListView.as_view(),
        name="post-list",
    ),
    path(
        "post/<int:id>/",
        PostDetailView.as_view(),
        name="post-detail",
    ),
]
