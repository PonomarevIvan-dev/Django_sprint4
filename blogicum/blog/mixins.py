from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.mixins import UserPassesTestMixin
from .models import Post


class PostMixin:
    model = Post
    template_name = 'blog/create.html'


class CommentEditMixin:
    template_name = 'blog/comment.html'
    pk_url_kwarg = 'comment_id'

    def get_success_url(self):
        return reverse('blog:post_detail',
                       kwargs={'post_id': self.kwargs['post_id']})


class AuthorPermissionMixin:
    """Миксин для проверки прав автора на объект."""

    def dispatch(self, request, *args, **kwargs):
        obj = get_object_or_404(self.model, pk=kwargs[self.pk_url_kwarg])
        if obj.author != request.user:
            return redirect('blog:post_detail', post_id=kwargs['post_id'])
        return super().dispatch(request, *args, **kwargs)


class AuthorRequiredMixin(UserPassesTestMixin):
    """Миксин для проверки, является ли пользователь автором объекта."""

    def test_func(self):
        """Проверяет, является ли пользователь автором объекта."""
        obj = self.get_object()
        return obj.author == self.request.user

    def handle_no_permission(self):
        """Обрабатывает случай, когда пользователь не является автором."""
        return redirect('blog:post_detail', post_id=self.get_object().pk)
