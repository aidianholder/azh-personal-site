from django.conf.urls.defaults import *

urlpatterns = patterns('azh.blog.views',
                      url(r'^$', 'entries_index', name="index"),
                      url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>\D+)/$', 'entry_detail', name="post"),
                      url(r'^(?P<year>\d{4})/(?P<month>\w{3})/$', 'month_archive', name="month-archive"),
                      url(r'^archives/$', 'full_archive', name="archive"),

                      url(r'^category/(?P<category>\D+)/$', 'category_detail', name="category"),
                      url(r'^sendmessage/$', 'send_message', name="sendmessage"),
                      )
