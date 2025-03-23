from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.contrib.auth import logout
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import Post, Comment
from .forms import CustomUserCreationForm, CommentForm


# Create your views here.
def index(request):
    return render(request, "blog/home.html")


class LogoutView(LogoutView):
    success_url = "/home/"


def logout_view(request):
    logout(request)
    return redirect("/login/")


def register(request):

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/login/")
    else:
        form = CustomUserCreationForm()
    context = {
        "form": form,
    }
    return render(request, "blog/register.html", context)


class ProfileManagement(UpdateView):
    pass


@login_required
def profile(request):
    if request.method == "POST":
        user = User.objects.get(user=request.user)
        form = CustomUserCreationForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect("/login/")
    else:
        form = CustomUserCreationForm()
    context = {"form": form}

    return render(request, "blog/profile.html", context)


class PostListView(ListView):
    model = Post
    queryset = Post.objects.all()
    template_name = "blog/post_list.html"


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    queryset = Post.objects.all()
    template_name = "blog/post_detail.html"


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "content", "author"]
    success_url = "/posts/"
    template_name = "blog/post_form.html"


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ["title", "content", "author"]
    success_url = "/posts/"
    template_name = "blog/post_form.html"

    def test_func(self):
        return self.get_object().author == self.request.user


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = "/posts/"
    template_name = "blog/post_confirm_delete.html"

    def test_func(self):
        return self.get_object().author == self.request.user

    # Though I have implemented the UserPassesTestMixin, I didn't understand it more research needed.


class CommentCreateView(CreateView):
    model = Comment
    fields = ["post", "content", "author"]
    success_url = "/posts/"
    template_name = "blog/comment_form.html"


class CommentUpdateView(UpdateView):
    model = Comment
    context_object_name = "comment"
    fields = ["post", "content", "author"]
    template_name = "blog/post_detail.html"


class CommentDeleteView(DeleteView):
    model = Comment
    success_url = "/posts/"
    template_name = "blog/comment_confirm_delete.html"