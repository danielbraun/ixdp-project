from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.list import ListView
from django.conf import settings
from grades.models import ClassEvaluation


admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', ListView.as_view(model=ClassEvaluation)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
