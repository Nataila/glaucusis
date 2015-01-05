from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.views.generic import RedirectView
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', RedirectView.as_view(url='/login/')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', include('apps.users.urls')),
    url(r'^home/$', include('apps.home.urls')),
    url(r'^stock/$', include('apps.stock.urls'))
)
