from django.contrib.syndication.views import Feed
from azh.blog.models import Entry

class LatestEntries(Feed):
    title = "Latest Posts"
    link = "/rss/"
    description = "The latest posts on aidianholder.net"
    
    def items(self):
        return Entry.objects.order_by('-pub_date')[:5]
    
    def item_title(self, item):
        return item.head
    
    def item_description(self, item):
        return item.body.split('. ')[0]
        