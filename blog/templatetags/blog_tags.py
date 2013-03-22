from django import template
from azh.blog.models import Entry, Category

register = template.Library()

#used for generating latest posts in footer
class LatestEntriesNode(template.Node):
	def render(self, context):
		context['latest_entries'] = Entry.objects.all()[:5]
		return ''

@register.tag
def do_latest_entries(parser, token):
	return LatestEntriesNode()


#register.tag('get_latest_entries', do_latest_entries)


#used for generating categories list in main menu dropdown
class BlogCategoriesNode(template.Node):
	def render(self, context):
		context['blog_categories'] = Category.objects.all()

@register.tag
def get_categories(parser, token):
	return BlogCategoriesNode()

