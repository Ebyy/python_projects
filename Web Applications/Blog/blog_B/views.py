from django.shortcuts import render
from .models import BlogPost, Entry
from django.http import HttpResponseRedirect
from .forms import BlogPostForm, EntryForm
from django.core.urlresolvers import reverse


# Create your views here.

def index(request):
    """Return processed view response"""
    return render(request, 'blog_B/index.html')


def posts(request):
    """Return view with list of post headlines."""
    posts = BlogPost.objects.order_by('date_added')
    context = {'posts': posts}
    return render(request, 'blog_B/posts.html', context)


def post(request, entry_id):
    """Process view for post content."""
    post = BlogPost.objects.get(id=entry_id)
    entries = post.entry_set.order_by('-date_added')
    context = {'post': post, 'entries': entries}
    return render(request, 'blog_B/post.html', context)


def new_post(request):
    """Enable users to add posts."""
    if request.method != 'POST':
        form = BlogPostForm()
    else:
        form = BlogPostForm(data=request.POST)
        if form.is_valid():             # entry satisfies all specified attributes of the model.
            form.save()
            return HttpResponseRedirect(reverse('blog_B:posts'))
    context = {'form': form}
    return render(request, 'blog_B/new_post.html', context)


def new_entry(request, post_id):
    """Enable user to make entries to their post."""
    post = BlogPost.objects.get(id=post_id)

    if request.method != 'POST':
        # if no entry yet create form for entry.
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.post = post       # assigns the new entry to the corresponding topic pulled from the db
            new_entry.save()
            return HttpResponseRedirect(reverse('blog_B:post', args=[post_id]))
    context = {'post': post, 'form': form}
    return render(request, 'blog_B/new_entry.html', context)


def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    post = entry.post

    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blog_B:post',
                                                args=[post.id]))
    context = {'entry': entry, 'post': post, 'form': form}
    return render(request, 'blog_B/edit_entry.html', context)
