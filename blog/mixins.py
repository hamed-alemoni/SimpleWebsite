from django.shortcuts import get_object_or_404, redirect
from django.http import Http404
from .models import Post


class AuthorAccessMixin():
    # check a post belongs to current user or not and up to them show proper response
    def dispatch(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        if post.author == request.user or request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404('You don\'t have permission')
