from django.shortcuts import render_to_response
from django.template import Context, loader, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from azh.blog.models import Entry, Category
from azh.blog.forms import ContactForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, InvalidPage



def entries_index(request):
    
    entries = Entry.objects.all()
    #months = Entry.objects.dates('pub_date', 'month', order='DESC')
    #categories = Category.objects.all()
    paginator = Paginator(entries, 6)
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        page = 1
    try:
        p = paginator.page(page)
    except (EmptyPage, InvalidPage):
        p = paginator.page(paginator.num_pages)
    return render_to_response('blog/entry_index.html', { 'entry_list': p}, context_instance=RequestContext(request))

def full_archive(request):
    entries = Entry.objects.all()
    months = Entry.objects.dates('pub_date', 'month', order='DESC')
    return render_to_response('blog/posts_archive.html', {'entry_list':entries, 'month_list':months}, context_instance=RequestContext(request))




def month_archive(request, year, month):
    import time, datetime
    entries = Entry.objects.all()
    months = Entry.objects.dates('pub_date', 'month', order='DESC')
    #featured_posts = entries.filter(featured=True)
    date_stamp = time.strptime(str(year)+str(month)+str(1), "%Y%b%d")
    pub_date = datetime.date(*date_stamp[:3])
    entries = entries.filter(pub_date__month=pub_date.month, pub_date__year=pub_date.year)
    categories = Category.objects.all()
    paginator = Paginator(entries, 6)
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        page = 1
    try:
        p = paginator.page(page)
    except (EmptyPage, InvalidPage):
        p = paginator.page(paginator.num_pages)
    return render_to_response('blog/entry_index.html', { 'page_title':str(year)+str(month), 'entry_list': p, 'category_list':categories, 'months':months}, context_instance=RequestContext(request))

def category_detail(request, category):
    entries = Entry.objects.all()
    months = Entry.objects.dates('pub_date', 'month', order='DESC')
    featured_posts = entries.filter(featured=True)
    categories = Category.objects.all()
    entries = entries.filter(category__slug=category)
    paginator = Paginator(entries, 6)
    
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        page = 1
        
    try:
        p = paginator.page(page)
    except (EmptyPage, InvalidPage):
        p = paginator.page(paginator.num_pages)
   
    return render_to_response('blog/entry_index.html', { 'page_title':category, 'entry_list': p, 'featured_list': featured_posts, 'category_list':categories, 'months':months })
    
    

def entry_detail(request, year, month, day, slug):
    import datetime, time
    entries = Entry.objects.all()
    months = Entry.objects.dates('pub_date', 'month', order='DESC')
    categories = Category.objects.all()
    date_stamp = time.strptime(year+month+day, "%Y%b%d")
    pub_date = datetime.date(*date_stamp[:3])
    entry = get_object_or_404(Entry, 
                              pub_date__year=pub_date.year,
                              pub_date__month=pub_date.month,
                              pub_date__day=pub_date.day,
                              slug=slug)
    return render_to_response('blog/entry_detail.html', {'page_title':'post', 'entry':entry, 'category_list':categories, 'months':months})

def send_message(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            sub = cd['subject']
            msg = cd['message']
            add = cd['email']
            print sub, msg, add
        return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm()
    return render_to_response('contact_form.html', {'form':form})

def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))
            
