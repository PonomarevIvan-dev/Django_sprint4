from django.urls import reverse

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


