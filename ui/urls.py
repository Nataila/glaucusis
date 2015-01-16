from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.views.generic import RedirectView
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin', include(admin.site.urls)),
    url(r'^home/$', include('apps.home.urls')),
    url(r'^stock/', include('apps.stock.urls')),
    url(r'^choice/$', include('apps.choice.urls')),
    url(r'^news/$', include('apps.news.urls')),
    url(r'^simulate/$', include('apps.simulate.urls')),
)

urlpatterns += patterns('',
    url(r'^$', RedirectView.as_view(url='/login/')),
    url(r'^login/$', include('apps.users.urls')),
    url(r'^auth_logout', 'apps.users.views.auth_logout', name='auth_logout'),
    url(r'^register/$', 'apps.users.views.register', {'template': 'users/register.html'}, 'register'),
)
