from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    url(r'^$', 'resumize.views.home'),
    url(r'resume/^$', 'resumize.views.resume'),
    url(r'^submit_resume/$', 'resumize.views.submit_resume'),

    url(r'^admin/', include(admin.site.urls)),
)\

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
