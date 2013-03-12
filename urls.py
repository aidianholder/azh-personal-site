
from django.conf.urls.defaults import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
admin.autodiscover()
from azh.blog.forms import ContactForm
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('',
    
    #url(r'hospitalsafety/', include('azh.hospitals.urls')),
    
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^tiny_mce/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/opt/django-projects/tinymce/jscripts/tiny_mce/' }),
    
    url(r'^blog/', include('azh.blog.urls')),
    url(r'^about/contact/$', 'azh.blog.views.contact', name="contact"),
    url(r'^about/contact/success/$', direct_to_template, {'template': 'blog/contact_success.html', 'extra_context':{'form':ContactForm()}}, name="success"),
    url(r'', include('django.contrib.flatpages.urls')),
    
    )



urlpatterns += staticfiles_urlpatterns()
