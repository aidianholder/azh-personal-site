from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from azh.blog.forms import ContactForm
from azh.blog.feeds import LatestEntries

urlpatterns = patterns('azh.blog.views',
                      url(r'^$', 'entries_index', name="index"),
                      url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>\D+)/$', 'entry_detail', name="post"),
                      url(r'^(?P<year>\d{4})/(?P<month>\w{3})/$', 'month_archive', name="month-archive"),
                      url(r'^archives/$', 'full_archive', name="archive"),
                      url(r'^categories/$', 'category_all', name='categories'),
                      url(r'^category/(?P<category>\D+)/$', 'category_detail', name="category"),
                      url(r'^about/contact/$', 'contact', name="contact"),
                      url(r'^about/contact/success/$', direct_to_template, {'template': 'blog/contact_success.html', 'extra_context':{'form':ContactForm()}}, name="success"),
                      url(r'^feed/$', LatestEntries()),
                      )
