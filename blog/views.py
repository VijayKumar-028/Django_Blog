from django.shortcuts import render
from django.views.generic import (ListView,
                                  DetailView
,CreateView,UpdateView,DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .models import Post

def home(request):
    context={
        'posts':Post.objects.all()
    }
    return render(request,'blog/home.html',context)

class PostListView(ListView):           #List view for the posts
    model=Post
    template_name = 'blog/home.html' #<app>/<model>_<viewtype>.html
    context_object_name='posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView): #detailed view for every post
    model=Post

class PostCreateView(LoginRequiredMixin,CreateView):  #creation of the post
    model=Post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):        #Updation of the post
    model=Post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)

    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):        #Deletion of the post
    model=Post
    success_url = '/'
    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False

def about(request):
    return render(request,'blog/about.html',{'title':'about'})

