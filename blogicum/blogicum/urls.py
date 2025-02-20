from django.contrib import admin
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import include, path, reverse_lazy
import debug_toolbar
from django.conf import settings
from django.conf.urls.static import static


handler404 = 'pages.views.page_not_found'
handler500 = 'pages.views.server_error'

urlpatterns = [
    path(
        'pages/',
        include('pages.urls', namespace='pages')
    ),
    path(
        '',
        include('blog.urls', namespace='blog')
    ),
    path(
        'auth/',
        include('django.contrib.auth.urls')
    ),
    path(
        'admin/',
        admin.site.urls
    ),
    path('__debug__/', include(debug_toolbar.urls)),
    path(
        'auth/registration/',
        CreateView.as_view(
            template_name='registration/registration_form.html',
            form_class=UserCreationForm,
            success_url=reverse_lazy('blog:index'),
        ),
        name='registration',
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
