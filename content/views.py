from django.http import HttpRequest
from django.views import generic
from django.shortcuts import redirect

from content.forms import CommentForm
from content.models import Post

# Create your views here.
class PostListView(generic.ListView):
    model = Post
    template_name = "content/list.html"
    context_object_name = "posts"


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "content/detail.html"
    context_object_name = "post"
    pk_url_kwarg = "id"

    comment_form = CommentForm

    def post(self, request: HttpRequest, id: int, *args, **kwargs):
        form = self.comment_form(data=request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.get_object()
            comment.save()
            return redirect("content:post-detail", id=id)

        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            comment_form=self.comment_form(),
        )
        return context
