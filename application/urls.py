from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$', views.feed, name='feed'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^project/(\d+)/$', views.project, name='project'),
    url(r'^accounts/register/complete/$', views.edit_profile, name='edit_profile'),
    url(r'upload/$', views.upload, name='upload'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)