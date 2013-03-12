
from django.conf.urls.defaults import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    
    #url(r'hospitalsafety/', include('azh.hospitals.urls')),
    
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^tiny_mce/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/opt/django-projects/tinymce/jscripts/tiny_mce/' }),
    
    url(r'^blog/', include('azh.blog.urls')),
    url(r'', include('django.contrib.flatpages.urls')),
    
    )



urlpatterns += staticfiles_urlpatterns()
