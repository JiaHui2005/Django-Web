from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.db.models import Q
from .models import Post
from .forms import PostForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class PostListView(ListView):
    model = Post
    template_name = 'core/post_list.html'
    context_object_name = 'posts'
    ordering = ['-created_at'] 
    paginate_by = 5

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get('q')
        
        if q:
            qs = qs.filter(
                Q(title__icontains = q) | Q(content__icontains = q) 
            )
            
        return qs
        

class PostCreateView(LoginRequiredMixin ,CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'core/post_form.html'
    success_url = reverse_lazy('post_list')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin ,UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'core/post_form.html'
    success_url = reverse_lazy('post_list')
    
    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user
    
class PostDeleteView(UserPassesTestMixin ,DeleteView):
    model = Post
    template_name = 'core/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')
    
    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user


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

# def post_list(request):
#     posts = Post.objects.all().order_by('-created_at')
#     return render(request, 'core/post_list.html', {'posts': posts})

# def post_create(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('post_list')
        
#     else:
#         form = PostForm()
        
#     return render(request, 'core/post_form.html', {'form': form})

# def post_update(request, pk):
#     post = get_object_or_404(Post, pk=pk)
    
#     if request.method == 'POST':
#         form = PostForm(request.POST, instance=post)
#         if form.is_valid():
#             form.save()
#             return redirect('post_list')
        
#     else:
#         form = PostForm(instance=post)
        
#     return render(request, 'core/post_form.html', {'form': form})

# def post_delete(request, pk):
#     post = get_object_or_404(Post, pk=pk)
    
#     if request.method == 'POST':
#         post.delete()
#         return redirect('post_list')
    
#     return render(request, 'core/post_confirm_delete.html', {'post': post})
        
