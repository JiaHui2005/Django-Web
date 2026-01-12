from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .models import Post
from .forms import PostForm

def home(request):
    context = {
        'user_name': 'Huy Huy',
        'is_logged_in': True,
        'tasks': ['Learn Django', 'Build Project', 'Get Job'],
    }
    
    return render(request, 'core/home.html', context)

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    contact = {
        'email': 'vogiahuypro9@gmail.com',
        'phone': '0352582180',
        'facebook': 'Huy Huy',
    }
    
    return render(request, 'core/contact.html', contact)

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'core/post_list.html', {'posts': posts})

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
        
    else:
        form = PostForm()
        
    return render(request, 'core/post_form.html', {'form': form})

def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_list')
        
    else:
        form = PostForm(instance=post)
        
    return render(request, 'core/post_form.html', {'form': form})

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    
    return render(request, 'core/post_confirm_delete.html', {'post': post})
        
