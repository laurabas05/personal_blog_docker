from django.shortcuts import render, redirect
from .models import Post
from comments.forms import CommentForm
from django.contrib.auth.decorators import login_required

def post_list(request):
    posts = Post.objects.all().order_by('-date_published')
    return render(request, 'posts/posts.html', {'posts': posts})

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    comments = post.comments.all().order_by('-created_at')
    form = CommentForm()
    return render(request, 'posts/post_detail.html', {
        'post': post,
        'comments': comments,
        'form': form,
    })

@login_required(login_url='users:login')
def add_comment(request, slug):
    post = Post.objects.get(slug=slug)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.author = request.user
            new_comment.post = post
            new_comment.save()
    return redirect('posts:post_detail', slug=post.slug)