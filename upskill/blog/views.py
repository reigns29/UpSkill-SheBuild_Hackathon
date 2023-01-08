from django.shortcuts import render, redirect
from .forms import BlogPostForm
from .models import Post


def list_posts(request):
    if request.user.is_anonymous:
        return redirect("/login")
    posts = Post.objects.all()
    return render(request, "blog_list.html", {"posts": posts})


def view_post(request, post_id):
    if request.user.is_anonymous:
        return redirect("/login")
    post = Post.objects.get(id=post_id)
    post.count += 1
    post.save()
    return render(request, "blog_view.html", {"post": post})


def new_post(request):
    if request.user.is_anonymous:
        return redirect("/login")
    if request.method == "POST":
        form = BlogPostForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            post = Post.objects.create(
                title=form.cleaned_data["title"],
                content=form.cleaned_data["content"],
                # Add any other fields you want to include
            )
            return redirect("/blog", post_id = post.id)
    else:
        form = BlogPostForm()
    return render(request, "blog_new.html", {"form": form})


def top_posts(request):
    if request.user.is_anonymous:
        return redirect("/login")
    post = Post.objects.all().order_by('-count' )
    return render(request, "blog_topfeed.html", {"posts": post})

def count(request):
    pass    
